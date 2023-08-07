class Esporte:
  def __init__(self, nome, horarios, mensalidade):
    self.__nome = nome
    self.__horarios = horarios
    self.__mensalidade = mensalidade

  def set_nome(self, nome):
    if nome == str():
      nome = self.__nome
    else:
      ValueError()
  def set_horarios(self, horarios):
    if horarios == str():
      horarios = self.__horarios
    else:
      ValueError()
  def set_mensalidade(self, mensalidade):
    if mensalidade != 0:
      mensalidade = self.__mensalidade
    else:
      ValueError()

  def get_nome(self):
    return self.__nome
  def get_horarios(self):
    return self.__horarios
  def get_mensalidade(self):
    return self.__mensalidade

  def __str__(self):
    return f"Nome: {self.__nome}, Horários: {self.__horarios}, Mensalidade: {self.__mensalidade}"

class Academia:
  def __init__(self, nome, endereco):
    self.__nome = nome
    self.__endereco = endereco
    self.__esportes = []

  def set_nome(self, nome):
    if nome == str():
      nome = self.__nome
    else:
      ValueError()
  def set_endereco(self, endereco):
    if endereco == str():
      endereco = self.__endereco
    else:
      ValueError()

  def get_nome(self):
    return self.__nome
  def get_endereco(self):
    return self.__endereco

  def inserir(self, esporte):
    self.__esportes.append(esporte)

  def listar(self):
    return self.__esportes

  def mediamensalidade(self):
    media = 0
    for esporte in self.__esportes:
      media += esporte.get_mensalidade()
    return media / len(self.__esportes)

  def __str__(self):
    return f"Nome: {self.__nome}, Endereço: {self.__endereco}, Esportes: {self.__esportes}"

