import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.dicionario import Dicionario
from models.produto import Produto

#Essa função é responsável por testar se a busca de produto está funcionando utilizando os parametros id ou nome
def testarBuscaProduto():
    print('Testando Busca do Produto')
    print(Dicionario.buscarProduto(id=49))
    print(Dicionario.buscarProduto(nome='Produto 48'))
    print('\n')

#Essa função é responsável por testar se a adição de produto está funcionando passando como parâmetro a instancia de um produto
def testarAdicionarProduto():
    print('Testando Adicionar Produto')
    Dicionario.adicionarProduto(Produto('Cibele', 10, 0.0, True))
    print(Dicionario.buscarProduto(id=50))
    print(Dicionario.buscarProduto(nome='Cibele'))
    print('\n')

#Essa função é responsável por testar se a atualização de produto está funcionando
# Para isso, é necessário passar os parâmetros id, que é obrigatório, quantidade ou preço

def testarAtualizarProduto():
    print('Testando Atualizar Produto')
    Dicionario.atualizarProduto(50, quantidade=0, preco=0)
    print(Dicionario.buscarProduto(50))
    Dicionario.atualizarProduto(50, quantidade=5)
    print(Dicionario.buscarProduto(50))
    Dicionario.atualizarProduto(50, preco=10)
    print(Dicionario.buscarProduto(50))

    print('\n')

#Essa função é responsável por testar se a remoção de produto está funcionando 
#Para isso é necessário passar como parâmetro o id
def testarRemoverProduto():
    print('Testando Remover Produto')
    Dicionario.removerProduto(50)
    print(Dicionario.buscarProduto(id=50))
    print(Dicionario.buscarProduto(nome='Cibele'))
    print('\n')

#Essa funcão é responsável por executar os testes 
def executarTestes():
    print('Inicializando Caso de Teste')
    Dicionario.inicializarDicionarioProdutos()
    testarBuscaProduto()
    testarAdicionarProduto()
    testarAtualizarProduto()
    testarRemoverProduto()

executarTestes()
