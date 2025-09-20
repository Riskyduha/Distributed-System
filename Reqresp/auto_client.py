import socket, time

def run_client():
    time.sleep(2)
    s = socket.socket()
    s.connect(("reqresp-server", 4444))
    for msg in ["hello", "distributed", "systems", "bye"]:
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print("CLIENT RECEIVED:", data)
        if msg == "bye":
            break
    s.close()

if __name__ == '__main__':
    run_client()