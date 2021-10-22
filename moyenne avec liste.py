print("nous allons calculer la moyenne des notes que vous allez entrer")
liste=[]
n=0
while n!="fin" :
    n=input("Entrer une note ou écrire fin si il n'y a plus de note à entrer")
    if n!= "fin" :
        n = float(n)
        liste.append(n)
print("Vous avez entré", len(liste), "notes")
m=sum(liste)/len(liste)
print("la moyenne de votre série est", m)