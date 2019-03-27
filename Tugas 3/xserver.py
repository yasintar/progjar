import socket
import threading
import os

def Process(name, sock):
    filename = sock.recv(1024)

    if filename[:4] == 'list': 
        print "directory list"
        print "path: " + filename[5:]
        filelist = os.listdir(filename[5:])
        print filelist
        sock.send(str(filelist))

    elif os.path.isfile(filename):  
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                totalBytes = f.read(1024)
                sock.send(totalBytes)
                while totalBytes != "":
                    totalBytes = f.read(1024)
                    sock.send(totalBytes)
        else:
            sock.send("Error.")


    else:
        print "Error."

    sock.close()


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)

    print "Server is ready."
    while True:
        c, addr = s.accept()
        print "client connected to " + str(addr)
        t = threading.Thread(target=Process, args=("retrThread", c))
        t.start()

    s.close()


if __name__ == '__main__':
    Main()
