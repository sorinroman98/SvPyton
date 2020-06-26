import socket
import threading

HEAD = 1000
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE= 'DISCONECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    
    connected = True 
    while connected:
        msg = conn.recv(HEAD).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE: 
            connected = False

        print(msg)

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()