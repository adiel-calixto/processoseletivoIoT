from machine import I2C
import struct

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        # Acorda o sensor
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')

    def _read_raw(self, reg):
        data = self.i2c.readfrom_mem(self.addr, reg, 2)
        val = struct.unpack('>h', data)[0]
        return val

    def acceleration(self):
        x = self._read_raw(0x3B) / 16384.0
        y = self._read_raw(0x3D) / 16384.0
        z = self._read_raw(0x3F) / 16384.0
        return x, y, z

    def temperature(self):
        raw = self._read_raw(0x41)
        return raw / 340.0 + 36.53
