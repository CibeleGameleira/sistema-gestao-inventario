class Produto:
    def __init__(self, nome: str, quantidade: int, preco: float, importado: bool):
        self.nome: str = nome
        self.quantidade: int = quantidade
        self.preco: float = preco
        self.importado: bool = importado

    def __repr__(self):
        return f"nome: {self.nome}, quantidade: {self.quantidade}, preco: {self.preco}, importado: {self.importado}"