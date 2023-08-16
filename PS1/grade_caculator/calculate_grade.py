def calculate_grade(checkpoint1, checkpoint2, checkpoint3, challenge, challenge2, global_solution):
    checkpoint_average = 0
    if checkpoint1 < checkpoint2 and checkpoint1 < checkpoint3:
        checkpoint_average = checkpoint2 + checkpoint3
    elif checkpoint2 < checkpoint1 and checkpoint2 < checkpoint3:
        checkpoint_average = checkpoint1 + checkpoint3
    else:
        checkpoint_average = checkpoint1 + checkpoint2
    
    checkpoint_average /= 2
    challenge_average = (challenge + challenge2) / 2
    final_grade = checkpoint_average * 0.2 + global_solution * 0.6 + challenge_average * 0.2
    return final_grade

while True:
    checkpoint1 = input("Qual foi a nota do seu primeiro checkpoint: ")
    checkpoint2 = input("Qual foi a nota do seu segundo checkpoint: ")
    checkpoint3 = input("Qual foi a nota do seu terceiro checkpoint: ")
    challenge = input("Qual foi a nota da sprint 1 do seu challenge: ")
    challenge2 = input("Qual foi a nota da sprint 2 do seu challenge: ")
    global_solution = input("Qual foi a nota do seu global solution: ")
    grade = calculate_grade(
        float(checkpoint1),
        float(checkpoint2),
        float(checkpoint3),
        float(challenge),
        float(challenge2),
        float(global_solution),
    )

    print("Sua nota final é -> " + str(grade))
    if grade >= 6:
        print("Parabéns! Você está aprovado! Hurray!")
    else:
        print("Que tistreza! Você está reprovado")