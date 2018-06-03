import socket
def gethosrname():
    hostname = socket.gethostname()
    return hostname
def getip():
    hostname = socket.gethostname()
    ip=socket.gethostbyname(hostname)
    return ip
