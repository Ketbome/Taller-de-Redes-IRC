def chat(packet):
    try:
       req = packet['IRC']['request'].split(" ")
       if(req[0]=='PRIVMSG'):
           print (packet["IRC"]["request"])
           packet["IRC"]["request"] = packet['IRC']['request'].replace(":hola",":chao")
           print (packet["IRC"]["request"])
       return packet
    except:
        print ("error")
        return packet
