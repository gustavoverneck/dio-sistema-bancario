from .clientes import Cliente

from .utils import centavos_para_real, real_para_centavos

class SistemaBancario:
    def __init__(self):
        self.clientes = []
        
    def criar_conta(self, nome:str, senha:str, endereco:str, contato:str, saldo_inicial:float=0.0):
        saldo_inicial = real_para_centavos(saldo_inicial)   # Converte o saldo de reais para centavos
        id = str(len(self.clientes))
        self.clientes.append(
            Cliente(
                id=id,
                nome=nome,
                senha=senha,
                endereco=endereco, 
                contato=contato, 
                saldo_inicial=saldo_inicial
            )
        )
        print(f"Conta criada com sucesso!")
        print(f"ID: {id}")
        print(f"Nome: {nome}")
        print(f"Senha: {senha}")
        print(f"Endereço: {endereco}")
        print(f"Contato: {contato}")
        print(f"Saldo inicial: R$ {centavos_para_real(saldo_inicial):.2f}\n")
    
    def realizar_saque(self, id, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo")
        valor = real_para_centavos(valor)
        if self.clientes[id].sacar(valor):
            print("Saque realizado com sucesso!")
    
    def realizar_deposito(self, id, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo")
        valor = real_para_centavos(valor)
        if self.clientes[id].depositar(valor):
            print("Deposito realizado com sucesso!")
    
    def fazer_pix(self, id_user, id_destinatario, valor):
        if valor < 0:
            raise ValueError("O valor deve ser positivo")
        valor = real_para_centavos(valor)
        if self.clientes[id].sacar(valor):
            if self.clientes[id_destinatario].depositar(valor):
                print("Pix realizado com sucesso!")
        else:
            print("Não há saldo suficiente")
    
    def verificar_senha(self, id, senha):
        if senha == self.clientes[id].senha[0]:
            return True
        else:
            return False
    
    def iniciar_sessao_de_usuario(self, id, senha):
        if id <= len(self.clientes) and self.verificar_senha(id, senha):
            usuario = self.clientes[id]
            print(f"Olá {usuario.nome}")
        else:
            print("Senha errada.")
            return False
        while True:
            sair = not self.mostrar_menu(id)
            if sair:
                break
    
    def mostrar_menu(self, user_id):
        print("O que deseja fazer:")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Fazer Pix")
        print("4 - Sair")
        sucesso = False
        while not sucesso:
            escolha = int(input())
            if escolha in [1, 2, 3, 4]:
                sucesso = True
            else:
                print("Tente escolher novamente")
                
        
        match escolha:
            case 1:
                valor = float(input("Quanto deseja sacar (reais)?"))
                self.realizar_saque(user_id, valor)
            case 2:
                valor = float(input("Quanto deseja sacar (reais)?"))
                self.realizar_deposito(user_id, valor)
            case 3:
                valor = float(input("Quanto deseja transferir via pix?"))
                id_dest = int(input("Para quem deseja enviar?"))
                if valor > 0.0 and id_dest < len(self.clientes):
                    self.fazer_pix(user_id, id_dest, valor)
            case 4:
                return False
        