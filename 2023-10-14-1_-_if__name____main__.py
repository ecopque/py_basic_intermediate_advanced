def soma(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__': #1:        
    print(soma(10, 15)) #2:
    print(soma(10, 25)) #3:
    print(__name__) #4:

def main() -> None: #5:
    print(soma(100, 150))
    print(soma(100, 250))

if __name__ == '__main__':
    main()


#1: Ou seja, se meu arquivo estiver sendo executado diretamente AQUI...
#2: Resposta: 25.
#3: Resposta: 35.
#4: Resposta: __main__.
#5: Também podemos fazer desta forma, como função.