import csv
"""
Creer une classe personne representant chaque ligne du fichier csv
"""
monFichier = open('clients.csv','r')
data = csv.reader(monFichier, delimiter=',')
print(data)
for line in data:
    print(line)
    #Creer un objet de type personne à partir de la ligne et le stocker dans une liste qui contient toutes les personnes