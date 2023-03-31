def select_option():
    """
    Função que exibe as opções para o usuário
    Pede que ao usuário que entre com uma opção
    input sempre retorna string, então é convertido para int
    Retorna um inteiro
    """
    print("1 - Cadastrar estudante")
    print("2 - Lançar notas")
    print("3 - Consultar estudante")
    print("4 - Listar estudantes")
    print("0 - Sair")

    option = int(input())
    return option


def create_student():
    """
    Pede ao usuário os dados do estudante
    As variaveis first_name, last_name, student_class e identification
    são utilizadas para criar um dicionário
    Retorna um dicionário com os dados do usuário
    """
    first_name = input("Digite seu primeiro nome: ")
    last_name = input("Digite seu sobrenome: ")
    student_class = input("Digite a sua turma: ")
    identification = input("Digite seu RM: ")
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'class': student_class,
        'id': identification
    }
    return student


def get_student(students):
    """
    A função localiza e retorna um estudante
    Tem como parâmetro a lista de estudantes onde
    será realizada a busca
    Retorna um dicionário com os dados do estudante
    caso seja localizado.
    Se não achar o estudante, não retorna nada
    """
    identification = input("Digite o RM do aluno: ")
    for student in students:
        # Verifica atráves da chave id se o conteúdo
        # da chave é igual ao dado informado pelo usuário
        if student['id'] == identification:
            return student


def insert_grades(students):
    """
    Atualiza as notas de um estudante
    Primeiro ele acha um estudante utilizando
    a função get_student. Se não encontrar,
    apenas encerra a sua execução
    Ao achar um estudante, pede para o usuário
    as notas.
    Não retorna nada, porque a função atualiza
    os dados do estudante
    """
    student = get_student(students)
    if not student:
        return
    
    global_solution = float(input("Digite a nota do global solution: "))
    challenge = float(input("Digite a nota do challenge: "))
    checkpoints = []
    while True:
        """
        Esse loop é eterno até que pelo menos
        3 notas de checkpoints sejam cadastradas
        """
        if len(checkpoints) >= 3:
            option = input("Deseja cadastrar mais checkpoints (s/n)?")
            if option == 'n':
                break
        checkpoint = float((input("Digite a nota do checkpoint: ")))
        checkpoints.append(checkpoint)

    
    # grade = {
    #     'challenge': challenge,
    #     'global_solution': global_solution,
    #     'checkpoints': checkpoints
    # }
    # student.update(grade)
    # O código acima está comentado, pois é uma outra forma de atualizar os dados

    student['challenge'] = challenge
    student['global_solution'] = global_solution
    student['checkpoints'] = checkpoints
    

def show_students(students):
    for student in students:
        print(student)

students = []
while True:
    """
    Essa forma é uma das possíveis abordagens
    para validar qual opção o usuário selecionou
    A função select_option é executada apenas
    uma vez. Caso seja selecionada a opção 0,
    sai do loop.
    Do contrário, verifica qual das opções foi selecionada
    """
    option = select_option()
    if option == 0:
        break

    if option == 1:
        student = create_student()
        students.append(student)
    elif option == 2:
        insert_grades(students)
    elif option == 3:
        student = get_student(students)
        if student: # Não se preocupe com isso. Será abordado ao longo do curso
            print(student)
        else:
            print("Não foi encontrado este estudante")
            confirmation = input("Deseja cadastrar um novo (s/n)?")
            if confirmation == 's':
                student = create_student()
                students.append(student)
    elif option == 4:
        show_students(students)
