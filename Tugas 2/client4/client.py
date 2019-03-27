import socket


TARGET_IP = '127.0.0.1'
TARGET_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("ok", (TARGET_IP, TARGET_PORT))

def menerima():
    ditulis = 0

    while True:
        data, addr = sock.recvfrom(1024)
        if(data[0:5]=="mulai"):
            print data[6:]
            fp = open(data[6:],'wb+')
        elif(data=="selesai"):
            ditulis = 0
            fp.close()
        elif(data=="berhenti"):
            break
        else:
            fp.write(data)
            print "blok ", len(data), data[0:10]

while True:
    data, addr = sock.recvfrom(1024)
    if(data=="kirim"):
        menerima()
        break

