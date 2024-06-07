class SymbolTable:
    def __init__(self):
        self.table={}
    def add(self,name,attributes):
        self.table[name]=attributes
    def get(self,name,attributes):
        return self.table.get(name,None)
    def stringify(self):
        result = "Symbol Table:\n"
        for name, attributes in self.table.items():
            result += f"{name}: {attributes}\n"
        return result

    def __repr__(self):
        return self.stringify()