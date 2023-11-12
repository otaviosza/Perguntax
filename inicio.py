# Conteúdo do arquivo inicio.py
from Pergunta1 import obter_resposta as resposta_A
from Pergunta2 import obter_resposta as resposta_B
from Pergunta3 import obter_resposta as resposta_C

def fazer_pergunta():
    print("Qual ativo digital se valorizou mais desde a sua criação?")
    print("A:", resposta_A())
    print("B:", resposta_B())
    print("C:", resposta_C())

def verificar_resposta(resposta_usuario):
    if resposta_usuario.lower() == "a":
        return resposta_A()
    elif resposta_usuario.lower() == "b":
        return resposta_B()
    elif resposta_usuario.lower() == "c":
        return resposta_C()
    else:
        return "Opção inválida."

if __name__ == "__main__":
    fazer_pergunta()
    resposta_usuario = input("Digite a letra correspondente à sua resposta: ")
    
    if resposta_usuario.lower() == "a":
        print("Parabéns! Você acertou. A resposta correta é:", resposta_A())
    else:
        print("Resposta incorreta.")
