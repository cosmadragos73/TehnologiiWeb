#! python

from socket import *
import sys

MESAJ_INTAMPINARE = 'Bun venit la acesta simpla aplicatie. Scrie url-ul sau path-ul pe care vrei sa il vizitezi si apasa enter. Ca sa iesi scrie /quit '

INPUT_ERROR_MESAJ = 'Apel incorect, te rog sa imi transmitia adresa serverului pe linia de comanda.\nExemplu: ./client.py <adresaIP>'

BROWSER_HEADER = '\n' + 50*'-' + '\n'

BROWSER_FOOTER = '\n' + 50*'-' + '\n'

if (len(sys.argv)<2):
	print (INPUT_ERROR_MESAJ)
	sys.exit()

HOST = sys.argv[1] #hostul este primul argument primit pe linia de comanda
PORT = 80    #portul nostru la care ne conectam
ADDR = (HOST,PORT)
BUFSIZE = 4096


def formRequest(path):
	return "GET /{} HTTP/1.1".format(path)  

def main():

	print (MESAJ_INTAMPINARE)
	path = raw_input()
	
	while (path != '/quit'):
		response, buff = '',''
		cli = socket( AF_INET,SOCK_STREAM)
		cli.connect((ADDR))
		request = path
		cli.sendall(formRequest(path)) #trimite un request catre server
		while 1:
			buff = cli.recv(BUFSIZE) #primim prima portiune din mesaj
			if not buff: break #daca portiunea curent este goala, aceasta este
			response = response + buff # o concatenam la raspuns
		print (BROWSER_HEADER + response + BROWSER_FOOTER)
		cli.close()
		path = raw_input()



main()


