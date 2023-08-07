class Circulo:
  def __init__(self, raio):
    self.raio = 0

  def area(self):
    return 3.14 * (self.raio ** 2)
  def circunferencia(self):
    return 2 * (3.14 * self.raio)

n = Circulo()
n.raio = float(input("Digite o valor do raio:"))
print(n.area())
print(n.circunferencia())