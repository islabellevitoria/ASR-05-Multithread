[readme_md.md](https://github.com/user-attachments/files/32716210/readme_md.md)
# Sistemas Distribuídos - Tarefa ASR 05: Cliente-Servidor Multithreaded

---

## Estrutura do Projeto

* `constCS.py`: Arquivo de configurações compartilhadas (endereço IP, porta e quantidade de requisições).
* `server.py`: Servidor *multithreaded* capaz de processar operações matemáticas (`ADD`, `MUL`, `MAX`).
* `client.py`: Cliente *multithreaded* automatizado que dispara requisições concorrentes para testes de estresse.
* `client_single.py`: Cliente *single-threaded* sequencial utilizado como base de comparação de desempenho.

---

## Pré-requisitos

É necessário ter o **Python 3** instalado em sua máquina.

Para verificar se o Python já está instalado, abra o terminal e digite:
```bash
python --version
# ou
python3 --version
```

---

## Como Executar o Projeto Passo a Passo

### 1. Clonar ou Acessar a Pasta do Projeto
Navegue até o diretório onde os arquivos estão salvos através do terminal:

```bash
cd caminho/para/a/pasta/ASR05
```

### 2. Iniciar o Servidor
Abra o primeiro terminal e inicie o servidor:

```bash
python server.py
```
> **Nota:** Mantenha este terminal aberto. O servidor exibirá a mensagem `Servidor Multithread rodando em 127.0.0.1:5678...` e ficará aguardando conexões.

### 3. Executar o Experimento Single-Thread (ASR 04)
Abra uma **segunda janela ou aba do terminal**, navegue até a mesma pasta do projeto e execute o cliente sequencial:

```bash
python client_single.py
```
O script enviará 500 requisições sequenciais e exibirá o tempo total decorrido ao finalizar.

### 4. Executar o Experimento Multithread (ASR 05)
No mesmo segundo terminal, execute o cliente *multithreaded*:

```bash
python client.py
```
O script criará *threads* simultâneas para enviar as requisições em paralelo e exibirá o tempo total decorrido.

---
