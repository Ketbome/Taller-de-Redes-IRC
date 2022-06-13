def nick(packet):
    try:
        req = packet['IRC']['request'].split(" ")
        if (req[0] == 'NICK'):
            packet['IRC']['request'] = "NICK nont"
            print (packet['IRC']['request'])
        return packet
    except:
        print ("except")
        return packet
