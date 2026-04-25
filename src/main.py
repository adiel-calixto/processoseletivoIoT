from ssd1306 import SSD1306_I2C
from mpu6050 import MPU6050
from machine import I2C, Pin
import onewire, ds18x20
import time, math

# Pinos
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
mpu = MPU6050(i2c)
buzzer = Pin(25, Pin.OUT)
ds_pin = Pin(4)
ow = onewire.OneWire(ds_pin)
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

# Parâmetros
AMOSTRAS = 50
LIMIAR_ZSCORE = 2.5
LIMIAR_TEMP = 60.0  # °C


# Funções auxiliares
def media_desvio(valores):
    n = len(valores)
    med = sum(valores) / n
    var = sum((v - med) ** 2 for v in valores) / n
    return med, math.sqrt(var)


def zscore(valor, media, desvio):
    return abs(valor - media) / (desvio + 0.001)


def mostrar_oled(linha1, linha2="", linha3=""):
    oled.fill(0)
    oled.text(linha1, 0, 0)
    oled.text(linha2, 0, 20)
    oled.text(linha3, 0, 40)
    oled.show()


def beep():
    buzzer.on()
    time.sleep_ms(200)
    buzzer.off()


# Calibração
def calibrar():
    mostrar_oled("Calibrando...", "Aguarde")
    print("Calibrando...")

    lx, ly, lz = [], [], []

    for i in range(AMOSTRAS):
        accel = mpu.read_accel_data(g=True)
        x, y, z = accel["x"], accel["y"], accel["z"]
        lx.append(x)
        ly.append(y)
        lz.append(z)
        time.sleep_ms(50)

    mx, dx = media_desvio(lx)
    my, dy = media_desvio(ly)
    mz, dz = media_desvio(lz)

    print(f"Media:  X={mx:.2f} Y={my:.2f} Z={mz:.2f}")
    print(f"Desvio: X={dx:.2f} Y={dy:.2f} Z={dz:.2f}")
    mostrar_oled("Calibrado!", "Monitorando...")
    time.sleep(1)

    return (mx, dx), (my, dy), (mz, dz)


# Setup
(mx, dx), (my, dy), (mz, dz) = calibrar()

# Loop principal
print("Monitorando...")

while True:
    # Leitura do acelerômetro
    accel = mpu.read_accel_data(g=True)
    x, y, z = accel["x"], accel["y"], accel["z"]
    zx = zscore(x, mx, dx)
    zy = zscore(y, my, dy)
    zz = zscore(z, mz, dz)

    # Leitura do DS18B20
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(roms[0]) if roms else 0.0

    # Detecção
    anomalia_vib = zx > LIMIAR_ZSCORE or zy > LIMIAR_ZSCORE or zz > LIMIAR_ZSCORE
    anomalia_temp = temp > LIMIAR_TEMP
    anomalia = anomalia_vib or anomalia_temp

    # Log serial
    status = "ANOMALIA!" if anomalia else "Normal"
    print(f"{status} | X={x:.2f} Y={y:.2f} Z={z:.2f} T={temp:.1f}C")

    # Display OLED
    if anomalia:
        motivo = "Vibracao!" if anomalia_vib else "Temperatura!"
        mostrar_oled("!! ANOMALIA !!", motivo, f"T={temp:.1f}C")
        beep()
    else:
        mostrar_oled("Status: OK", f"T={temp:.1f}C", f"Z={max(zx,zy,zz):.1f}")

    time.sleep_ms(200)
