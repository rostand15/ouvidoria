from operacoesbd1 import *

def listar(conn):
    consultaListagemManifestacao = 'select * from manifestacao'
    manifestaçoes = listarBancoDados(conn,consultaListagemManifestacao)

    if len(manifestaçoes) == 0:
            print("nenhuma manifestação adicionada!")
    else:
        for item in manifestaçoes:
            print(f"Manifestação:{item[1]} do autor {item[2]}")

def adicionar (conn):
     while True:
        while True:
            indice = input("\n1)Reclamação \n2)Elogio \n3)Sugestão \nEscolha o tipo da manifestação: ")
            tipoManifestacao = ""
            if indice == "1":
                print("Você escolheu reclamação!")
                tipoManifestacao == "Reclamação"
                break

            elif indice == "2":
                print("Você escolheu elogio!")
                tipoManifestacao == "Elogio"
                break
            
            elif indice == "3":
                print("Você escolheu sugestão!")
                tipoManifestacao == "Sugestão"
                break
            else:
                print("Digite novamente")
             

        novaManifestacao = input("Digite a nova manifestação que deseja adicionar: ")
        if len(novaManifestacao) ==0:
            print("ERRO!, digite novamente a manifestação desejada: ")
        else:
            print("Manifestação cadastrada com sucesso!")
            break
        consultaInsert = "insert into manifestacao(descrição, tipo) values(%s,%s)"

        dados = [novaManifestacao , indice] 

        insertNoBancoDados(conn,consultaInsert,dados)
        print("Manifestação cadastrada com sucesso!")
                      
                