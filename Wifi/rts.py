from scapy.all import *

#Def de l'interface
face = ''

#Conf pour monitor en meme temps
conf.use_pcap = True
monitor = True

#Craft du paquet#
dot11 = Dot11(type=1, subtype = 11,
            #ID = 0700,
            addr1 = '',
            addr2 = '')

frame = RadioTap()/dot11

#On le voit tranquillement
frame.show()
print("Hexaframe")
hexdump(frame)
input("Press enter")

for x in range(1000):
    sendp(frame, iface= face,monitor=True,loop=True, inter = 0.001)

