import os
import time
import random
import json

def modo_easy(lista_pgt,score):
    for dic in lista_pgt:
        os.system("cls")
        print(dic["pgt"])
        print()
        print(dic["alt"])
        print()
        resposta = input("Insira a resposta:")
        if resposta == dic["resp"]:
            print("Resposta certa!")
            score += 1
            print(f"Pontuação: {score}")
            time.sleep(2)

        else:
            print("Reposta errada!")
            print(f"Pontuação: {score}")
            time.sleep(2)
            finalizar(score)
    print(f"Fim do quiz!\nSeu score foi de {score} pontos")
    time.sleep(4)
    quit()

def modo_hard(lista_pgt,score):
    for dic in lista_pgt:
        os.system("cls" if os.name=="nt" else "clear")
        print(dic["pgt"])
        print()
        print(dic["alt"])
        print()
        resposta = input("Insira a resposta:")
        if resposta == dic["resp"]:
            print("Resposta certa!")
            score += 1
            time.sleep(2)
        else:
            print("Reposta errada!")
            time.sleep(2)
            score -= 1
            if score <= 0:
                print("Você chegou a zero pontos. Fim de jogo!")
                time.sleep(1.5)
                os.system("cls" if os.name=="nt" else "clear")
                again = input("Quer inciar novamente?\nDigite 's' para sim e 'n' para não: ")
                if again == "s":
                    random.shuffle(lista_pgt)
                    perguntar(lista_pgt,score)
                elif again == 'n':
                    print("Até a próxima!")
                    time.sleep(3)
                    quit()
                else: 
                    print("Insira uma opção válida!")
            else:
                finalizar(score)
    print(f"Fim do quiz!\nSeu score foi de {score} pontos")
    time.sleep(4)
    quit()
            
def perguntar(lista_pgt,score):
    print("=====QUIZ DE PYTHON E SQL=====\n")
    print("Modos de jogo: ")
    print("""1 - Difícil\n(Ganha um ponto para cada pergunta correta e perde um ponto para cada erro. Se chegar a zero, perde o jogo.\n
          \n2 - Fácil\n(Ganha um ponto para cada pergunta correta)\n""")
    modo = input("Selecione o modo de jogo: ")
    if modo == "1":
        modo_hard(lista_pgt,score)
    elif modo == "2":
        modo_easy(lista_pgt,score)
    else:
        print("Selecione um modo válido!")

def finalizar(score):
    print("Quer continuar?")
    while True: 
        c = input("Pressione 's' para continuar ou 'n' para sair: ")
        if c == "n":
            print(f"Sua pontuação foi de {score} pontos")
            quit()
        elif c == "s":
            break
        else:
            print("Pressione uma tecla válida!")
            time.sleep(1)
    
with open("C:/Users/usu/OneDrive/Área de Trabalho/codigos/quiz de python/perguntas.json","r",encoding="utf-8") as arquivo:
    doc = json.load(arquivo)
    perguntas = doc["perguntas"]

random.shuffle(perguntas)
perguntar(perguntas,0)