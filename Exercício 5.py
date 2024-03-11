def inverter_string(s):
    # Inicia uma string vazia para armazenar o resultado
    resultado = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        # Concatena cada caractere à string resultado
        resultado += s[i]
    
    return resultado

# Exemplo de uso:
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)