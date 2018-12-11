#!python

import os.path

status_codes ={
    200 : 'OK',
    201 : 'Created',
    202 : 'Accepted',
    301 : 'Moved permanently',
    302 : 'Moved temporarily',
    400 : 'Bad request',
    401 : 'Unauthorised',
    404 : 'Not found',
    405 : 'Method not allowed',
    500 : 'Internal Server error',
    501 : 'Not implemented'
}

ROOT_PATH = "/tmp/"
DEFAULT_OPEN_MODE = 'r'
SUCCES_HEADER = 'HTTP/1.1 200 OK\n'
FILE_NOT_FOUND_HEADER ='HTTP/1.0 404 Not Found\n'
FILE_NOT_FOUND_PATH = '404.html'

def parseRequest(request):
    requestArray = request.split()
    if (requestArray[0]== 'GET'):
        return fetchFile(requestArray[1].lstrip('/'))

def fetchFile(path):
    if (os.path.exists(ROOT_PATH + path)) :
        with open(ROOT_PATH + path, DEFAULT_OPEN_MODE) as f:
            return SUCCES_HEADER + f.read()
    else:
        return fileNotFound()

def fileNotFound():
    with open(FILE_NOT_FOUND_PATH, DEFAULT_OPEN_MODE) as f:
        return FILE_NOT_FOUND_HEADER + f.read()