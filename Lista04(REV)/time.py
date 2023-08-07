class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome = nome
    self.__camisa = camisa
    self.__gols = gols

  def get_gols(self):
    return self.__gols

  def __str__(self):
    return f"Nome = {self.__nome}, Camisa{self.__camisa}, Número de gols{self.__gols}"

class Time:
  def __init__(self, nome, estado):
    self.__nome = nome
    self.__estado = estado
    self.__jogadores = []

  def set_nome(self, nome):
    if nome == str():
      nome == self.__nome
    else:
      ValueError()
  def set_estado(self, estado):
    if estado == str():
      estado == self.__estado
    else:
      ValueError()

  def get_nome(self):
    return self.__nome
  def get_estado(self):
    return self.__estado

  def inserir(self, jogador):
    self.__jogadores.append(jogador) #append inseri objetos na lista

  def listar(self):
    return self.__jogadores

  def artilheiro(self): #entender melhor
    if len(self.__jogadores) == 0:
      return None
    artilheiro = self.jogadores[0]
    for jogador in self.__jogadores:
      if jogador.get_gols() > artilheiro.get_gols():
        artilheiro = jogador
        return artilheiro

