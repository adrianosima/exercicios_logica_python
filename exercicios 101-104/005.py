"""

5. Os professores de Educação Física estão organizando 
uma seletiva para montar a equipe de natação. Para isso, 
eles convocaram os 7 melhores tempos da última competição 
e marcaram o tempo de cada um dos nadadores, na prova dos 
25 metros, estilo livre.
    Considerando que não houve tempos iguais, construa um pro
grama que leia o nome e o tempo (em segundos) de cada atleta 
e, em seguida, gere o seguinte relatório:
    a. nome do nadador com o melhor tempo
    b. nome do nadador com o pior desempenho
    c. tempo médio dos nadadores e
    d. quantidade de atletas com o tempo entre 12s e 15s

"""
from statistics import mean 



TempoNadatores = []
NomeNadadores = []
Nadadores12a15 = []

for i in range(7):
    Nome = input("Informe o nome do atleta: ")
    Tempo = float(input("Informe o tempos em segundo: "))

    if 12 < Tempo < 15:
        Nadadores12a15.append(Tempo)
        print(Nadadores12a15)
        
    TempoNadatores.append(Tempo)
    NomeNadadores.append(Nome)

MaiorPontuacacao = max(TempoNadatores)
NadadorMaiorPontuacacao = int(TempoNadatores.index(MaiorPontuacacao))

MenorPontuacacao = min(TempoNadatores)
NadadorMenorPontuacacao = int(TempoNadatores.index(MenorPontuacacao))

TempoMedioNadadores = mean(TempoNadatores)

print(f"Nadador com maior pontuação {NomeNadadores[NadadorMaiorPontuacacao]} potuação {MaiorPontuacacao}, Nadador com menor pontuação {NomeNadadores[NadadorMenorPontuacacao]} potuação {MenorPontuacacao}, tempo medio entre os nadadores {TempoMedioNadadores} ")
