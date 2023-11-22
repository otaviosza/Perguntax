class ArvoreDados:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_caminho_para_palavra(root, palavra_busca, caminho_atual=[]):
    if root is None:
        return None
    
    caminho_atual.append(root.valor)

    if root.valor.lower() == palavra_busca.lower():
        return " -> ".join(caminho_atual)

    caminho_esquerda = encontrar_caminho_para_palavra(root.esquerda, palavra_busca, caminho_atual.copy())
    caminho_direita = encontrar_caminho_para_palavra(root.direita, palavra_busca, caminho_atual.copy())

    return caminho_esquerda or caminho_direita

raiz = ArvoreDados("Maça")
raiz.esquerda = ArvoreDados("Morango")
raiz.direita = ArvoreDados("Pera")
raiz.esquerda.esquerda = ArvoreDados("Goiaba")
raiz.esquerda.direita = ArvoreDados("Limão")
raiz.direita.direita = ArvoreDados("Abacaxi")
raiz.direita.direita.direita = ArvoreDados("Laranja")
raiz.direita.direita.direita.direita = ArvoreDados("Cebola")
raiz.direita.direita.direita.esquerda = ArvoreDados("Banana")

palavra_busca = input("Digite a palavra que deseja buscar na árvore: ")

caminho_resultante = encontrar_caminho_para_palavra(raiz, palavra_busca)

if caminho_resultante:
    print(f"Caminho para '{palavra_busca}': {caminho_resultante}")
else:
    print(f"A palavra '{palavra_busca}' não foi encontrada na árvore.")
