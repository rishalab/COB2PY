import math

class Program:

    def __init__(self,length):
        self.Memory = [""]*length

    def getAsString(self,offset,length):
        return ''.join(self.Memory[offset:offset+length])
    
    def getAsInt(self,offset,length):
        return int(''.join(self.Memory[offset:offset+length]))
    
    def getAsFloat(self,offset,length):
        return float(''.join(self.Memory[offset:offset+length]))
    
    def setAsInt(self,offset,length,value,isRounded):
        value = abs(round(value)) if isRounded else abs(int(value))
        dataLength = 1 if value==0 else math.floor(math.log10(value)) + 1
        if dataLength>length:
            value = str(value)[-length:]
            for i in range(0,length):
                self.Memory[offset+i]=value[i]
        else:
            value = str(value)
            for i in range(0,dataLength):
                self.Memory[offset+i]=value[i]
            for i in range(length,dataLength):
                self.Memory[offset+i]='0'
    
    def setAsString(self,offset,length,value):
        value=str(value)
        dataLength=len(value)
        if dataLength>length:
            value = str(value)[-length:]
            for i in range(0,length):
                self.Memory[offset+i]=value[i]
        else:
            for i in range(0,dataLength):
                self.Memory[offset+i]=value[i]
            for i in range(length,dataLength):
                self.Memory[offset+i]=' '
    
    def setAsFloat(self,offset,length,value,isRounded,pic):
        intPart,decPart= pic.split('.')
        intPartLen,decPartLen=len(intPart),len(decPart)
        value = abs(round(value,decPartLen)) if isRounded else abs(int(float(value)*(10**decPartLen))/(10**decPartLen))
        value = str(value)[-length-1:]
        intPart,decPart=value.split('.')
        intPart,decPart=intPart[-intPartLen:],decPart[:decPartLen]
        while(len(intPart)<intPartLen):
            intPart= '0'+intPart
        while(len(decPart)<decPartLen):
            decPart= decPart+'0'
        value= intPart+'.'+decPart
        for i in range(0,length):
                self.Memory[offset+i]=value[i]