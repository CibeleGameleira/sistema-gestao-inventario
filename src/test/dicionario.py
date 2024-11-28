import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.dicionario import Dicionario
from models.produto import Produto

Dicionario.inicializarDicionarioProdutos()
Dicionario.adicionarProduto(Produto('Cibele', 10, 0.0, True))
print(Dicionario.buscarProduto(id=50))
Dicionario.atualizarProduto(50, Produto('Cibele', 11, 0.0, True))
print(Dicionario.buscarProduto(id=50))
Dicionario.removerProduto(50)
print(Dicionario.buscarProduto(id=50))
print(Dicionario.buscarProduto(id=1))
print(Dicionario.buscarProduto(nome='Produto 1'))

