dic={"nome":"Edna","ultimonome":"Feliz","idade":"20","curso":"direito","endereco":"Rua Lopes Souza N 2"}
print(dic.items()) #Resposta A
print(dic["nome"]) #Resposta B
print(dic["ultimonome"]) #Resposta B
print(dic["idade"]) #Resposta B
print(dic["curso"]) #Resposta B
print(dic["endereco"]) #Resposta B
del dic["curso"] #Resposta C
dic["ultimonome"] = "Lopes" #Resposta D
print(dic.items()) #Resposta E
print(dic["endereco"]) #Resposta F
dic2 = dic.copy() #Resposta G
dic2["nome"] = "Olivia" #Resposta G
dic2["idade"] = "17" #Resposta G
print(dic2.items()) #Resposta H