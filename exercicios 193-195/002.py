# exemplo de objetos (formigas em um gramado)
import turtle, random
class formiga:
    def __init__(self,i): #aqui define-se o comportamento inicial da formiga
 # um parâmetro passado é um número i
        self.t=turtle.Pen() #cria-se uma turtle de nome t no objeto e ela tem o método pen
        tcor=["violet","red","yellow","green","blue","brown","orange","pink","black",
 "purple","olive","fuchsia","blueviolet","plum",
 "coral","cornsilk","chartreuse","cyan","aqua","crimson"] #as diversas cores
 #ind=random.randint(0,7)
        self.t.color=tcor[i%len(tcor)]
 #a cor é atribuida de maneira circular
        self.t.ondex=200-random.randint(0,399) #a formiga começa em x=-200..200 randomicamente
        self.t.ondey=200-random.randint(0,399) # idem para y
        self.t.direcao=random.randint(0,359)
 # ganha uma direção randômica 0..360
        self.t.potencia=random.randint(1,11) # ganha uma potência randômica 1..11
        self.t.penup()
        # levanta a caneta
        self.t.goto(self.t.ondex,self.t.ondey) # vai para onde ela está
        self.t.pendown()
 # abaixa a caneta
    def anda(self): # como a formiga anda
        self.t.penup()
        # levanta a caneta
        self.t.goto(self.t.ondex,self.t.ondey) # vai para onde ela está
        self.t.pensize(self.t.potencia)
        # associa a grossura do traço à potência
        self.t.pendown()
        self.t.pencolor(self.t.color)
        dist=random.randint(25,70)
        ndir=random.randint(0,359)
        self.t.right(ndir)
        self.t.fd(dist)
        x=self.t.pos()
        # abaixa a caneta
        # associa a cor da caneta
        # dist= randomica 25..70
        # ndir= direção randômica 0..359
        # manda girar à direita ndir
        # manda andar dist
        # descobre onde parou (x,y)
        self.t.ondex=x[0]
        self.t.ondey=x[1]
x=[0]*60 # criam-se 60 formigas
for i in range(0,len(x)):
    x[i]=formiga(i)
    # guarda onde parou (x)
    # guarda onde parou (y)
    # cada formiga ganha a cor i
    x[i].anda()
 # anda
for j in range(len(x)): 
    for i in range(len(x)): # cada formiga (são 60) realiza 4 movimentos a cada ciclo
        x[i].anda()
    for i in range(len(x)):
        x[i].anda()
    for i in range(len(x)):
        x[i].anda()
    for i in range(len(x)):
        x[i].anda()