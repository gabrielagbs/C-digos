import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome  
    self.__email = email
    self.__fone = fone
  def set_id(self, id):
    self.__id = id
  def set_nome(self, nome):
    self.__nome = nome
  def set_email(self, email):
    self.__email = email
  def set_fone(self, fone):
    self.__fone = fone
  def get_id(self):
    return self.__id
  def get_nome(self):
    return self.__nome
  def get_email(self):
    return self.__email
  def get_fone(self):
    return self.__fone
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 # encontrar o maior id já usado
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)




class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.__id = id
    self.__descricao = descricao
    self.__valor = valor
    self.__duracao = duracao
  def get_id(self): return self.__id
  def get_descricao(self): return self.__descricao
  def get_valor(self): return self.__valor
  def get_duracao(self): return self.__duracao
  def set_id(self, id): self.__id = id
  def set_descricao(self, descricao): self.__descricao = descricao
  def set_valor(self, valor): self.__valor = valor
  def set_duracao(self, duracao): self.__duracao = duracao
  def __str__(self):
    return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__duracao}"

class NServico:
  __servicos = []         # lista de servicos inicia vazia
  @classmethod
  def inserir(cls, obj):
    NServico.abrir()
    id = 0 # encontrar o maior id já usado
    for servico in cls.__servicos:
      if servico.get_id() > id: id = servico.get_id()
    obj.set_id(id + 1)
    cls.__servicos.append(obj)  # insere um servico (obj) na lista
    NServico.salvar()
  @classmethod
  def listar(cls):
    NServico.abrir()    
    return cls.__servicos       # retorna a lista de servicos
  @classmethod
  def listar_id(cls, id):
    NServico.abrir()
    for servico in cls.__servicos:
      if servico.get_id() == id: return servico
    return None
  @classmethod
  def atualizar(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    servico.set_descricao(obj.get_descricao())
    servico.set_valor(obj.get_valor())
    servico.set_duracao(obj.get_duracao())
    NServico.salvar()
  @classmethod
  def excluir(cls, obj):
    NServico.abrir()
    servico = cls.listar_id(obj.get_id())
    cls.__servicos.remove(servico)    
    NServico.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__servicos = []
      with open("servicos.json", mode="r") as f:
        s = json.load(f)
        for servico in s:
          c = Servico(servico["_Servico__id"], servico["_Servico__descricao"],
                     servico["_Servico__valor"], servico["_Servico__duracao"])
          cls.__servicos.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("servicos.json", mode="w") as f:
      json.dump(cls.__servicos, f, default=vars)



class Agenda:
    def __init__(self, id, data, confirmado, idCliente, idServico):
         self.__id = id
         self.__data = datetime.datetime.strptime(data)
         self.__confirmado = confirmado
         self.__idCliente = idCliente
         self.__idServico = idServico

    def get_id(self): 
        return self.__id
    def get_data(self): 
        return self.__data
    def get_confirmado(self): 
        return self.__confirmado
    def get_idCliente(self): 
        return self.__idCliente
    def get_idServico(self):
         return self.__idServico

    def set_id(self, id):
         self.__id = id
    def set_data(self, data):
        self.__data = data
    def set_confirmado(self, confirmado):
         self.__confirmado = confirmado
    def set_idCliente(self, idCliente): 
        self.__idCliente = idCliente
    def set_idServico(self, idServico):
         self.__idServico = idServico

    def __str__(self):
      return f"{self.__id} - {self.__data} - {self.__confirmado} - {self.__idCliente} - {self.__idServico}"

class NAgenda:
    __agendas = []

    @classmethod
    def inserir(cls, obj):
      NAgenda.abrir()
      id = 0 
      for agente in cls.__agentes:
        if agente.get_id() > id: id = agente.get_id()
      obj.set_id(id + 1)
      cls.__agentes.append(obj)  
      NAgenda.salvar()

    @classmethod
    def listar(cls):
      NAgenda.abrir()    
      return cls.__agendas

    @classmethod
    def listar_id(cls, id):
      NAgenda.abrir()
      for agenda in cls.__agendas:
        if agenda.get_id() == id: 
            return agenda
      return None

    @classmethod
    def excluir(cls, obj):
      NAgenda.abrir()
      agenda = cls.listar_id(obj.get_id())
      cls.__agendas.remove(agenda)    
      NAgenda.salvar()
      
    @classmethod
    def abrir(cls):
        try:
          cls.__clientes = []
          with open("clientes.json", mode="r") as f:
            s = json.load(f)
            for cliente in s:
              c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"], cliente["_Cliente__email"], cliente["_Cliente__fone"])
              cls.__clientes.append(c)
        except FileNotFoundError:
          pass