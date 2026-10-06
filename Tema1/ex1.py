import csv
import random

def alege_studenti(fisier_csv, numar_studenti):

    lista_studenti = []
        with open(fisier_csv, mode='r', encoding='utf-8') as fisier:
            cititor = csv.reader(fisier)

        for rand in cititor:
            if rand:
                lista_studenti.append(rand[0].strip())

    total_studenti = len(lista_studenti)

    studenti_selectati = random.sample(lista_studenti, k=numar_studenti)

    print(f"S-au selectat {numar_studenti} studenți din totalul de {total_studenti}:")
    for i, student in enumerate(studenti_selectati, start=1):
        print(f"{i}. {student}")

    numar_de_extras = 3

    alege_studenti(nume_fisier, numar_de_extras)