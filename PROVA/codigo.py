import datetime
import json

class Medicamento:
  def __init__(self, id, descricao, valor, vencimento):
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__vencimento = vencimento

  def set_id(self, id):
    self.__id = id
  def set_descricao(self, descricao):
    self.__descricao = descricao
  def set_valor(self, valor):
    self.__valor = valor
  def set_vencimento(self, vencimento):
    self.__vencimento = vencimento
  def get_id(self):
    return self.__id
  def get_descricao(self):
    return self.__descricao
  def get_valor(self):
    return self.__valor
  def get_vencimento(self):
    return self.__vencimento
  def __str__(self):
    return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__vencimento}"



class NMedicamento:
  __medicamentos = []
  
  @classmethod
  def inserir(cls, obj):
    NMedicamento.abrir()
    id = 0
    for medicamento in cls.__medicamentos:
      if medicamento.get_id() > id: id = medicamento.get_id()
    obj.set_id(id+1)
    cls.__medicamentos.append(obj)
    NMedicamento.salvar()


  @classmethod
  def listar(cls):
     NMedicamento.abrir()    
     return cls.__medicamentos

  
  @classmethod
  def listar_id(cls, id):
    NMedicamento.abrir()
    for medicamento in cls.__medicamentos:
      if medicamento.get_id() == id: return medicamento
    return None


  @classmethod
  def atualizar(cls, obj):
    NMedicamento.abrir()
    medicamento = NMedicamento.listar_id(obj.get_id())
    if medicamento != None:
      # medicamento.set_id(obj.get_id())
      medicamento.set_descricao(obj.get_descricao())
      medicamento.set_valor(obj.get_valor())
      medicamento.set_vencimento(obj.get_vencimento())
      NMedicamento.salvar()

  @classmethod
  def excluir(cls, obj):
    NMedicamento.abrir()
    medicamento = cls.listar_id(obj.get_id())
    cls.__medicamentos.remove(medicamento)    
    NMedicamento.salvar()


  @classmethod
  def abrir(cls):
    try:
      cls.__medicamentos = []
      with open("medicamentos.json", "r") as c:
        medicamentos_json = json.load(c)
        for medicamento in medicamentos_json:
          c = Medicamento(medicamento["_Medicamento__id"], 
                          medicamento["_Medicamento__descricao"],
                          medicamento["_Medicamento__valor"], 
                          medicamento["_Medicamento__vencimento"])
          cls.__medicamentos.append(c)
    except FileNotFoundError:
      pass

  
  @classmethod
  def salvar(cls):
    with open("medicamentos.json", mode="w") as f:
      json.dump(cls.__medicamentos, f, default=vars)


  @classmethod
  def vencidos(cls):
    NMedicamento.abrir()
    lista_vencidos = []
    # hoje = datetime.datetime.now()
    for medicamento in cls.__medicamentos:
      data_medicamento = datetime.datetime.strptime(medicamento.get_vencimento(), "%d/%m/%Y")
      if data_medicamento < datetime.datetime.now():
        lista_vencidos.append(medicamento)
    if lista_vencidos == []:
      return "Nenhum medicamento vencido"
    else:
      return lista_vencidos