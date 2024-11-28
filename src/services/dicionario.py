import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.produto import Produto

class Dicionario: 
    estoque = {}
    @staticmethod
    def inicializarDicionarioProdutos (): 
         for i in range(1, 50):
            produto = Produto(f"Produto {i}", 1, 0.0, False)
            Dicionario.estoque[i] = produto

    @staticmethod
    def adicionarProduto (produto: Produto):
        ultimoProduto = list(Dicionario.estoque.keys())[-1]
        Dicionario.estoque[ultimoProduto + 1] = produto

    @staticmethod
    def atualizarProduto (id, produto: Produto):
        Dicionario.estoque[id] = produto

    @staticmethod
    def removerProduto (id):
        Dicionario.estoque.pop(id, None) 

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
        


    
             

