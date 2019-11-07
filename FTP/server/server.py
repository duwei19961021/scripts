<<<<<<< HEAD
# -*- coding: utf-8 -*-
import  socket
import struct
=======
import  socket
import  os
>>>>>>> origin/master
server = socket.socket()
server.bind(("127.0.0.1",80))
server.listen(5)
while True:
    conn,addr = server.accept()
    file_info = eval(conn.recv(1024).decode("utf-8"))
    # {'action': 'put', 'filename': 'pod.png', 'filesize': 25032}
    if file_info["action"] == 'put':
        filenname = file_info["filename"]
        filesize = file_info["filesize"]
        reve_data = b''
        reve_datesize = 0
        while reve_datesize < filesize:
            data = conn.recv(1024)
            reve_data += data
            reve_datesize += len(data)
            with open(filenname,"wb") as f:
                f.write(reve_data)
            if reve_datesize == filesize:
                conn.send(b"exit")
            f.close()
    elif file_info["action"] == 'get':
        filesize = str(os.path.getsize(file_info["filename"])).encode("utf-8")
        print(filesize,type(filesize))
        conn.send(filesize)
        data = conn.recv(1024).decode("utf-8")
        if data == 'ok':
            with open(file_info["filename"],"rb") as f:
                for line in f:
                    conn.send(line)
            single = conn.recv(1024)
            if single == b'exit':
                break



