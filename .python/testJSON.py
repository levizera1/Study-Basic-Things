import json

def escrever_json(dados):
    with open("meu_arquivo_teste", "w", encoding = "utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Coloque seu sobrenome: ")
ultimo_nome = input("Coloque seu ultimo nome: ")

nome_completo = nome + sobrenome + ultimo_nome

escrever_json(nome_completo)



#def escrever_json(dados):
#    with open("meu_arquivo_teste", "w", encoding = "utf-8") as f:
#        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

#meuDic = input("Coloque seu nome: ")
#escrever_json(meuDic)
