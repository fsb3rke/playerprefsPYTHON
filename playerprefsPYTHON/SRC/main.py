import playerprefsLib
deneme = "berke deneme"
playerprefsLib.playerprefs("berke").savestring(deneme)
print(playerprefsLib.playerprefs("berke").getstring())
asd = 15
playerprefsLib.playerprefs("ali").saveint(asd)
print(playerprefsLib.playerprefs("ali").getint())
abo:int = playerprefsLib.playerprefs("ali").getint()
print(abo)
bs = True
ba = False
playerprefsLib.playerprefs("bsa").savebool(bs)
playerprefsLib.playerprefs("bas").savebool(ba)
print(playerprefsLib.playerprefs("bsa").getbool())
print(playerprefsLib.playerprefs("bas").getbool())
bumba:bool = playerprefsLib.playerprefs("bsa").getbool()
abmub:bool = playerprefsLib.playerprefs("bas").getbool()
print(bumba)
print(abmub)
playerprefsLib.playerprefs("hobsa").savefloat(0.02)
bsasz:float = playerprefsLib.playerprefs("hobsa").getfloat()
print(bsasz)
