from manifestmet import *
from operacoesbd1 import *

manifestacao = []

conn = criarConexao('localhost','root','linguicaqueimada','ouvidoria')
consultaListagemManifestacoes = 'select * from manifestacao'

manifest = listarBancoDados(conn,consultaListagemManifestacoes)

while True:
    print("\nOpções: \n1)Lista de manifestações " \
    "\n2)Listagem de Manifestações por Tipo " \
    "\n3)Criar uma nova Manifestação " \
    "\n4)Exibir quantidade de manifestações " \
    "\n5)Pesquisar uma manifestação por código " \
    "\n6) Excluir uma Manifestação pelo Código " \
    "\n7) Sair do Sistema.")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        listar(conn)

    elif opcao == 2:
        listarportipo(conn)
        
    elif opcao == 3:
       adicionar(conn)

    elif opcao == 4:
       quantidade(conn)
    
    elif opcao == 5:
        buscarCodigo(conn)
    
    elif opcao ==6:
        removerManifestacao(conn)
        
    elif opcao == 7:
        print("Saindo do sistema, agradecemos pelo acesso!")
        break
    
    else:
        print("Opção inválida")
        