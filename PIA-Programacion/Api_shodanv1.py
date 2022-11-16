from shodan import Shodan

api = Shodan('hSgHyoWTPKKxZsNHgEEM4mHGG2joLXIV')


direccion_ip = input("Inngrese la direccion IP: ")
host=api.host(direccion_ip)

file=open('BusquedaShodan.txt', 'a+', encoding="utf-8")

file.write("Informacion general")
file.write('''
    Direccion: {}
    Hostname: {}
    Dominio: {}
    Pais: {}
    Ciudad: {}
    Organizacion: {}
    ISP: {}
    ASN: {}
    Puertos abiertos: {}
    '''.format(host['ip_str'],host['hostnames'],host['domains'],host['country_name'],host['city'],host['org'],host['isp'],host['asn'],host['ports']))

file.close()

print("Archivo txt guardado con exito")