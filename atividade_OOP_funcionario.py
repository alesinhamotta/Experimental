# atividade_funcionarios.py

class Funcionario:
    def __init__(self, nome, admissao, salario):
        self.nome = nome
        self.admissao = admissao
        # garante que salario seja número (float)
        self.salario = float(salario)

    def recebe_acima_de(self, limite):
        """Retorna True se o salário do funcionário for maior que 'limite'."""
        return self.salario > limite

    def __repr__(self):
        return f"{self.nome} (R${self.salario:.2f}) - admissão: {self.admissao}"


def funcionarios_acima(lista_funcionarios, limite):
    """Retorna a lista de funcionários cujo salário é maior que 'limite'."""
    return [f for f in lista_funcionarios if f.recebe_acima_de(limite)]


# --- Exemplo de uso ---
if __name__ == "__main__":
    # cria uma lista com mais de 5 funcionários
    funcionarios = [
        Funcionario("João",  "21/04/2001", 2500),
        Funcionario("Maria", "10/03/2019", 1800),
        Funcionario("Pedro", "02/02/2017", 2200),
        Funcionario("Ana",   "15/09/2020", 2050),
        Funcionario("Lucas", "01/01/2018", 1900),
        Funcionario("Paula", "12/06/2016", 3000),
        Funcionario("Rafael","03/11/2015", 2100),
    ]

    # checa se tem mais de 5 funcionários
    if len(funcionarios) > 5:
        print(f"Total de funcionários: {len(funcionarios)} (maior que 5)\n")
    else:
        print(f"Total de funcionários: {len(funcionarios)} (não tem mais de 5)\n")

    limite = 2000.0
    acima = funcionarios_acima(funcionarios, limite)

    print(f"Funcionários que recebem acima de R${limite:.2f}:")
    if acima:
        for f in acima:
            print(f"- {f.nome}: R${f.salario:.2f} (admissão: {f.admissao})")
    else:
        print("Nenhum funcionário ganha mais que esse limite.")
