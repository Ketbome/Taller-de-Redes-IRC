def join(packet):
     try:
         req = packet['IRC']['request'].split(" ")
         if (req[0] == "JOIN"):
            packet["IRC"]["request"] = packet["IRC"]["request"].replace("JOIN","PART")
         return packet
     except:
        print ("error")
        return packet
