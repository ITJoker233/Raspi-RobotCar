import os
def LoadData(filename):
    port=[]
    mypath=os.path.dirname(os.path.realpath(__file__))
    file=open(mypath+'/'+filename)
    for line in file.readlines():
        lineArr = line.strip().split('=')# Nomal is Space
        port.append(int(lineArr[1]))
    return port[0]
