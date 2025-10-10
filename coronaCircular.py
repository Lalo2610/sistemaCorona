# -------------------------------------
#        LALOTECH - Cálculo de Corona Circular
# -------------------------------------

def calcular_corona_circular():
    print("====================================")
    print("        LALOTECH - Corona Circular  ")
    print("====================================")

    try:
        # Entrada de datos
        radio_mayor = float(input("Ingrese el radio mayor (R): "))
        radio_menor = float(input("Ingrese el radio menor (r): "))

        # Validación
        if radio_menor >= radio_mayor:
            print("❌ Error: El radio menor debe ser menor que el radio mayor.")
            return

        # Constante pi
        PI = 3.141592653589793

        # Cálculos
        area = PI * (radio_mayor**2 - radio_menor**2)
        perimetro = 2 * PI * (radio_mayor + radio_menor)

        # Resultados
        print("\n✅ Resultados:")
        print(f"Área: {area:.2f} unidades²")
        print(f"Perímetro: {perimetro:.2f} unidades")

    except ValueError:
        print("❌ Error: Debe ingresar valores numéricos válidos.")

# Ejecutar programa
if __name__ == "__main__":
    calcular_corona_circular()
