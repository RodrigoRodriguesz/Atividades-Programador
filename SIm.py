dic= {"nome":"Guilherme","ultimonome":"Castilho","idade":"22","Jogador": "Ceará"}

print(dic.items()) 

print(dic["nome"]) 

print(dic["ultimonome"]) 

print(dic["idade"])

print(dic["Jogador"])

del dic ["Jogador"]


dic["ultimonome"] = "Rodrigues"

print(dic.items())

print(dic["idade"])

dic2 = dic.copy()

dic2["nome"] = "David" 

dic2["idade"] = "19"

print(dic2.items())
