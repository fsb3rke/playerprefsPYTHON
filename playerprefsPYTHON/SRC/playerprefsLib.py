import json
class playerprefs:
    def __init__(self, code):
        self.code = code
    def saveint(self, intvalue:int):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        file.write(f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {intvalue}
        {hobas}
    ]
{hobas}
        """)
        file.close()
    def getint(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = 0
        for name in data["playerprefs"]:
            a = name[self.code]
        return a

    def savestring(self, stringvalue:str):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        file.write(f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {bumba}{stringvalue}{bumba}
        {hobas}
    ]
{hobas}
        """)
        file.close()
    def getstring(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = ""
        for name in data["playerprefs"]:
            a = name[self.code]
        return a
