import socket 
import json
import constCS
import random
import time
import threading

def send_request():
    """Conecta, envia requisição automatizada e recebe a resposta"""
    ops = ['ADD', 'MUL', 'MAX']
    op = random.choice(ops)
    args = [random.randint(1, 100), random.randint(1, 100)]
    
    # Automatizando a geração de requisições
    req_data = json.dumps({"op": op, "args": args})
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((constCS.HOST, constCS.PORT))
        s.sendall(req_data.encode())
        resposta = s.recv(1024)
        # print(resposta.decode()) # Comentado para não poluir o terminal durante o experimento de tempo
        s.close()
    except Exception as e:
        pass # Ignora erros de conexão para não atrapalhar o benchmark

def run_experiment_multithread():
    print(f"Iniciando {constCS.NUM_REQUESTS} requisições MULTITHREAD...")
    start_time = time.time()
    
    threads = []
    # Cria uma thread para cada requisição (ASR 05)
    for _ in range(constCS.NUM_REQUESTS):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()
        
    # Aguarda todas as requisições terminarem
    for t in threads:
        t.join()
        
    end_time = time.time()
    print(f"Tempo total (Cliente Multi + Servidor Multi): {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    run_experiment_multithread()