import csv
from fpdf import FPDF
from PIL import Image
import requests
import os


class Skill:
    def __init__(self,skill_info:dict):
                         
        self.name=skill_info["Name"]    
        self.description=skill_info["Description"] 
        self.requirements=skill_info["Requirements"] 
        self.cooldown=skill_info["Cooldown"] 
        self.slots=skill_info["Slots"] 
        self.range=skill_info["Range"] 
        self.sets=skill_info["Sets"] 
        self.stat=skill_info["Stat"] 
        self.school_image=skill_info["School Image"] 
        self.school=skill_info["School"] 
        self.ap=skill_info["Ap"] 
        self.sp=skill_info["Sp"] 
        self.image=skill_info["Image"] 


def poner_imagen(pdf,link,i,x,w,h):
        #si la imagen es .jpg se cambia a .png y luego la añade al pdf
        if link.endswith(".jpg"):
            imagen = requests.get(link).content
            with open(f"test{i}.jpg", 'wb') as handler:
                handler.write(imagen)

            im = Image.open(f"test{i}.jpg")
            im.save(f'test{i}.png', quality=95)
            pdf.image(f"test{i}.png", x = x, y = None, w = w, h = h, type = '')
            os.remove(f"test{i}.jpg")
            os.remove(f"test{i}.png")
        else:
            pdf.image(link, x = x, y = None, w = w, h = h, type = '')



def imprimir(skills:list,archivo):

    pdf = FPDF()
    pdf.add_page()

    for num,object in enumerate(skills):
        ancho_skill=50
        alto_skill=100
        columnas=3
        xvalue=10.00125+num%columnas*(10.00125+ancho_skill)


        #Skill border
        pdf.set_font('Arial', '', 8)
        pdf.set_x(xvalue)
        pdf.cell(ancho_skill,alto_skill,txt="",border= 1, ln=0)


        #slots  
        pdf.set_x(xvalue) 
        pdf.cell(ancho_skill,4,txt=f'{object.slots}',border=0,ln=0,align ="L")


        #ap
        pdf.set_x(xvalue)
        pdf.cell(ancho_skill,4,txt=f'AP {object.ap}',border=0,ln=1,align ="R")


        #sp
        pdf.set_x(xvalue)
        pdf.cell(ancho_skill,4,txt=f'SP {object.sp}',border=0,ln=1,align ="R")


        #name
        pdf.set_font('Arial', '', 12)
        pdf.set_x(xvalue)
        pdf.cell(ancho_skill,8,txt=f'{object.name}',border=0,ln=1,align ="C")


        #imagen
        w=15
        h=15
        x=ancho_skill/2-w/2+xvalue
        poner_imagen(pdf,object.image,num,x,w,h)   


        #descripcion
        pdf.set_y(pdf.get_y()+2)
        pdf.set_x(xvalue)
        pdf.set_font('Arial', '', 8)    
        pdf.multi_cell(ancho_skill,4,txt=f'{object.description}',border= 0,align ="J")


        #requirements
        pdf.set_y(pdf.get_y()+2)
        pdf.set_x(xvalue)
        pdf.multi_cell(ancho_skill,4,txt=f'{object.requirements}',border= 0,align ="J")


        #stat
        pdf.set_x(xvalue)
        pdf.multi_cell(ancho_skill,4,txt=f'{object.stat}',border= 0,align ="J")


        #sets
        pdf.set_x(xvalue)
        pdf.multi_cell(ancho_skill,4,txt=f'{object.sets}',border= 0,align ="J")


        #cooldown
        pdf.set_x(xvalue)
        pdf.multi_cell(ancho_skill,4,txt=f'Cooldown {object.cooldown} turn(s)' ,border= 0,align ="J")


        #range
        pdf.set_x(xvalue)
        pdf.multi_cell(ancho_skill,4,txt=f'{object.range}',border= 0,align ="J")

        
        #setea la coordenada Y dependiendo de la actual
        if pdf.get_y()<10.00125+alto_skill:  #si Y esta antes del alto de la skill 
            pdf.set_y(10.00125+alto_skill-8)
        else:
            pdf.set_y(2*(10.00125+alto_skill)-8) #si Y esta igual o despues del alto de la skill

        #school and image
        pdf.set_x(xvalue)
        pdf.set_font('Arial', '', 10)
        if object.school_image:      #school and image when there is image  
            pdf.cell(ancho_skill,8,txt=f'     {object.school}',border=1,ln=0,align ="C")
            

            largo_school=pdf.get_string_width(object.school)
            w=8
            h=8
            x=ancho_skill/2-largo_school/2-w/2+xvalue
            poner_imagen(pdf,object.school_image,num,x,w,h)        
        else:                       #solo school whene there is no image
            pdf.cell(ancho_skill,8,txt=f'{object.school}',border=1,ln=1,align ="C")


        #setea la coordenada Y dependiendo de la actual
        if (num+1)%columnas==0:
            pdf.set_y(pdf.get_y()+10.00125)
        else:
            pdf.set_y(pdf.get_y()-alto_skill)



    pdf.output(archivo,'F')




