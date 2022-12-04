from fpdf import FPDF
import csv
from DOS2 import Skill, imprimir


def main():
    info=[]

    with open ("C:/Users/PC/Desktop/python/DOS2/skills.csv",newline="") as file:
        filereader=csv.DictReader(file,delimiter=";")
        for row in filereader:
            info.append(row)

    

    lista=[]
    for row in info:
        lista.append(Skill(row))


    imprimir(lista,"C:/Users/PC/Desktop/python/DOS2/DOS2 skills.pdf")


if __name__ == "__main__":
    main() 
