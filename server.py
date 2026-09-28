import socket
import json
import threading
import constCS

def process_request(data_str):
    """Resolve ASR 04: Processamento no servidor com múltiplas funcionalidades"""
    try:
        req = json.loads(data_str)
        op = req.get('op')
        args = req.get('args', [])
        
        # Múltiplas funcionalidades
        if op == 'ADD':
            result = sum(args)
        elif op == 'MUL':
            result = args[0] * args[1]
        elif op == 'MAX':
            result = max(args)
        else:
            return "Operacao nao suportada."
            
        return f"Resultado ({op}): {result}"
    except Exception as e:
        return f"Erro no processamento: {str(e)}"

def handle_client(conn, addr):
    """Resolve ASR 05: Trata a requisição em uma thread separada"""
    try:
        data = conn.recv(1024)
        if data:
            resposta = process_request(data.decode())
            conn.sendall(resposta.encode())
    except Exception as e:
        print(f"Erro com {addr}: {e}")
    finally:
        conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite reusar a porta rapidamente
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    s.bind((constCS.HOST, constCS.PORT))
    s.listen(100)
    print(f"Servidor Multithread rodando em {constCS.HOST}:{constCS.PORT}...")

    while True:
        conn, addr = s.accept()
        # Dispara uma nova thread para cada requisição recebida (ASR 05)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    start_server()