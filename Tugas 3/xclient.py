import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Input File? -> ")
    if filename[:4] == 'view':
        s.send(filename)
        inputFile = s.recv(1024)
        print "directory: " + str(inputFile)

    else:
        s.send(filename)
    data = s.recv(1024)
    if data[:6] == 'EXISTS':
        filesize = long(data[6:])
        notif = raw_input("File exists, " + str(filesize) + " Bytes, Download? (Y/N) -> ")
        if notif == 'Y':
            s.send("OK")
            new_filename = filename.rsplit("/")[-1]
            f = open('new ' + new_filename, 'wb')
            data = s.recv(1024)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
                data = s.recv(1024)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "%"

            print "Completed!"
            f.close()
    else:
        print "Not Exist!"
    s.close()


if __name__ == '__main__':
    Main()