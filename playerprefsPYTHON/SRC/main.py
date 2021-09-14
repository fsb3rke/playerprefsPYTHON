import playerprefsLib
deneme = "berke deneme"
playerprefsLib.playerprefs("berke").savestring(deneme)
print(playerprefsLib.playerprefs("berke").getstring())
asd = 15
playerprefsLib.playerprefs("ali").saveint(asd)
print(playerprefsLib.playerprefs("ali").getint())
abo:int = playerprefsLib.playerprefs("ali").getint()
print(abo)
