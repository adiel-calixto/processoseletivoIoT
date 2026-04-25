# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## Relatório do Candidato

---

### 👤 Identificação do Candidato

- **Nome completo:** José Adiel Calixto Serafim
- **GitHub:** https://github.com/adiel-calixto

---

## 1️⃣ Visão Geral da Solução

Sistema de **monitoramento industrial** baseado em ESP32 com MicroPython. Detecta anomalias de vibração (acelerômetro MPU6050) e temperatura (sensor DS18B20), alertando o operador via display OLED e buzzer.

---

## 2️⃣ Arquitetura do Sistema Embarcado

```
┌──────────────────────────────────────────────┐
│                  main.py                     │
│                                              │
│  Calibragem ──► Leitura contínua ──► Detecção│
│      │                  │              │     │
│      ▼                  ▼              ▼     │
│   Média/Desvio      MPU6050         Alerta   │
│   (referência)      DS18B20      OLED/Buzzer │
└──────────────────────────────────────────────┘
```

**Fluxo principal:**
1. `calibrar()` - Coleta 50 amostras do acelerômetro para estabelecer média e desvio padrão
2. Loop infinito - Leitura contínua de aceleração (X/Y/Z) e temperatura
3. `zscore()` - Calcula Z-Score para cada eixo, comparando com a calibração
4. Detecção de anomalia - Vibração (z-score > 2.5) ou temperatura (> 60°C)
5. Alerta - Display OLED exibe status e motivo; buzzer emite beep

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | Função |
|---|---|
| **ESP32 DevKit C v4** | Microcontrolador executando MicroPython |
| **SSD1306 OLED 128x64** | Display para feedback visual ao operador |
| **MPU6050** | Acelerômetro 6-DOF para detecção de vibração |
| **DS18B20** | Sensor de temperatura 1-Wire |
| **Buzzer** | Alerta sonoro em caso de anomalia |
| **Resistor 4.7kΩ** | Pull-up no barramento 1-Wire |

---

## 4️⃣ Decisões Técnicas Relevantes

- **Algoritmo Z-Score:** Utilizado para detecção de vibração incomum, isolando o ruido natural do sensor através da calibração inicial
- **Constantes configuráveis:** `AMOSTRAS`, `LIMIAR_ZSCORE`, `LIMIAR_TEMP` para ajuste fácil
- **Tempo de conversão DS18B20:** `sleep_ms(750)` aguarda conversão completa antes da leitura

---

## 5️⃣ Resultados Obtidos

- Calibragem automática na inicialização com média e desvio exibidos no serial
- Leitura contínua de aceleração (X/Y/Z em g) e temperatura (°C)
- Display OLED mostra "Status: OK" ou "!! ANOMALIA !!" com motivo
- Alerta sonoro emitido ao detectar vibração ou temperatura anômala
- GitHub Actions executando simulação via Wokwi CLI

---

## 6️⃣ Alterações no processo de build/CI

### CI (`.github/workflows/ci.yml`)

| Campo | Antes | Depois |
|-------|-------|--------|
| `expect_text` | `'Teste'` | `'Normal \| '` |

O texto esperado na saída serial foi atualizado de `'Teste'` para `'Normal | '` para refletir o novo formato de output do projeto.

---

### Dockerfile

Os módulos `mpu6050.py` e `ssd1306.py` (drivers para o acelerômetro e display OLED) são copiados separadamente para o filesystem da ESP32, permitindo importação via `import mpu6050` e `import ssd1306`.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
