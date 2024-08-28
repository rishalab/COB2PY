from collections import defaultdict


class FileWriter:

    def __init__(self):
        self.CurrentFile = ''
        self.indentation = 0
        pass

    def writeHeader(self):
        with open(self.Currentfile+".py", "w") as file:
            sentences = ["import Program from Program\n",f"class {self.CurrentFile}(Program):\n"]
            for s in sentences:
                file.write(s)
            
    def writeGetterAndSetter(self,addressMap):
        self.indentation=1
        variableToName=[]
        nameMap = defaultdict(int)
        for element in addressMap:
            variable,dataName,offset,totalLength,length,pic=element
            variableCount = nameMap.get(dataName)
            hashval = ''
            if variableCount is not None:
                hashval = str(variableCount)
                nameMap[dataName]+=1
                dataName+=("_"+hashval)
            else:
                nameMap[dataName]+=1
            variableToName.append([variable,dataName])
            parentOccurs = []
            for parent in variable.parents:
                if parent.occurs > 1:
                    parentOccurs.append(parent.length)
            with open(self.Currentfile+".py", "a+") as file:
                offset = str(offset)
                for i in range(0,len(parentOccurs)):
                    offset+=("+ idx"+str(i+1)+f"*{str(parentOccurs[i])}")
                if pic[1]=="decimal":
                    file.write(f"{'\t'*self.indentation}def get{dataName}(self):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().getAsFloat({offset},{length})\n")
                    file.write("\n")
                    file.write(f"{'\t'*self.indentation}def set{dataName}(self,value,isRounded):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().setAsFloat({offset},{length},value,isRounded,'{pic[0][0]}')\n")
                    file.write("\n")
                if pic[1]=="integer":
                    file.write(f"{'\t'*self.indentation}def get{dataName}(self):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().getAsInt({offset},{length})\n")
                    file.write("\n")
                    file.write(f"{'\t'*self.indentation}def set{dataName}(self,value,isRounded):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().setAsInt({offset},{length},value,isRounded)\n")
                    file.write("\n")
                if pic[1]=="alphaNumericEdited" or pic =='':
                    file.write(f"{'\t'*self.indentation}def get{dataName}(self):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().getAsString({offset},{length})\n")
                    file.write("\n")
                    file.write(f"{'\t'*self.indentation}def set{dataName}(self,value):\n")
                    file.write(f"{'\t'*(self.indentation+1)}return super().setAsString({offset},{length},value)\n")
                    file.write("\n")
        
        return variableToName



            


        