class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
    def get_maior_lado(self):
        return max(self.lado_a, self.lado_b, self.lado_c)

lado_a = float(input("Informe o comprimento do lado A: "))
lado_b = float(input("Informe o comprimento do lado B: "))
lado_c = float(input("Informe o comprimento do lado C: "))

triangulo = Triangulo(lado_a, lado_b, lado_c)

perimetro = triangulo.calcular_perimetro()
maior_lado = triangulo.get_maior_lado()

print("O perímetro do triângulo é", perimetro)
print("O maior lado do triângulo é", maior_lado)