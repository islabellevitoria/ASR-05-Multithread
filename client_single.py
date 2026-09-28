import socket, json, constCS, random, time

def send_request():
    op = random.choice(['ADD', 'MUL', 'MAX'])
    args = [random.randint(1, 100), random.randint(1, 100)]
    req_data = json.dumps({"op": op, "args": args})
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((constCS.HOST, constCS.PORT))
    s.sendall(req_data.encode())
    s.recv(1024)
    s.close()

def run_experiment_singlethread():
    print(f"Iniciando {constCS.NUM_REQUESTS} requisições SINGLE-THREAD...")
    start_time = time.time()
    
    # Requisições enviadas de forma sequencial
    for _ in range(constCS.NUM_REQUESTS):
        send_request()
        
    end_time = time.time()
    print(f"Tempo total (Cliente Single): {end_time - start_time:.4f} segundos")

if __name__ == '__main__':
    run_experiment_singlethread()