from codigo import Medicamento, NMedicamento

class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu()
      if op == 1: UI.MedicamentoInserir()
      if op == 2: UI.MedicamentoListar()
      if op == 3: UI.MedicamentoAtualizar()
      if op == 4: UI.MedicamentoExcluir()
      if op == 5: UI.MedicamentosVencidos()
        
  @classmethod
  def Menu(cls):
    print("\nMedicamentos: ")
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Medicamentos Vencidos")
    print("\nSair")
    print("99-Sair")
    return int(input())

  @classmethod
  def MedicamentoInserir(cls):
    descricao = input("Descrição: ")
    valor = input("Valor: ")
    vencimento = input("Vencimento (dd/mm/yyyy): ")
    medicamento = Medicamento(0, descricao, valor, vencimento)
    NMedicamento.inserir(medicamento)
    
  @classmethod
  def MedicamentoListar(cls):
    for medicamento in NMedicamento.listar():
      print(medicamento)
      
  @classmethod
  def MedicamentoAtualizar(cls):
    print("Medicamentos cadastrados")
    UI.MedicamentoListar()
    id = int(input("Id do medicamento a ser atualizado: "))
    descricao = input("Novo descricao: ")
    valor = input("Novo valor: ")
    vencimento = input("Novo vencimento (dd/mm/yyyy): ")
    medicamento = Medicamento(id, descricao, valor, vencimento)
    NMedicamento.atualizar(medicamento)    
    
  @classmethod
  def MedicamentoExcluir(cls):
    UI.MedicamentoListar()
    id = int(input("Id do medicamento a ser excluído: "))
    medicamento = Medicamento(id, "", "", "")
    NMedicamento.excluir(medicamento)

  @classmethod
  def MedicamentosVencidos(cls):
    print(*NMedicamento.vencidos())
    
UI.Main()