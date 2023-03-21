###3 checkpoints 2 valem 20%
# Global sc (prova) 30% 
# Challenge 50%
# a soma de tudo vale 40% no bimestre
print("##########################################")
print("######## CALCULADORA MEDIA FIAP ##########")
print("###########################################")

def calculate_rating(first_checkp, sec_checkp, thir_checkpoint, global_sc, challenge):
    media_cp = 0
    if (first_checkp < sec_checkp and sec_checkp < thir_checkpoint):
        media_cp = (sec_checkp + thir_checkpoint)/ 2
    elif (first_checkp > sec_checkp and sec_checkp < thir_checkpoint ):
        media_cp = (first_checkp + thir_checkpoint) / 2
    else:
        media_cp = (first_checkp + sec_checkp) / 2

    media_total = (media_cp * 0.20) + (global_sc * 0.30) + (challenge * 0.50)
    return media_total

first_checkp = float(input("Digite sua primeira nota do Checkpoint: "))
sec_checkp = float(input("Digite a nota do seu Segundo Checkpoint: "))
thir_checkpoint = float(input("Digite a terceira nota do seu Checkpoint: "))
global_sc_nota = float(input("Sua nota do global Solution: "))
challenge = float(input("Sua nota no Challenge: "))

media = calculate_rating(first_checkp, sec_checkp, thir_checkpoint, global_sc_nota, challenge)

print(f"sua media do checkpoint é: {media}")