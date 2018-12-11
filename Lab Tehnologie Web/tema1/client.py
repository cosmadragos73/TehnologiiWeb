import socket,select,sys
INPUT_ERROR_MESAJ = 'Apel incorect, te rog sa imi transmitia adresa serverului pe linia de comanda.\nExemplu: ./client.py <adresaIP> <port>'
def prompt():
    sys.stdout.write("> ")
    sys.stdout.flush()

class Client(object):

    def __init__(self):
        self.host = (sys.argv[1])
        self.port = int(sys.argv[2])
        self.sock = None
        self.seteaza_conexiune_server()

    def seteaza_conexiune_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
        # conectare la hostul remote
        try:
            self.sock.connect((self.host, self.port))
        except:
            print('EROARE:Nu ma pot conecta')
            sys.exit()

        print ("INFO: Conexiunea cu serverul remote a reusit.\n")
        print ("INFO: Poti trimite mesaje\n")
        prompt()
        self.asteapta_mesaje()

    def asteapta_mesaje(self):
        while 1:
            socket_list = [sys.stdin, self.sock]

            #Luam lista cu socketurile care pot fii citiate
            citeste_socketuri, scrie_socketuri, erori_socketuri = select.select(socket_list, [], [])

            for sock in citeste_socketuri:
                #mesaj care vine de la serverul remote
                if sock == self.sock:
                    data = sock.recv(4096)
                    if not data:
                        print("\nINFO:Deconectat de la server")
                        sys.exit()
                    else:
                        #printeaza datele
                        sys.stdout.write(data)
                        prompt()
                #utilizatorul a introdus un mesaj
                else:
                    msg = sys.stdin.readline()
                    self.sock.send(msg)
                    prompt()

if __name__ == '__main__':
    if len(sys.argv) < 2:   
        print(INPUT_ERROR_MESAJ)
    else:
        client = Client()


