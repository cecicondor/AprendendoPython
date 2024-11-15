def lernotas():
    n=float(input("Digite a nota do aluno: ")) #aqui vai imputar os valores dos alunos
    return n

def resultado(n1,n2):
    media=(n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("media:", media, "Resultado:", end ="") #aqui vamos fazer o cálculo das médias

    if media >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")  #nessa parte da função vamos verificar a condição se o aluno foi ou não aprovado

a=lernotas()
b=lernotas()
resultado(a,b)