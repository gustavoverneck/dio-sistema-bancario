from sistema_bancario import banco

def main():
    sistema = banco.SistemaBancario()
    
    # Criar algumas contas de exemplo
    sistema.criar_conta("João Silva", "1234", "Rua A, 123", "11999999999", 1000.0)
    sistema.criar_conta("Maria Santos", "1234", "Rua B, 456", "11888888888", 500.0)
    
    # Exemplo de uso do sistema
    print("=== Sistema Bancário ===")
    
    # Login do usuário
    user_id = int(input("Digite seu ID de usuário: "))
    senha = str(input("Digite sua senha: "))
    
    sistema.iniciar_sessao_de_usuario(user_id, senha)

if __name__ == "__main__":
    main()