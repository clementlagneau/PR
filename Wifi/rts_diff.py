from scapy.all import *

#Def de l'interface
face = ''

#Conf pour monitor en meme temps
conf.use_pcap = True
monitor = True

def ktos(k):
    tmp = hex(k)[2:].zfill(12)
    out = str(tmp[0:2])+":"+str(tmp[2:4])+":"+str(tmp[4:6])+":"+str(tmp[6:8])+":"+str(tmp[8:10])+":"+str(tmp[10:12])
    return(out)

l = []
#On l'envoie
for k in range(200):
    l.append(RadioTap()/Dot11(type=1, subtype = 11,
                #ID = 0700,
                addr1 = '',
                addr2 = ktos(k)))
for k in l:
    sendp(k, iface= face,monitor = True)

