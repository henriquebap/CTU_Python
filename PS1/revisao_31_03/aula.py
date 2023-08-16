def select_option():
    print("1 - Cadastrar o Aluno")
    print("2 - Lancar notas")
    print("3 - Consultar aluno")
    print("4 - Listar todos os estudantes")
    print("0 - Sair")

    option = int(input())
    return option

def create_student():
    first_name = input("Digite o seu nome: ")
    last_name = input("Digite o seu sobre nome: ")
    student_class = input("Digite a sua turma: ")
    identification = input("Digite o seu RM: ")
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'class': student_class,
        'id': identification,
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

def show_students(students):
    identification = input("Digite o Rm do Aluno: ")
    for student in students:
        if student['id'] == identification:
            return student

def insert_grades(students):
    student = get_student(students)
    if not student:
        return 
    global_solution = float(input("Digite a nota do GC: ")) 
    challenge = float(input("Digite a nota do Challenge: "))
    checkpoints = []
    while True:
        if len(checkpoints) >= 3:
            option = input("Deseja cadastrar mais Checkpoints? [s]/[n]")
            if option == 'n':
                break
        checkpoint = float(input("Digite a nota do checkpoint: "))
        checkpoints.append(checkpoint)
    student['challenge'] = challenge
    student['global_solution'] = global_solution
    student['checkpoints'] = checkpoints

def show_students(students):
    for student in students:
        print(student)

students = []
while True:
    option = select_option()
    if option == 0:
        break
    if option == 1:
        student = create_student()
        students.append(student)
    elif option == 2:
        insert_grades(students)
    elif option == 3:
        show_students(students)
        if student:
            print(student)
        else:
            print("Aluno nao foi encontrado!")
            confirmation = input("Deseja cadastrar um novo aluno? (s/n)")
            if confirmation == 's':
                student = create_student()
                students.append(student)
    elif option == 4:
        show_students(students)