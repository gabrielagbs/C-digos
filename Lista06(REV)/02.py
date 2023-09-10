class Campeonatos:
	def __init__(self,id,nome,data):
		self.__id=id
		self.__nome=nome
		self.__data=data
	def set_id(self,id):
		if id>0:
			self.__id=id
		else:raise ValueError()
	def set_nome(self,nome):
		if nome==str():
			self.__nome=nome
		else:raise ValueError()
	def set_data(self,data):
		if data>0:
			self.__data=data
		else:raise ValueError()
	def get_id(self):
		return self.__id
	def get_nome(self):
		return self.__nome
	def get_data(self):
		return self.__data
	def __str__(self):
		return f"id={self.__id},nome={self.__nome},data={self.__data}"

class Fases:
	def __init__(self,id,idCampeonato,fase):
		self.__id=id
		self.__idCampeonato=idCampeonato
		self.__fase=fase
		self.set_id(id)
		self.idCampeonato(idCampeonato)
		self.set_fase(fase)
	def set_id(self,id):
		if id>0:
			self.__id=id
		else:raise ValueError()
	def set_idCampeonato(self,idCampeonato):
		if idCampeonato>0:
			self.__idCampeonato=idCampeonato
		else:raise ValueError()
	def set_fase(self,fase):
		if fase==str():
			self.__fase=fase
		else:raise ValueError()
	def get_id(self):
		return self.__id
	def get_idCampeonato(self):
		return self.__idCampeonato
	def get_fase(self):
		return self.__fase
	def __str__(self):
		return f"Id={self.__id}, idCampeonato={self.__idCampeonato}, Fase={self.__fase}"

class Equipe:
	def __init__(self,id,idCampeonato,time,jogadores):
		self.__id=id
		self.__idCampeonato=idCampeonato
		self.__time=time
		self.__jogadores=jogadores
		self.set_id(id)
		self.set_idCampeonato(idCampeonato)
		self.set_time(time)
		self.set_jogadores(jogadores)
	def set_id(self,id):
		if id>0:
			self.__id=id
		else:raise ValueError()
	def set_idCampeonato(self,idCampeonato):
		if idCampeonato>0:
			self.__idCampeonato=idCampeonato
		else:raise ValueError()
	def set_time(self,time):
		if time==str():
			self.__time=time
		else:raise ValueError()
	def set_jogadores(self,jogadores):
	if jogadores==str():
		self.__jogadores=jogadores
	else:raise ValueError()
	def get_id(self):
		return self.__id
	def get_idCampeonato(self):
		return self.__idCampeonato
	def get_time(self):
		return self.__time
	def get_jogadores(self):
		return self.__jogadores
	
	def __str__(self):
		return f"Id={self.__id}, idCampeonato={self.__idCampeonato}, Fase={self.__fase}"

class NEquipe:
	def __init__(self):
		self.equipes=[]
	def inserir(self,m):
		self.equipes.append(m)
	def listar(self):
		return self.equipes
	def atualizar(self,m):
		for obj in self.equipes:
			if
			obj.get_id()==m.get_id():
				obj.set_time(m.get_time())
obj.set_jogadores(m.get_jogadores())

	def deletar(self,m):
		self.equipes.remove(m)

class UI:
	def menu():
		print("0-fim, 1-inserir,2-Listar, 3-Atualizar,4-Remover")
		return int(input())
	def main():
		op=1
		C=Campeonatos("1","Copa","27/11")
		NE=NEquipe()