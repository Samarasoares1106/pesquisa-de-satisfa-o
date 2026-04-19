# Inicialização dos contadores
qtd_excelente = 0
qtd_ruim = 0

# Definindo o número de entrevistados para o teste (alterar para 50 no uso real)
total_entrevistados = 50

print("--- Pesquisa de Satisfação TudoWeb ---")

for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado nº {i}:")
    
    # Coleta de dados básicos
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    # Coleta e validação da opinião
    print("Opiniões: 1-EXCELENTE | 2-BOM | 3-RUIM")
    opiniao = input("Digite sua opinião (1, 2 ou 3): ")

    # Estrutura de decisão para contabilização
    if opiniao == '1':
        qtd_excelente += 1
    elif opiniao == '3':
        qtd_ruim += 1
    # Opção '2' (BOM) não precisa ser contada individualmente conforme o enunciado

# Exibição dos resultados finais
print("\n" + "="*30)
print("RESULTADO FINAL DA PESQUISA")
print("="*30)
print(f"Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"Quantidade de respostas 'RUIM': {qtd_ruim}")
