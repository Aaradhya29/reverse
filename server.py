import socket 
import sys




def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s=socket.socket()

    except socket.error as msg:
        print('Socket creation error:'+ str (msg))

#binding socket and listening connection
#         

def bind_socket():
    try:
        global host
        global port
        global s             
        
        print("bind creation error:"+ str (port))
        s.bind(host,port)
        s.listen(5)

    except socket.error as msg:
        print('Socket creation error:'+ str (msg)+"\n"+ "Retrying..")
        bind_socket()