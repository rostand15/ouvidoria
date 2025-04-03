from manifestmet import*
from operacoesbd1 import*

manifestacao = []

conn = criarConexao('localhost','root','linguicaqueimada','ouvidora')
consultaListagemManifestacao = 'select * from manifestacao'

while True:
    print("\nOpções: \n1)Lista de manifestções \n2)Adicionar manifestações \n3)Exibir quantidade de manifestações \n4)Pesquisar manifestação com codigo \n5)Sair do sistema \n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        listar(conn)
    
    elif opcao==2:
        adicionar(conn)
    
    elif opcao==3:
        if len(manifestacoes)>0:
            print("A quantidade de manifestações na lista é de:", len(manifestacoes),"manifestações")
        else:
            print("Ainda não há manifestações na lista!")

    elif opcao ==4:
        pos = int(input("Digite o código da manifestação: "))
        indice = pos-1

        if indice >= 0 and indice < len(manifestacoes):
            print("Manifestação:", manifestacoes[indice])
        else:
            print("Código inválido.")
    
    elif opcao ==5:
        print("Sistema encerrado, agradecemos o acesso!.")
        break
    
    else:
        print("Opção inválida")