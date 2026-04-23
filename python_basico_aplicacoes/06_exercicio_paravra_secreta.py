import os
import random
import time

word_list  = ['javascript','ruby', 'lisp', 'java', 'python','html']
secret_word = random.choice(word_list)

##hidden_word  = list(secret_word.replace(secret_word[:], "*" * (len(secret_word))))

hidden_word = ["*"] * len(secret_word)

print(f"Palavra secreta: " + "".join(hidden_word ))

count = 0

print(f"""
BEM-VINDO AO JOGO
ACERTE A PALAVRA SECRETA
"""
)

while "*" in (hidden_word):
    try:
      
        typed_letter = input("Digite uma letra: ").lower()

        if(not typed_letter.isalpha() or len(typed_letter) != 1):
            print("Você informou um número ou mais de uma letra.")
            print("Informe apenas UMA letras válidas")
            continue
        count +=1 

        if(typed_letter in secret_word):
            for inx, char in enumerate(secret_word):
                if(char == typed_letter):
                    hidden_word [inx] = typed_letter
            print(f"Acertou! A palavra é: " + "".join(hidden_word ))
        else:
            print(f'A letra "{typed_word}" não está na palavra secreta.')
   
    except Exception as e:
        print(f"Erro: {e}")
    

print("PARABÉNS! VOCÊ GANHOU: " + secret_word)
print(f'Tentativas: {count}')
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')