def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

string_original = input("Informe uma string para ser invertida: ")

resultado = inverter_string(string_original)

print(f"String invertida: {resultado}")
