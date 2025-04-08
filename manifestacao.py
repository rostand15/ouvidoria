from manifestmet import *
from operacoesbd1 import *

manifestacao = []

conn = criarConexao('localhost','root','linguicaqueimada','ouvidoria')
consultaListagemManifestacoes = 'select * from manifestacao'

manifest = listarBancoDados(conn,consultaListagemManifestacoes)

print("Bem-vindo(a) à ouvidoria da Universidade XYZ!")

while True:
    print("\nOpções: \n1) Lista de manifestações " \
    "\n2) Listagem de manifestações por tipo " \
    "\n3) Criar uma nova manifestação " \
    "\n4) Exibir quantidade de manifestações " \
    "\n5) Pesquisar uma manifestação por código " \
    "\n6) Excluir uma manifestação pelo Código " \
    "\n7) Sair do sistema\n")
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
        print("Saindo do sistema, agradecemos o acesso!")
        break

    else:
        print("Opção inválida")