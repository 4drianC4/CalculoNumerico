import sympy as sp

def main():
    # Paso 1: Importar sympy y definir la variable simbólica 'x'
    x = sp.Symbol('x')

    # Paso 2: Define tu función en términos de 'x'
    funcion = x**3 + 2*x**2 - 4*x + 1

    # Paso 3: Calcula la derivada de la función con respecto a 'x'
    derivada = sp.diff(funcion, x)

    # Paso 4: Imprime la función derivada
    print("Derivada de la función:", derivada)

    # Paso 5: Sustituye el valor de 'x' por un número específico y obtén el resultado
    x_valor = 2
    resultado = derivada.subs(x, x_valor)
    print(f"Resultado de la función en x={x_valor}: {resultado}")
if __name__ == "__main__":
    main()
