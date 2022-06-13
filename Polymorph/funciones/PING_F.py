def ping(packet):
     try:
         req = packet['IRC']['request'].split(" ")
         if (req[0] == "PING"):
            packet["IRC"]["request"] = "PING 1"
         return packet     
     except:
        print ("error")
        return packet
