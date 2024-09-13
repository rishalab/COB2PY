from collections import defaultdict

class FileWriter:

    def __init__(self):
        self.CurrentFile = 'converted'
        self.indentation = 0
        pass

    def writeHeader(self):
        with open(self.CurrentFile+".py", "w") as file:
            sentences = ["from Program import Program\n\n\n",f"class {self.CurrentFile}(Program):\n","\n"]
            for s in sentences:
                file.write(s)
    
    def constructor(self,addressMap):
        self.indentation=1
        element=max(addressMap,key=lambda element:(element[2],element[3]))
        variable,dataName,offset,totalLength,length,pic=element
        with open(self.CurrentFile+".py", "a+") as file:
            file.write(('\t' * self.indentation) +"def __init__(self):\n")
            file.write(('\t' * (self.indentation+1)) +f"super().__init__({offset+totalLength})"+"\n")
            file.write("\n")
    
    def intializer(self,variableMap):
        self.indentation=1
        with open(self.CurrentFile+".py", "a+") as file:
            file.write(('\t' * self.indentation) +"def initialize(self):\n")
            self.indentation+=1
            for variable,Name in variableMap:
                if len(variable.children)==0:
                    if variable.value is not None:
                        
                        parentOccurs = []
                        for parent in variable.parents:
                            if parent.occurs > 1:
                                parentOccurs.append(parent.occurs)
                        if (variable.occurs!=1):
                            parentOccurs.append(variable.occurs)
                        if len(parentOccurs)!=0:
                            le = len(parentOccurs)
                            indexes=''
                            for i in range(le):
                                file.write(('\t' * self.indentation) +f"for idx{i+1} in range(0,{parentOccurs[i]}):\n")
                                indexes+=("idx"+str(i+1)+',')
                                self.indentation+=1
                            if variable.picInfo[-1]=='decimal' :
                                file.write(('\t' * self.indentation) +f'self.set{Name}({indexes}{float(variable.value)},False)'+'\n')
                            elif variable.picInfo[-1]=='integer' :
                                file.write(('\t' * self.indentation) +f'self.set{Name}({indexes}{int(variable.value)},False)'+'\n')
                            elif variable.picInfo[-1]=="alphaNumericEdited":
                                file.write(('\t' * self.indentation) +f'self.set{Name}({indexes}{variable.value})'+'\n')
                            self.indentation-=le
                        else:
                            print(variable,Name,variable.picInfo,"intializer")
                            if variable.picInfo[-1]=='decimal' :
                                file.write(('\t' * self.indentation) +f'self.set{Name}({float(variable.value)},False)'+'\n')
                                print(('\t' * self.indentation) +f'self.set{Name}({float(variable.value)},False)'+'\n')
                            elif variable.picInfo[-1]=='integer' :
                                file.write(('\t' * self.indentation) +f'self.set{Name}({int(variable.value)},False)'+'\n')
                                print(('\t' * self.indentation) +f'self.set{Name}({int(variable.value)},False)'+'\n')
                            elif variable.picInfo[-1]=="alphaNumericEdited":
                                file.write(('\t' * self.indentation) +f'self.set{Name}({variable.value})'+'\n')
            file.write(('\t' * self.indentation) +"pass\n")
            self.indentation-=1


                            
    

                        

            
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
            if (variable.occurs!=1):
                parentOccurs.append(variable.length)
            with open(self.CurrentFile+".py", "a+") as file:
                offset = str(offset)
                indexes = ''
                for i in range(0,len(parentOccurs)):
                    offset+=("+ idx"+str(i+1)+f"*{str(parentOccurs[i])}")
                    indexes+=(",idx"+str(i+1))
                if pic[1] == "decimal":
                    file.write(('\t' * self.indentation) + f"def get{dataName}(self{indexes}):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().getAsFloat({offset}, {length})" + '\n')
                    file.write('\n')
                    file.write(('\t' * self.indentation) + f"def set{dataName}(self{indexes}, value, isRounded):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().setAsFloat({offset}, {length}, value, isRounded, '{pic[0][0]}')" + '\n')
                    file.write('\n')

                if pic[1] == "integer":
                    file.write(('\t' * self.indentation) + f"def get{dataName}(self{indexes}):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().getAsInt({offset}, {length})" + '\n')
                    file.write('\n')
                    file.write(('\t' * self.indentation) + f"def set{dataName}(self{indexes}, value, isRounded):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().setAsInt({offset}, {length}, value, isRounded)" + '\n')
                    file.write('\n')

                if pic[1] == "alphaNumericEdited" or pic == '':
                    file.write(('\t' * self.indentation) + f"def get{dataName}(self{indexes}):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().getAsString({offset}, {length})" + '\n')
                    file.write('\n')
                    file.write(('\t' * self.indentation) + f"def set{dataName}(self{indexes}, value):" + '\n')
                    file.write(('\t' * (self.indentation + 1)) + f"return super().setAsString({offset}, {length}, value)" + '\n')
                    file.write('\n')


        return variableToName
