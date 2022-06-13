def sala(packet):
     try:
        req = packet['IRC']['request'].split(" ")[0]
        if (req == "JOIN"):
           packet["IRC"]["request"] = packet["IRC"]["request"].replace("chat","nada")
        return packet
     except:
        print ("except")
        return packet
