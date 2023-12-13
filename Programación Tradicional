class ClimaSemana:
    def __init__(self):
        self.temperaturas = [0] * 7

    def ingresar_temperaturas_diarias(self):
        for dia in range(7):
            self.temperaturas[dia] = float(input(f"Ingrese la temperatura del día {dia + 1}: "))

    def calcular_promedio_semanal(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

# Programa principal
def main_poo():
    print("Programa de cálculo del promedio semanal del clima")
    clima_semana = ClimaSemana()
    clima_semana.ingresar_temperaturas_diarias()
    promedio = clima_semana.calcular_promedio_semanal()
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

if __name__ == "__main__":
    main_poo()
