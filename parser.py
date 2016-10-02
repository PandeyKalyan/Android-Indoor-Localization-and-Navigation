import random
import wknn

mac_address = ['ac:72:89:83:48:7a', 'd4:ca:6d:8c:4b:97', '00:26:66:86:27:d0',
               'd4:ca:6d:8d:4b:bb', '00:0c:42:c8:5f:22', '34:a8:4e:4e:a6:10',
               '00:14:d1:23:da:b3']

def rssiParse(strengthList):
    mac_rssi = dict()
    data_to_babu = list()
    strength = strengthList.split(',')
    for i in range(len(strength)):
        needed_strength = strength[i][-21:].split(' ')
        mac_rssi[needed_strength[0]] = needed_strength[1]

    for i in range(len(mac_address)):
        try:
            data_to_babu.append(int(mac_rssi[mac_address[i]]))
        except:
            data_to_babu.append(-90)
    wknn.initialCor(data_to_babu)

def firstParser(socketOutput):
    strengthAngleSteps = socketOutput.split("]")
    strengthList = strengthAngleSteps[0][1:]
    strength = rssiParse(strengthList)
    angleSteps = strengthAngleSteps[1].split(" ")
    angle = angleSteps[0]
    steps = angleSteps[1][:-1]
    return strength, angle, steps
    
