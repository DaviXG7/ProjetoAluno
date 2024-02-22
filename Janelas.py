import tkinter as tk
import DadosPessoas
import random

telas = {}

Atual_Login = None

logado = Atual_Login is not None

labelsBuscadas = 0

ultimaBuscaAlunos = []

modoDeCadastro = True

pagina_atual = 1

buscado = False


def voltarPagina(tela, turma):
    if not buscado:
        return

    global pagina_atual
    if pagina_atual == 1:
        return

    pagina_atual -= 1

    for widget in tela.grid_slaves():
        info = widget.grid_info()
        if info["row"] >= 8:
            widget.grid_forget()

    try:
        alunos = DadosPessoas.pegarAlunos(turma)
    except ValueError as e:
        return

    index = 8

    for i in range(23):
        aluno_index = (pagina_atual - 1) * 23 + i
        if aluno_index < len(alunos):
            aluno = alunos[aluno_index]

            label_nome_aluno = tk.Label(tela, text=aluno.nome)
            label_matricula_aluno = tk.Label(tela, text=aluno.matricula)
            label_turma_aluno = tk.Label(tela, text=aluno.turma)
            label_m1_aluno = tk.Label(tela, text=aluno.m1)
            label_m2_aluno = tk.Label(tela, text=aluno.m2)
            label_m3_aluno = tk.Label(tela, text=aluno.m3)
            label_mf_aluno = tk.Label(tela, text=f"{aluno.mediaFinal:.2f}")

            label_nome_aluno.grid(row=index, column=0)
            label_matricula_aluno.grid(row=index, column=1)
            label_turma_aluno.grid(row=index, column=2)
            label_m1_aluno.grid(row=index, column=3)
            label_m2_aluno.grid(row=index, column=4)
            label_m3_aluno.grid(row=index, column=5)
            label_mf_aluno.grid(row=index, column=6)
            index += 1


def avancarPagina(tela, turma):
    if not buscado:
        return
    try:
        alunos = DadosPessoas.pegarAlunos(turma)
    except ValueError as e:
        return
    global pagina_atual

    if len(alunos) <= 23 * pagina_atual:
        return

    pagina_atual += 1

    for widget in tela.grid_slaves():
        info = widget.grid_info()
        if info["row"] >= 8:
            widget.grid_forget()

    index = 8

    for i in range(23):
        aluno_index = (pagina_atual - 1) * 23 + i
        if aluno_index < len(alunos):
            aluno = alunos[aluno_index]

            label_nome_aluno = tk.Label(tela, text=aluno.nome)
            label_matricula_aluno = tk.Label(tela, text=aluno.matricula)
            label_turma_aluno = tk.Label(tela, text=aluno.turma)
            label_m1_aluno = tk.Label(tela, text=aluno.m1)
            label_m2_aluno = tk.Label(tela, text=aluno.m2)
            label_m3_aluno = tk.Label(tela, text=aluno.m3)
            label_mf_aluno = tk.Label(tela, text=f"{aluno.mediaFinal:.2f}")

            label_nome_aluno.grid(row=index, column=0)
            label_matricula_aluno.grid(row=index, column=1)
            label_turma_aluno.grid(row=index, column=2)
            label_m1_aluno.grid(row=index, column=3)
            label_m2_aluno.grid(row=index, column=4)
            label_m3_aluno.grid(row=index, column=5)
            label_mf_aluno.grid(row=index, column=6)
            index += 1


def buscar(turma, tela, label):
    global pagina_atual
    global buscado
    global ultimaBuscaAlunos

    pagina_atual = 0

    try:

        for widget in tela.grid_slaves():
            info = widget.grid_info()
            if info["row"] >= 7:
                widget.grid_forget()

        alunos = DadosPessoas.pegarAlunos(turma)
        ultimaBuscaAlunos = alunos


    except ValueError as e:
        buscado = False
        label["text"] = "Nenhum aluno foi encontrado nesta turma!"
        print(e)
        return

    label_nome = tk.Label(tela, text="Nome")
    label_matricula = tk.Label(tela, text="Matrícula")
    label_turma = tk.Label(tela, text="Turma")
    label_m1 = tk.Label(tela, text="Nota primeiro trimestre")
    label_m2 = tk.Label(tela, text="Nota segundo trimestre")
    label_m3 = tk.Label(tela, text="Nota terceira trimestre")
    label_mf = tk.Label(tela, text="Nota final")

    label_nome.grid(row=7, column=0)
    label_matricula.grid(row=7, column=1)
    label_turma.grid(row=7, column=2)
    label_m1.grid(row=7, column=3)
    label_m2.grid(row=7, column=4)
    label_m3.grid(row=7, column=5)
    label_mf.grid(row=7, column=6)

    buscado = True

    avancarPagina(tela, turma)

    label["text"] = ""


def mudarModoDeCadastro(button, label):
    global modoDeCadastro
    if modoDeCadastro:
        button["text"] = "Clique para alterar o modo de cadastro: Aluno"
        label["text"] = "Formação"
        modoDeCadastro = False
    else:
        button["text"] = "Clique para alterar o modo de cadastro: Professor"
        label["text"] = "Turma"
        modoDeCadastro = True


def voltar_tela(function, telaatual):
    telaatual.destroy()
    function


def deslogar():
    global Atual_Login
    Atual_Login = None
    for value in telas.values():
        value.destroy()
    tela_inicial()


def logar(matricula, label):
    try:
        global Atual_Login
        Atual_Login = DadosPessoas.logar(matricula)
        if isinstance(Atual_Login, DadosPessoas.Aluno):
            for value in telas.values():
                value.destroy()
            tela_aluno(Atual_Login)
        else:
            for value in telas.values():
                value.destroy()
            tela_professor(Atual_Login)

    except ValueError as e:
        label['text'] = "Não foi possivel efetuar o login, você colocou um valor inválido ou não foi encontrado"
        print(e)


def cadastrar(nome, conteudo, label):
    matricula = "2" + str(random.randint(100000000, 999999999))

    if modoDeCadastro:
        try:

            aluno = DadosPessoas.Aluno(nome, int(matricula), conteudo, random.randrange(0, 10), random.randrange(0, 10),
                                       random.randrange(0, 10))
            DadosPessoas.addAluno(aluno)
            label["text"] = "Seu cadastro foi feito com sucesso! Sua matrícula é: " + matricula
        except ValueError as e:
            label["text"] = ("Há algo de errado no seu cadastro, verifique se você não deixou espaços ou não colocou "
                             "algo errado")
            print(e)
    else:
        try:
            professor = DadosPessoas.Professor(nome, int(matricula), conteudo)
            DadosPessoas.addProfessor(professor)
            label["text"] = "Seu cadastro foi feito com sucesso! Sua matrícula é: " + matricula
        except ValueError as e:
            label["text"] = ("Há algo de errado no seu cadastro, verifique se você não deixou espaços ou não colocou "
                             "algo errado")
            print(e)


def tela_inicial():
    tela = tk.Toplevel()
    tela.title('Tela inicial')
    botao_login = tk.Button(tela, text="Login", command=tela_login)
    botao_cadastro = tk.Button(tela, text="Cadrastar", command=tela_cadastro)

    botao_login.grid(row=0, column=0)
    botao_cadastro.grid(row=2, column=0)

    telas["tela inicial"] = tela


def tela_login():
    telas["tela inicial"].destroy()
    tela = tk.Toplevel()
    tela.title('Login')

    label_matricula = tk.Label(tela, text="Número da matrícula")
    label_matricula.grid(row=0, column=0)

    entry_matricula = tk.Entry(tela, width=20)
    entry_matricula.grid(row=0, column=1)

    label_erro = tk.Label(tela, text="")
    label_erro.grid(row=1, column=0)

    botao_login = tk.Button(tela, text="Login", command=lambda: logar(entry_matricula.get(), label_erro))
    botao_login.grid(row=2, column=0)
    voltar = tk.Button(tela, text="Voltar", command=lambda: voltar_tela(tela_inicial(), tela))
    voltar.grid(row=3, column=0)

    telas["tela login"] = tela


def tela_cadastro():
    telas["tela inicial"].destroy()
    tela = tk.Toplevel()
    tela.title('Cadastrar')

    label_erro = tk.Label(tela, text="")
    label_erro.grid(row=2, column=0)

    label_nome = tk.Label(tela, text="Nome completo")
    label_nome.grid(row=0, column=0)

    entry_nome = tk.Entry(tela, width=20)
    entry_nome.grid(row=0, column=1)

    label_Aluno_Professor = tk.Label(tela, text="Turma")
    label_Aluno_Professor.grid(row=1, column=0)

    entry_Aluno_Professor = tk.Entry(tela, width=20)
    entry_Aluno_Professor.grid(row=1, column=1)

    botao_cadastro = tk.Button(tela, text="Cadrastar",
                               command=lambda: cadastrar(entry_nome.get(), entry_Aluno_Professor.get(), label_erro))
    botao_cadastro.grid(row=3, column=0)

    botao_AlterarFormaDeCadastro = tk.Button(tela, text="Clique para alterar o modo de cadastro: Professor",
                                             command=lambda: mudarModoDeCadastro(botao_AlterarFormaDeCadastro,
                                                                                 label_Aluno_Professor))
    botao_AlterarFormaDeCadastro.grid(row=3, column=1)

    voltar = tk.Button(tela, text="Voltar", command=lambda: voltar_tela(tela_inicial(), tela))
    voltar.grid(row=4, column=0)

    telas["tela login"] = tela


def tela_professor(professor):
    tela = tk.Toplevel()

    telas["tela professor"] = tela

    tela.title("Logado como: " + professor.nome)

    label_suas_infos = tk.Label(tela, text="Suas informações:")
    label_suas_infos.grid(row=0, column=0)

    label_seu_nome = tk.Label(tela, text=f"Seu nome: {professor.nome}")
    label_seu_nome.grid(row=1, column=0)

    label_sua_matricula = tk.Label(tela, text=f"Sua matricula: {professor.matricula}")
    label_sua_matricula.grid(row=2, column=0)

    label_sua_formacao = tk.Label(tela, text=f"Sua formação: {professor.formacao}")
    label_sua_formacao.grid(row=3, column=0)

    label_erro = tk.Label(tela, text="")
    label_erro.grid(row=4, column=0)

    label_turmas = tk.Label(tela, text="Mostrar notas de turma: ")
    label_turmas.grid(row=5, column=0)

    entry_turmas = tk.Entry(tela, width=20)
    entry_turmas.grid(row=5, column=1)

    button_deslogar = tk.Button(tela, text="Deslogar", command=deslogar)
    button_deslogar.grid(row=6, column=0)

    button_voltar = tk.Button(tela, text="Voltar", command=lambda: voltarPagina(tela, entry_turmas.get()))
    button_voltar.grid(row=6, column=1)

    button_voltar = tk.Button(tela, text="Avançar", command=lambda: avancarPagina(tela, entry_turmas.get()))
    button_voltar.grid(row=6, column=2)

    botao_buscar = tk.Button(tela, text="Buscar",
                             command=lambda: buscar(entry_turmas.get(), tela, label_erro))
    botao_buscar.grid(row=5, column=2)


def tela_aluno(aluno):
    tela = tk.Toplevel()

    telas["tela aluno"] = tela

    tela.title("Logado como: " + aluno.nome)

    label_nome = tk.Label(tela, text="Nome")
    label_matricula = tk.Label(tela, text="Matrícula")
    label_turma = tk.Label(tela, text="Turma")
    label_m1 = tk.Label(tela, text="Nota primeiro trimestre")
    label_m2 = tk.Label(tela, text="Nota segundo trimestre")
    label_m3 = tk.Label(tela, text="Nota terceira trimestre")
    label_mf = tk.Label(tela, text="Nota final")

    label_nome_aluno = tk.Label(tela, text=aluno.nome)
    label_matricula_aluno = tk.Label(tela, text=aluno.matricula)
    label_turma_aluno = tk.Label(tela, text=aluno.turma)
    label_m1_aluno = tk.Label(tela, text=aluno.m1)
    label_m2_aluno = tk.Label(tela, text=aluno.m2)
    label_m3_aluno = tk.Label(tela, text=aluno.m3)
    label_mf_aluno = tk.Label(tela, text=f"{aluno.mediaFinal:.2f}")

    label_nome.grid(row=0, column=0)
    label_matricula.grid(row=0, column=1)
    label_turma.grid(row=0, column=2)
    label_m1.grid(row=0, column=3)
    label_m2.grid(row=0, column=4)
    label_m3.grid(row=0, column=5)
    label_mf.grid(row=0, column=6)

    label_nome_aluno.grid(row=1, column=0)
    label_matricula_aluno.grid(row=1, column=1)
    label_turma_aluno.grid(row=1, column=2)
    label_m1_aluno.grid(row=1, column=3)
    label_m2_aluno.grid(row=1, column=4)
    label_m3_aluno.grid(row=1, column=5)
    label_mf_aluno.grid(row=1, column=6)

    button_deslogar = tk.Button(tela, text="Deslogar", command=deslogar)
    button_deslogar.grid(row=2, column=0)
