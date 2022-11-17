import nmap
import csv
#148.234.5.206
target = input('Ingresa la direccion IP que desea escanear: ')

print('Escaneando:')

scanner = nmap.PortScanner()
sc = scanner.scan(hosts=target, arguments='--open')
hosts_list = [(x, sc['scan'][x]['hostnames'][0]['name'], list(sc['scan'][x]['tcp'].keys())) for x in scanner.all_hosts()]

for item in hosts_list:
    with open('scanHosts1.1.csv', 'a', newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(item)

print('Listo! \n')
