# simple script to enumerate UPNP devices
 
import socket

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# M-Search message body
MS = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:239.255.255.250:1900\r\n' \
    'ST:upnp:rootdevice\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n' \
    '\r\n'
 
# Set up a UDP socket for multicast
SOC = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
SOC.settimeout(2)
 
# Send M-Search message to multicast address for UPNP
SOC.sendto(MS.encode('utf-8'), ('239.255.255.250', 1900) )
 
#listen and capture returned responses
try:
    while True:
        data, addr = SOC.recvfrom(8192)
        print (bcolors.OKGREEN + "FROM: ", bcolors.UNDERLINE + addr[0] + bcolors.ENDC + " P:" + str(addr[1]), "\n\n",data.decode("utf-8"), "\n")
except socket.timeout:
        pass
