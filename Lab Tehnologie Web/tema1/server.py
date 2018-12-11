import socket, select

class Server(object):
    #Avem nevoie de o lista cu descrierile socketuri-lor
    LISTA_CONEXIUNI = []
    RECVIE_BUFFER = 4096
    PORT = 5000

    def __init__(self):
        self.nume_utilizatori = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.seteaza_connexiuni()
        self.conectare_client()

    def seteaza_connexiuni(self):
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", self.PORT))
        self.server_socket.listen(5) #numarul maxim de conexiune simultane

        #Adaugam socketul serverului la lista cu conexiuni ok
        self.LISTA_CONEXIUNI.append(self.server_socket)
    #Functie care trimite mesajele catre toti clientii conectati
    def broadcast_data(self, sock, message):
        #Nu trimite mesajulu catre socketul master si catre clientul care a trimis mesajul catre server
        for socket in self.LISTA_CONEXIUNI:
            if socket != self.server_socket and socket != sock:
                #
                try:
                    socket.send(message)
                #Aici ar trebui tratate toate exceptiile care pot aparea atunci cand o conexiune prin socket nu este buna:
                #de exemplu: intrerupere prin ctrl+c
                except KeyboardInterrupt as error:
                    socket.close()
                    self.LISTA_CONEXIUNI.remove(socket)
                except:
                    socket.close()
                    self.LISTA_CONEXIUNI.remove(socket)

    def trimite_date_catre(self, sock, message):
        try:
            sock.send(message)
        except:
            #din nou tratate exceptiile care pot aparea intre conexiuni
            sock.close()
            if sock in self.LISTA_CONEXIUNI:
                self.LISTA_CONEXIUNI.remove(sock)
            else:
                pass
            


    def conectare_client(self):
        print("Serverul e pornit pe portul " + str(self.PORT))
        while 1:
            #Luam lista cu socketurile care pot fii citiate
            citeste_socketuri, scrie_socketuri, erori_socketuri = select.select(self.LISTA_CONEXIUNI, [], [])

            for sock in citeste_socketuri:
                #O noua conexiune
                if sock == self.server_socket:
                    #Rezolva cazul in care exista o noua conexiune primita prin socketul serverului
                    self.seteaza_conexiune()
                #Asteptam mesaj de la client?
                else:
                    #Primim date de la client, le procesam
                    try:
                        data = sock.recv(self.RECVIVE_BUFFER)
                        if data:
                            if self.nume_utilizator[sock].utilizator is None:
                                self.seteaza_nume_utilizator(data, sock)
                            else:
                                self.broadcast_data(sock, "\r" + '<' +self.nume_utilizator[sock].utilizator + '> ' + data)
                    except:
                        self.broadcast_data(sock, "Clientul (%s, %s) este offline" % addr)
                        print( "Clientul (%s, %s) este offline" % addr)
                        sock.close()
                        self.LISTA_CONEXIUNI.remove(sock)
                        continue
        self.server_socket.close()

    def seteaza_nume_utilizator(self, data, sock):
        self.nume_utilizator[sock].utilizator = data.strip()
        self.trimite_date_catre(sock, data.strip() + ', acum esti conectat\n')
        self.trimite_date_catre_clienti_inregistrati(sock, data.strip() + ', conexiune noua\n')

    def seteaza_conexiune(self):
        sockd, addr = self.server_socket.accept()
        self.LISTA_CONEXIUNI.append(socket)
        print("Clientul (%s, %s) conectat" %addr)
        self.trimite_date_catre(sockd, "Introdu numele tau: ")
        self.nume_utilizatori.update({sockd: Connection(addr)})
    
    def trimite_date_catre_clienti_inregistrati(self, sock, message):
        for local_soc, connection in self.nume_utilizatori.iteritems():
            if local_soc != sock and connextion.utilizator is not None:
                self.trimite_date_catre(local_soc, message)

class Connection (object):
    def __init__(self, addres):
        self.addres = addres
        self.utilizator = None

if __name__ == "__main__":
    server = Server()
