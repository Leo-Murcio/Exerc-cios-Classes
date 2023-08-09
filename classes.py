class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Curso:", self.curso)
        print()
    
    def aniversario(self):
        self.idade += 1

estudante1 = Estudante("Messi", 36, "GOAT")
estudante2 = Estudante("Ronaldinho", 25, "Driblador")
estudante3 = Estudante("Ronaldo Fenomeno", 26, "Finalizador")
print("Informações dos Estudantes:")

estudante1.apresentar()
estudante1.aniversario()  
print("Depois do aniversário:")

estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()


