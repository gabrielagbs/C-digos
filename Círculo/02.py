class Circulo:
  def __init__(self, raio):
    self.__raio = 0

  def set_raio(self, raio):
    if raio >= 0:
      self.__raio = raio
    else:
      ValueError()

  def get_raio(self):
    return self.__raio

  def calc_area(self):
    return 3.14 * (self.__raio ** 2)

  def calc_circunferencia(self):
    return 2 * 3.14 * self.__raio


class UI:
  @staticmethod
  def main():
    raio = float(input("Digite o valor do raio:"))
    c = Circulo(raio)
    print(f"Área: {c.calc_area()}")
    print(f"Circunferência: {c.calc_circunferencia()}")



UI.main()