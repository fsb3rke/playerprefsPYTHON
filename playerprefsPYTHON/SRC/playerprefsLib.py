import json
class playerprefs:
    def __init__(self, code):
        self.code = code
    def saveint(self, intvalue:int):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        text = f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {intvalue}
        {hobas}
    ]
{hobas}
        """
        file.write(text)
        file.close()
    def getint(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = 0
        for name in data["playerprefs"]:
            a = name[self.code]
        return a

    def savefloat(self, floatvalue:float):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        text = f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {floatvalue}
        {hobas}
    ]
{hobas}
        """
        file.write(text)
        file.close()
    def getfloat(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = 0.0
        for name in data["playerprefs"]:
            a = name[self.code]
        return a


    def savestring(self, stringvalue:str):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        text = f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {bumba}{stringvalue}{bumba}
        {hobas}
    ]
{hobas}
        """
        file.write(text)
        file.close()
    def getstring(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = ""
        for name in data["playerprefs"]:
            a = name[self.code]
        return a

    def savebool(self, boolvalue:bool):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        def sucuk(bools:bool):
            if bools == True:
                return "True"
            else:
                return "False"
        text = f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {bumba}{sucuk(boolvalue)}{bumba}
        {hobas}
    ]
{hobas}
        """
        file.write(text)
        file.close()

    def getbool(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = ""
        for name in data["playerprefs"]:
            a = name[self.code]
        def sck(bas):
            if bas == "True":
                return True
            elif bas == "False":
                return False
        return sck(a)
