class Cliente:
    def __init__(self, id:str, nome:str, senha:str, endereco:str, contato:str, saldo_inicial: int):
        self.id=id
        self.nome=nome,
        self.senha=senha,
        self.endereco=endereco, 
        self.contato=contato, 
        self.saldo = saldo_inicial  # Saldo em centavos
    
    def depositar(self, valor: int):
        if valor < 0:
            raise ValueError("Valor de depósito deve ser positivo")
        self.saldo += valor
        return True

    def sacar(self, valor:int):
        if valor > 0:
            if self.saldo - valor >= 0:
                self.saldo -= valor
                return True
        return False