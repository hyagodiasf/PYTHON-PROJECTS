secret_word = 'amor'
aux_secret_word = list(secret_word.replace(secret_word[:],"*"*(len(secret_word))))
# aux_secret_word = ["*"] * len(secret_word)
print(f"""
BEM-VINDO AO JOGO
ACERTE A PALAVRA SECRETA
"""
)
print(f"Palavra secreta: " + "".join(aux_secret_word))

while "*" in (aux_secret_word):
  try:
    typed_word = input("Digite uma letra: ").lower()
    if(len(typed_word) != 1 or typed_word.isdigit()):
      print('Você informou um número ou mais de uma letra.')
      continue
    if(typed_word in secret_word):
      for inx, char in enumerate(secret_word):
        if(char == typed_word):
          aux_secret_word[inx] = typed_word
      print(f"Acertou! A palavra é: " + "".join(aux_secret_word))
    else:
      print(f'A letra "{typed_word}" não está na palavra secreta.')   
  except:
       pass
print("Parabéns! Você acertou a palavra: " + secret_word)
