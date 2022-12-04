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


    """poder1=Skill(info[208])
    poder2=Skill(info[209])
    poder3=Skill(info[0])

    imprimir([poder1,poder2,poder3],"C:/Users/PC/Desktop/python/DOS2/DOS2 algunas skills.pdf")"""


if __name__ == "__main__":
    main() 
