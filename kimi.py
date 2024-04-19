class Kimi:
    def __init__(self,datum, nagydij,helyezes,befejezett,pont,konstruktor,celba,korhatrany,hiba ):
        self.datum = datum
        self.nagydij = nagydij
        self.helyezes = helyezes
        self.befejezett = befejezett
        self.pont = pont
        self.konstruktor = konstruktor
        self.celba = celba
        self.korhatrany = korhatrany
        self.hiba = hiba
    def __str__(self):
        return f"Nagydíj időpontja: {self.datum} Nagydíj neve: {self.nagydij} Nagydíjon elért helyezése: {self.helyezes} Nagydíj során befejezett körök száma: {self.befejezett} Nagydíjon szerzett pontok {self.pont} Melyik csapat színében versenyzett : {self.konstruktor} Sikeres volt-e a verseny: {self.celba} Körhátrány: {self.korhatrany} Hiba oka : {self.hiba} "

f = open('kimi.csv', 'rt', encoding ='utf 8' )
f.readline()

lista = []

for sor in f:
    tmp = sor.strip().split(';')
    lista.append(Kimi(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], tmp[8]))
    #print(len(tmp))
print('3.feladat')
print(len(lista))
print('4.feladat : Magyar Nagydíj helyezései:')
for celba in lista:
    if celba.nagydij == 'Magyar Nagydíj':
        if celba.befejezett == "I":
            print(f'{celba.datum}: {celba.helyezes}helyezés')
        