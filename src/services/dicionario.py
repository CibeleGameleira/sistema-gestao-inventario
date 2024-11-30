import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.produto import Produto

# Classe que representa o Dicionário de Produtos
class Dicionario: 
    estoque = {} #dicionário
    
    # Essa função é responsável por inicializar o dicionário, adicionando em um laço de repetição instâncias de produtos
    # Essa função é um método estático, pois não precisa de um objeto para ser chamado.  
   
    @staticmethod
    def inicializarDicionarioProdutos():
         for i in range(1, 50):
            produto = Produto(f"Produto {i}", 1, 0.0, False)
            Dicionario.estoque[i] = produto

    #Essa função é responsável por adicionar um produto baseado no que foi passado como parâmetro para função
    #Essa função valida o ID do último produto, adicionando em uma nova posição o produto
    #Essa função é um método estático, pois não precisa de um objeto para ser chamado.  

    @staticmethod
    def adicionarProduto(produto: Produto):
        ultimoProduto = list(Dicionario.estoque.keys())[-1]
        Dicionario.estoque[ultimoProduto + 1] = produto

    #Essa função é responsável por atualizar um produto baseado no ID passado como parâmetro para função
    #Essa função é um método estático, pois não precisa de um objeto para ser chamado.  
    #Essa função atualiza o produto na posição correspondente do dicionário, podendo atualizar as propriedades quantidade e preço
    #Caso não seja passado um novo valor para quantidade ou preço, a função não altera o valor da respectiva propriedade do produto.    
    #Essa função também valida se é encontrado o produto com o ID passado por parâmetro
    @staticmethod
    def atualizarProduto(id,quantidade=None, preco=None):
        if id in Dicionario.estoque:
            if  quantidade is not None:
                Dicionario.estoque[id].quantidade = quantidade
            if preco is not None:
                Dicionario.estoque[id].preco = preco

    #Essa função é responsável por remover um produto baseado no ID passado como parâmetro para função
    #Essa função é um método estático, pois não precisa de um objeto para ser chamado.  

    @staticmethod
    def removerProduto(id):
        Dicionario.estoque.pop(id, None) 

    #Essa função é responsável por buscar um produto baseado no ID ou nome passado como parâmetro para função
    #Essa função retorna o produto caso seja encontrado, caso contrário, retorna uma mensagem de produto não encontrado
    #Essa função é um método estático, pois não precisa de um objeto para ser chamado.  
    @staticmethod
    def buscarProduto(id=None, nome=None):
        if id is not None:
            if id in Dicionario.estoque:
                return Dicionario.estoque.get(id)

        if nome is not None:
            for produto in Dicionario.estoque.values():
                if produto.nome == nome:
                    return produto
        
        return "Produto não encontrado"
    
    
        


    
             

