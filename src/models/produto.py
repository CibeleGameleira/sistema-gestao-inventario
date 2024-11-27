class Produto:
    def __init__(self, id: int, nome: str, quantidade: int, preco: float, importado: bool):
        self.id: int = id
        self.nome: str = nome
        self.quantidade: int = quantidade
        self.preco: float = preco
        self.importado: bool = importado