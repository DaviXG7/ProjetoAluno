import json


def pegarProfessor(matricula):
    with open("alunos.json", "r") as arquivo:
        data = json.load(arquivo)
        for professor in data:
            if int(matricula) == professor["matricula"]:
                return professor
    return None


def pegarAluno(matricula):
    with open("alunos.json", "r") as arquivo:
        data = json.load(arquivo)
        for aluno in data:
            if int(matricula) == aluno["matricula"]:
                return aluno
    return None


def pegarAlunos(turma):
    with open("alunos.json", "r") as arquivo:
        data = json.load(arquivo)
        alunos = []
        for aluno in data:
            if aluno["turma"] == turma:
                alunos.append(Aluno(aluno["nome"], aluno["matricula"], aluno["turma"], aluno["m1"], aluno["m2"], aluno["m3"]))
        if len(alunos) == 0:
            raise ValueError("Nenhum aluno foi encontrado")
        return alunos
    return None


def addAluno(aluno):
    with open("alunos.json", "r") as arquivo:
        data = json.load(arquivo)
        data.append(aluno.to_dict())
    with open("alunos.json", "w") as arquivo:
        json.dump(data, arquivo, indent=2)


def logar(matricula):
    with open("alunos.json", "r") as arquivo:
        dados = json.load(arquivo)
        for conta in dados:
            if int(matricula) == conta["matricula"]:
                return Aluno(conta["nome"], conta["matricula"], conta["turma"], conta["m1"], conta["m2"], conta["m3"])
    with open("professores.json", "r") as arquivo:
        dados = json.load(arquivo)
        for conta in dados:
            if int(matricula) == conta["matricula"]:
                return Professor(conta["nome"], conta["matricula"], conta["formacao"])

    raise ValueError("Não foi possivel logar na conta")


def addProfessor(professor):
    with open("professores.json", "r") as arquivo:
        data = json.load(arquivo)
        data.append(professor.to_dict())
    with open("professores.json", "w") as arquivo:
        json.dump(data, arquivo, indent=2)


class Conta:

    def __init__(self, nomeCompleto, matricula):
        self.nome = nomeCompleto
        self.matricula = matricula


class Aluno(Conta):

    def __init__(self, nomeCompleto, matricula, turma, m1, m2, m3):
        super().__init__(nomeCompleto, matricula)
        self.turma = turma
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.mediaFinal = (m1 + m2 + m3) / 3

    def to_dict(self):
        return {"nome": self.nome, "matricula": self.matricula, "turma": self.turma, "m1": self.m1, "m2": self.m2,
                "m3": self.m3}


class Professor(Conta):

    def __init__(self, nomeCompleto, matricula, formacao):
        super().__init__(nomeCompleto, matricula)
        self.formacao = formacao

    def to_dict(self):
        return {"nome": self.nome, "matricula": self.matricula, "formacao": self.formacao}
