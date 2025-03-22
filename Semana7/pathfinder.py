from collections import deque

# Só consegui dar uma testada no uso de pilha e fila, mas não consegui terminar a lógica do labirinto

# Pseudocódigo do que eu queria fazer:
# ter uma pilha para armazenar os passos do robô (LIFO)
# ter uma fila para armazenar as chaves que o robô pegasse (FIFO).
# mover o robô num mapa (não consegui montar o mapa direito)
# não consegui terminar

pilha_movimentos = []  # aqui queria guardar passos do robô
fila_chaves = deque()  # aqui guardaria as chaves

# uma função que adiciona movimento na pilha
def mover_para(frase_de_movimento):
    # ex: "CIMA", "BAIXO", "ESQUERDA", "DIREITA"
    pilha_movimentos.append(frase_de_movimento)
    print("Movimento adicionado na pilha:", frase_de_movimento)

# função para pegar chave e guardar na fila
def pegar_chave():
    fila_chaves.append("chave")
    print("Chave coletada! Fila agora tem:", len(fila_chaves))

# ueria criar algo pra usar a chave na porta
def usar_chave():
    if fila_chaves:
        fila_chaves.popleft()
        print("Chave da fila usada")
    else:
        print("Não tem chave nenhuma na fila")

# Comecei a testar chamando as funções, mas não terminei
mover_para("CIMA")
mover_para("CIMA")
pegar_chave()
mover_para("DIREITA")
usar_chave()
# 
# daqui em frente fiquei confuso e não finalizei nada :(

# Queria ainda fazer o robô "desfazer" movimentos (tipo se ele ficou preso) usando algo como:
#     ultimo = pilha_movimentos.pop()
# mas não deeu certo

print("\nCódigo incompleto, parei por aqui e não consegui resolver tudo")