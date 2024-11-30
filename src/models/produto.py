#Define a classe produto
class Produto:
    #Define o método construtor, para construir a instância do produto. 
    def __init__(self, nome: str, quantidade: int, preco: float, importado: bool):
        self.nome: str = nome
        self.quantidade: int = quantidade
        self.preco: float = preco
        self.importado: bool = importado
    
    #Esse método irá retornar uma representação da instância 
    def __repr__(self):
        return f"nome: {self.nome}, quantidade: {self.quantidade}, preco: {self.preco}, importado: {self.importado}"