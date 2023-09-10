import datetime
import enum

class Midia(enum.Enum):
  enum.LP = int()
  enum.CD = int()
  enum.DVD = int()
  enum.BD = int()
  enum.Stream = int()

class Album:
  def __init__(self, titulo, formato, gravadora, lancamento):
    self.__titulo = titulo
    self.__formato = Midia()
    self.__gravadora = gravadora
    self.lancamento = datetime.datetime()

  def get_titulo(self):
    return self.__titulo
  def get_formato(self):
    return self.__formato
  def get_gravadora(self):
    return self.__gravadora
  def get_lancamento(self):
    return self.__lancamento
  def __str__(self):
    return(f"Título: {self.__titulo}, Formato: {self.__formato}, Gravadora: {self.__gravadora}, Lançamento: {self.__lancamento}")

class Banda:
  def __init__(self, nome, pais, estilo):
    self.__nome = nome
    self.__pais = pais
    self.__estilo = estilo
    self.__albuns = []

  def get_nome(self):
    return self.__nome
  def get_pais(self):
    return self.__pais
  def get_estilo(self):
    return self.__estilo

  def inserir(self, album):
    self.__albuns.append(album)

  