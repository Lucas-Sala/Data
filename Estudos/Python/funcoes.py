def fahr_to_celsius(temp):
    """
    Função que recebe como argumento uma temperatura
    em Fahrenheit e converte ela para Celsius 
    """
    return ((temp - 32) * (5/9))

fahr = float(input("Temperatura em Fahrenheit: "))

print(f"{fahr_to_celsius(fahr):.2f} °C")

