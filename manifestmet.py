from operacoesbd1 import *

conn = criarConexao('localhost','root','linguicaqueimada','ouvidoria')


def listar(conn):
    consultaListagemManifestacoes = 'select * from manifestacao'
    manifestacoes = listarBancoDados(conn,consultaListagemManifestacoes)

    if len(manifestacoes)==0:
        print("Nenhuma manifestação adicionada!")
    else:
        for item in manifestacoes:
            print(f"Manifestação: {item[3]} | Autor: {item[1]} | Tipo: {item[4]}")

def escolherTipo():
    while True:
        tipos = ["reclamação","elogio","sugestão"]
        print('TIPOS DE MANIFESTACAO')
        for index, tipo in enumerate(tipos):
                print(f'{index+1}) {tipo}')
        tipo = int(input("Digite o número do tipo da manifestação: "))

        if tipo ==1:
            return tipos[0]
        elif tipo ==2:
            return tipos[1]
        elif tipo ==3:
            return tipos[2]
        else:
            print("Opção inválida. Escolha um número entre 1 e 3.")
     

def adicionar(conn):
    while True:
        nomeAutor = input("Digite o seu nome: ")
        tipoFuncao = escolherTipo()
        descricao = input("Digite a manifestação que deseja adicionar: ")

        if len(descricao) ==0:
                print("ERRO!, digite novamente a manifestação desejada: ")
        
        elif len(nomeAutor) ==0:
             print("ERRO! Digite novamente o seu nome!")
        else:
             print("Manifestação adicionada com sucesso!")
             break
        

    consultaInsert = "insert into manifestacao(autor,descricao,tipo) values(%s,%s,%s)"

    dados = [ nomeAutor, descricao, tipoFuncao ] 

    insertNoBancoDados(conn,consultaInsert,dados)

def quantidade(conn):
    consultaListagemManifestacoes = 'select count(*) from manifestacao'
    resultado = listarBancoDados(conn,consultaListagemManifestacoes)
    quantidadeManifestacao = resultado[0][0]
    print("Temos",quantidadeManifestacao,"Manifestações")

def listarportipo (conn):
     while True:
        consultaListagemManifestacoes = 'select * from manifestacao'
        manifestacoes = listarBancoDados(conn,consultaListagemManifestacoes)
        consultaListagemReclamacao = "select * from manifestacao where tipo = 'reclamação'"
        consultaListagemElogio = "select * from manifestacao where tipo = 'elogio'"
        consultaListagemSugestao = "select * from manifestacao where tipo = 'sugestão'"

        listarTipo = int(input("Escolha o tipo da manifestação que deseja listar: 1)Reclamação 2)Elogio 3)Sugestão. "))

        if listarTipo == 1:
            reclamacoes = listarBancoDados(conn,consultaListagemReclamacao)
            for item in reclamacoes:
                print(f"Manifestação: {item[3]} | Autor: {item[1]} | Tipo: {item[4]}")
            if len(manifestacoes) ==0:
                print("Não existem reclamações adicionadas!")
            break

        elif listarTipo == 2:
            elogios = listarBancoDados(conn,consultaListagemElogio)
            for item in elogios:
                print(f"Manifestação: {item[3]} | Autor: {item[1]} | Tipo: {item[4]}")
            if len(manifestacoes) ==0:
                print("Não existem elogios adicionados!")
        
            break

        elif listarTipo == 3:
            sugestoes = listarBancoDados(conn,consultaListagemSugestao)
            for item in sugestoes:
                print(f"Manifestação: {item[3]} | Autor: {item[1]} | Tipo: {item[4]}")
            if len(manifestacoes) ==0:
                print("Não existem sugestões adicionadas!")
            break
            
        else:
            print("Erro!, digite um número entre 1 e 3")

def buscarCodigo(conn):
    codigoManifestacao = int(input("Digite o código: "))
    consultaPesquisaManifestacao = 'select * from manifestacao where codigo = %s'
    dados = [ codigoManifestacao ]

    manifestacao = listarBancoDados(conn,consultaPesquisaManifestacao,dados)

    if len(manifestacao) == 0:
        print("Não existem manifestações a serem exibidas")
    else:
        print("Manifestação encontrada: descrição:", manifestacao[0][3], "autor:", manifestacao[0][1], "tipo:", manifestacao[0][4])
    
def removerManifestacao(conn):
    codigoManifestacao = int(input("Digite o código da Manifestação que deseja remover: "))

    consultaRemover = "delete from manifestacao where codigo = %s"
    dados = [ codigoManifestacao ]

    linhasAlteradas = excluirBancoDados(conn,consultaRemover,dados)

    if linhasAlteradas == 0:
        print("Não existe manifestação para o código informado")
    else:
        print("Manifestação removida com sucesso!")
