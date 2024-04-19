print('1.feladat')
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
