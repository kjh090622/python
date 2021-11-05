import random

print("영어 단어 알파벳 찾기 게임")
print("===made by 북방코끼리바다표범")

words = ['book','bang','co','kili','bada','pyobum']
word = random.choice(words)

guesses = []

for _ in range(10):
    for char in word:
      if char in guesses:
        print(char,end=' ')
      else:
        print('_',end=' ')
    print()

    guess = input("알파벳을 입력하세요")
    guesses.append(guess)

    found_all = True
    for char in word:
      if char not in word:
           found_all = False
      if found_all:
        print("승리!")
        break
