from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ Legal (LIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11)
#  0  1  2  3  4  5  6  7  8  9  10, 11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ultimo_removido = lista.pop()
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Último: ', ultimo_removido) #1:
print('Lista:', lista) #2:
#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()

lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🚫 Ruim (FIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2.insert(0, 10)
#   0  1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2.insert(0, 11)
#  0   1   2  3  4  5  6  7  8  9, 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro_removido = lista2.pop(0)  # 11
#  0   1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro: ', primeiro_removido) #3:
print('Lista:', lista2)  #4:
print()

# ✅ Legal (FIFO com deque)

fila_correta: deque[int] = deque()
fila_correta.append(3) #5:
fila_correta.append(4) #6:
fila_correta.append(5) #7:
fila_correta.appendleft(2) #8:
fila_correta.appendleft(1) #9:
fila_correta.appendleft(0) #10:
print(fila_correta) #11:
fila_correta.pop()
fila_correta.popleft()
print(fila_correta) #12:

#Explanation Deque: Double-Ended Queue: A versatile data structure that efficiently supports adding and removing elements from both ends (front and back). Implemented in the collections module using collections.deque(). Offers constant-time performance (O(1)) for these operations.
#Explanation LIFO: Last-In-First-Out: Also known as a stack, it follows the principle where the last element added (pushed) is the first one removed (popped). Think of a stack of plates: the top plate (last added) is removed first.
#Explanation FIFO: First-In-First-Out: Also known as a queue, it operates on a "first-in, first-out" basis. The first element added (enqueued) is the first one removed (dequeued). Imagine a line of people waiting: the person who joined the line first gets served first.
#Obs: LIFO com listas é bom, FIFO com listas é ruim, FIFO com deque é bom.

#1: Response: 11.
#2: Response: Lista: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
#3: Response: 11.
#4: Response: Lista: [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
#5: Adiciona no final.
#6: Adiciona no final.
#7: Adiciona no final.
#8: Adiciona no começo.
#9: Adiciona no começo.
#10: Adiciona no começo.
#11: Response: deque([0, 1, 2, 3, 4, 5]).
#12: Response: deque([1, 2, 3, 4]).