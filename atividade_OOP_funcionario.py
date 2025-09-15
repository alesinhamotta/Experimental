#demonstração OO atividade 2 fincionarios
class funcionarios:
    def __init__(self,nome,admissao,salario):
        self.nome= nome
        self.admissao= admissao
        self.salario= salario
    
    def SALARIO(self):
        if self.salario > 2000:
            print ("Gamnha mias de r$2000")
            return
        
class professores (funcionarios):
    def Materia (self):
        if self.MATERIA == "Matemática":
            print (f"{self.nome} Ensina matemática!")
            return 
professor1= professores ("João", "21/04/2001",2500," Matemática")        
professor1.salario()
professor1.Materia