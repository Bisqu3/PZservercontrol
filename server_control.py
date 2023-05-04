from rcon.source import Client
import config
ip = config.ip
port = config.port
pas = config.password

def run(string):
    with Client(ip, port, passwd=pas) as client:
        print("Connected to client")
        response = client.run(string)
    return response


def manager():
    print("RCON SERVER MANAGER")
    while True:
        x = input(">> ")
        try: 
            print(run(x))
        except:
            print("Error")



manager()