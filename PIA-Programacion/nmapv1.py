import nmap
#148.234.5.206
nm=nmap.PortScanner()

ip=input("Ingrese la direccion ip que desea escanear: ")
nm.scan(hosts=ip, arguments="--top-ports 1000 -sV --version-intensity 3")
print("Comando ejecutado: {}".format(nm.command_line()))

print("Protocolos utilizados:{}".format(nm[ip].all_protocols()))
print("Estado de la maquina: {}".format(nm[ip].state()))


for puerto in nm[ip]['tcp'].keys():
    for data in nm[ip]['tcp'][puerto]:
        print(data +" : " + nm[ip]['tcp'][puerto][data])