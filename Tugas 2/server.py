from threading import Thread
import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
FILENAME = ["test1.jpg", "test2.jpg", "test3.jpg", "test4.jpg"]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))


def mengirim(CLIENT_IP, CLIENT_PORT):
    addr = CLIENT_IP, CLIENT_PORT
    sock.sendto("kirim", (addr))
    for tiap in FILENAME:
        sock.sendto("mulai {}".format(tiap), (addr))
        ukuran = os.stat(tiap).st_size
        fp = open(tiap, 'rb')
        k = fp.read()
        terkirim = 0
        for x in k:
            sock.sendto(x, (addr))
            terkirim = terkirim + 1
            print "\r terkirim {} of {} ".format(terkirim, ukuran)
        sock.sendto("selesai", (addr))
        fp.close()
    sock.sendto("berhenti", (addr))

if __name__ == "__main__":
	while True:
		print "Terkoneksi"
		data, addr = sock.recvfrom(1024)
		if (data == "ok"):
			thread = Thread(target=mengirim, args=(addr))
			thread.start()


