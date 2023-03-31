def select_option():
    print("1 - Cadastrar o Aluno")
    print("2 - Lancar notas")
    print("3 - Consultar aluno")
    print("0 - Sair")

    option = int(input())
    return option

def creat_student():
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

def show_students(students):
    identification = input("Digite o Rm do Aluno: ")
    for student in students:
        if student['id'] == identification:
            print(student)
            return
    print("Nao foi encontrado esse aluno!")

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

students = []
option = select_option()
while option != 0:
    if option == 1:
        student = creat_student()
        students.append(student)
    elif option == 2:
        insert_grades(students)
    elif option == 3:
        show_students(students)
    option = select_option()
print(students)