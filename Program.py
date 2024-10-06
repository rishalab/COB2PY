import math

class Program:

    def __init__(self,length):
        self.Memory = [""]*length
        self.overpunch=[
            {
                '0': '{', '1': 'A', '2': 'B', '3': 'C', '4': 'D', 
                '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I'
            },
            {
                '0': '}', '1': 'J', '2': 'K', '3': 'L', '4': 'M', 
                '5': 'N', '6': 'O', '7': 'P', '8': 'Q', '9': 'R'
            }
        ]
        self.unpunch = {
            '{':['0','+'],'A':['1','+'],'B':['2','+'],'C':['3','+'],'D':['4','+'],'E':['5','+'],'F':['6','+'],'G':['7','+'],'H':['8','+'],'I':['9','+'],
            '}':['0','-'],'J':['1','-'],'K':['2','-'],'L':['3','-'],'M':['4','-'],'N':['5','-'],'O':['6','-'],'P':['7','-'],'Q':['8','-'],'R':['9','-']
        }

    def getAsString(self,offset,length):
        return ''.join(self.Memory[offset:offset+length])   
    
    def getAsInt(self,offset,length,isSigned,isSignSeparate,isSignLeading):
        value = ''.join(self.Memory[offset:offset+length])
        if not isSigned:
            return int(value)
        else:
            if isSignSeparate:
                value,sign=[value[1:],value[0]] if isSignLeading else [value[:-1],value[-1]]
                value = '-'+value if sign=='-' else value
                return int(value)
            else:
                value,sign=[self.unpunch[value[0]][0]+value[1:],self.unpunch[value[0]][1]] if isSignLeading else [value[:-1]+self.unpunch[value[-1]][0],self.unpunch[value[-1]][1]]
                value = '-'+value if sign=='-' else value
                return int(value)
    
    def getAsDisplayInt(self,offset,length,isSigned,isSignSeparate,isSignLeading):
        val = self.getAsInt(offset,length,isSigned,isSignSeparate,isSignLeading)
        valstr=''
        if isSigned:
            valstr = '+' if val >= 0 else '-'
        val2 = str(abs(val))
        zero= '0'*(length-len(val2))
        if isSignSeparate:
            zero = zero[:-1]
        return valstr+zero+val2
    
    def getAsFloat(self,offset,length,pic,isSigned,isSignSeparate,isSignLeading):
        intPart,decPart= pic.split('.')
        intPartLen,decPartLen=len(intPart),len(decPart)
        value = ''.join(self.Memory[offset:offset+length])
        if not isSigned:
            return float(int(value)/10** decPartLen)
        else:
            if isSignSeparate:
                value,sign=[value[1:],value[0]] if isSignLeading else [value[:-1],value[-1]]
                value = '-'+value if sign=='-' else value
                return float(int(value)/10** decPartLen)
            else:
                value,sign=[self.unpunch[value[0]][0]+value[1:],self.unpunch[value[0]][1]] if isSignLeading else [value[:-1]+self.unpunch[value[-1]][0],self.unpunch[value[-1]][1]]
                value = '-'+value if sign=='-' else value
                return float(int(value)/10** decPartLen)

    def getAsDisplayFloat(self,offset,length,pic,isSigned,isSignSeparate,isSignLeading):
        val = self.getAsFloat(offset,length,pic,isSigned,isSignSeparate,isSignLeading)
        valstr=''
        if isSigned:
            valstr = '+' if val >= 0 else '-'
        val2 = str(abs(val))
        intPart,decPart= pic.split('.')
        intPartLen,decPartLen=len(intPart),len(decPart)
        val2 = val2.split('.')
        leadZero,tailZero = '0'*(intPartLen-len(val2[0])),'0'*(decPartLen-len(val2[1]))
        if isSigned:
            leadZero=leadZero[:-1]
        return valstr+leadZero+val2+tailZero       

    
        
    
    def setAsInt(self,offset,length,value,isRounded,isSigned,isSignSeparate,isSignLeading):
        sign = '+' if value > 0 else '-'
        if isSigned:
            if isSignSeparate:
                value = abs(round(value)) if isRounded else abs(int(value))
                dataLength = 1 if value==0 else math.floor(math.log10(value)) + 1
                dataLength+=1
                if dataLength>length:
                    value = str(value)[-length+1:]
                    value = sign+value if isSignLeading else value+sign
                    for i in range(0,length):
                        self.Memory[offset+i]=value[i]
                else:
                    mu = length-dataLength-1 if length-dataLength-1>=0 else 0
                    value = ('0'*(mu))+str(value)[-length+1:]
                    value = sign+value if isSignLeading else value+sign
                    for i in range(0,length):
                        self.Memory[offset+i]=value[i]
            else:
                value = abs(round(value)) if isRounded else abs(int(value))
                dataLength = 1 if value==0 else math.floor(math.log10(value)) + 1
                ind = 0 if sign=='+' else 1
                if dataLength>length:
                    value = str(value)[-length:]
                    value = self.overpunch[ind][value[0]]+value[1:] if isSignLeading else value[:-1]+ self.overpunch[ind][value[-1]]
                    for i in range(0,length):
                        self.Memory[offset+i]=value[i]
                else:
                    mu = length-dataLength if length-dataLength>=0 else 0
                    value = ('0'*(mu))+str(value)[-length:]
                    value = self.overpunch[ind][value[0]]+value[1:] if isSignLeading else value[:-1]+ self.overpunch[ind][value[-1]]
                    for i in range(0,length):
                        self.Memory[offset+i]=value[i]
        else:
            value = abs(round(value)) if isRounded else abs(int(value))
            dataLength = 1 if value==0 else math.floor(math.log10(value)) + 1
            if dataLength>length:
                value = str(value)[-length:]
                for i in range(0,length):
                    self.Memory[offset+i]=value[i]
            else:
                value = str(value)
                for i in range(0,length-dataLength):
                    self.Memory[offset+i]='0'
                for i in range(length-dataLength,length):
                    self.Memory[offset+i]=value[i+dataLength-length]
    
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
    
    def setAsFloat(self,offset,length,value,isRounded,pic,isSigned,isSignSeparate,isSignLeading):
        if not isSigned:
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
            value= intPart+decPart
            for i in range(0,length):
                    self.Memory[offset+i]=value[i]
        else:
            sign = '+' if value >=0 else '-'
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
            if isSignSeparate:
                value= sign+intPart+decPart if isSignLeading else intPart+decPart+sign
                for i in range(0,length):
                    self.Memory[offset+i]=value[i]
            else:
                ind =  0 if sign=='+' else 1
                value= intPart+decPart
                value = self.overpunch[ind][value[0]]+value[1:] if isSignLeading else value[:-1]+ self.overpunch[ind][value[-1]]
                for i in range(0,length):
                    self.Memory[offset+i]=value[i]

