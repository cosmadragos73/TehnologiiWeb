#! python
############
#Imports  #
############
from socket import * 
from functii_server import *

############
#Variabiles#
############

#Constant Variabiles
HOST = '' #Noi suntem Hostul
PORT = 80 #Un port arbitrar, portul default http e 80
ADDR = (HOST,PORT) #Adresa in sine vine ca si o combinatie de host:port
BUFFSIZE = 4096 #Dimensiunea buferului trebuie sa fie rezonabila
server = socket(AF_INET, SOCK_STREAM)


############
#Functions#
############

#Main
def main():
    #Acum creeam un nou obiect socket (server)

    #Legam socketul de conexinuea noastra
    server.bind((ADDR)) #parantezele duble creeaza tuple-ul necesar dintr-un element
    server.listen(5) #5 este numarul maxim de conexinui pe care-l acceptam'
    print ('Accept conexiuni pe portul: ' + str(PORT))

    while 1:

            conn,addr = server.accept() #acceptam conexiunea
            print('Conexiune noua: ', addr)
            request = conn.recv(BUFFSIZE) #primeste reuqestul
            print('Am primit un request ', request)
            conn.sendall(parseRequest(request)) #trimitem raspuns
            print('Am trimis raspuns')
            conn.close()
            print("Am inchis conexiunea")

try :
    main()
finally:
    server.close()