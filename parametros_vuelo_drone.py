# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:11:49 2021

@author: edwin
"""


import tkinter as tk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry ("1110x700")
ventana.config(bg="turquoise")

# PRIMERA FILA

espacio = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio.grid (row = 0, column = 0)

txt1 = tk.Label(ventana, text="          Distancia Focal (mm)=", bg="turquoise", fg="black")
txt1.grid (row = 1, column = 0)

campo1 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo1.grid (row = 1, column = 1)

txt2 = tk.Label(ventana, text="      Ancho de la imagen (Pixel)=", bg="turquoise", fg="black")
txt2.grid (row = 1, column = 2)

campo2 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo2.grid (row = 1, column = 3)

txt3 = tk.Label(ventana, text="      Alto de la imagen (Pixel)=", bg="turquoise", fg="black")
txt3.grid (row = 1, column = 4)

campo3 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo3.grid (row = 1, column = 5)

#SEGUNDA FILA

espacio1 = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio1.grid (row = 2, column = 0)

txt4 = tk.Label(ventana, text="          Ancho del sensor (mm)=", bg="turquoise", fg="black")
txt4.grid (row = 3, column = 0)

campo4 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo4.grid (row = 3, column = 1)

txt5 = tk.Label(ventana, text="      Alto del sensor (mm)=", bg="turquoise", fg="black")
txt5.grid (row = 3, column = 2)

campo5 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo5.grid (row = 3, column = 3)

txt6 = tk.Label(ventana, text="      Altura del vuelo (m)=", bg="turquoise", fg="black")
txt6.grid (row = 3, column = 4)

campo6 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo6.grid (row = 3, column = 5)

#TERCERA FILA

espacio2 = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio2.grid (row = 4, column = 0)

txt7 = tk.Label(ventana, text="          Solape Longitudinal (%)=", bg="turquoise", fg="black")
txt7.grid (row = 5, column = 0)

campo7 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo7.grid (row = 5, column = 1)

txt8 = tk.Label(ventana, text="      Solape Transversal (%)=", bg="turquoise", fg="black")
txt8.grid (row = 5, column = 2)

campo8 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo8.grid (row = 5, column = 3)

txt9 = tk.Label(ventana, text="      Largo de la parcela (m)=", bg="turquoise", fg="black")
txt9.grid (row = 5, column = 4)

campo9 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo9.grid (row = 5, column = 5)

#CUARTA FILA

espacio3 = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio3.grid (row = 6, column = 0)

txt10 = tk.Label(ventana, text="          Ancho de la parcela (m)=", bg="turquoise", fg="black")
txt10.grid (row = 7, column = 1)

campo10 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo10.grid (row = 7, column = 2)

txt11 = tk.Label(ventana, text="      Velocidad del vuelo (m/s)=", bg="turquoise", fg="black")
txt11.grid (row = 7, column = 3)

campo11 = tk.Entry(ventana, font = "Arial 12", justify = "center")
campo11.grid (row = 7, column = 4)

espacio3 = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio3.grid (row = 8, column = 0)


espacio3 = tk.Label(ventana, text="      ", bg="turquoise", fg="turquoise")
espacio3.grid (row = 10, column = 0)

#RESULTADOS
textResult = tk.Text(ventana)
textResult.grid(row = 11, column = 0, columnspan = 6)

#VIENE LO BUENO PAPA

def resultados():
    textResult.delete(1.0, tk.END)
    f_cam = float(campo1.get())
    anch_img = int(campo2.get())
    alt_img = int(campo3.get())
    anch_sensor = float(campo4.get())
    alt_sensor = float(campo5.get())
    RSI = anch_sensor/anch_img
    h_vuelo = float(campo6.get())
    s_long = float(campo7.get())
    s_trans = float(campo8.get())
    larg_parce = float(campo9.get())
    anch_parce = float(campo10.get())
    vel_vuelo = float(campo11.get())
    
    
    #GSD
    GSD = (((h_vuelo * 100 )/ (f_cam)) * RSI)
    textResult.insert(tk.END, f"GSD = {GSD}cm/pixel\n\n")
    
    #ESCALA DEL VUELO
    esc_vuelo = 1/((f_cam/1000)/h_vuelo)
    textResult.insert(tk.END, f"Escala de vuelo = {esc_vuelo}\n\n")
    
    #ANCHO DE LA IMAGEN
    AIMGTomada = (anch_sensor*esc_vuelo)/1000
    textResult.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {AIMGTomada}m\n\n")
    
    #ALTO DE LA IMAGEN
    AIMGTomada = (alt_sensor*esc_vuelo)/1000
    textResult.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {AIMGTomada}m\n\n")
    
    #BASE AEREA
    base_aer = (((anch_img * GSD )/100)* (1-(s_long/100)))
    textResult.insert(tk.END, f"Base Aerea = {base_aer}\n\n")
    
    #DISTANCIA ENTRE PASADAS
    DxPasada = (((alt_img * GSD )/100)) * (1-(s_trans/100))
    textResult.insert(tk.END, f"Distancia entre Pasadas = {DxPasada}m\n\n")
    
    #TIEMPO ENTRE FOTOS Y VELOCIDAD DE VUELO
    t_fotos = base_aer/vel_vuelo
    vel_vuelo= base_aer/t_fotos
    textResult.insert(tk.END, f"Tiempo entre fotos = {t_fotos}s\n\n")
    textResult.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo}m/s\n\n")
    
    #NUMERO DE PASADAS
    num_pasadas = anch_parce/DxPasada
    c_pasadas = num_pasadas - int(num_pasadas)
    if c_pasadas > 0 and c_pasadas < 1:
        c_pasadas = 1 - c_pasadas
        num_pasadas = num_pasadas + c_pasadas
        num_pasadas = int(num_pasadas)
    textResult.insert(tk.END, f"Numero de Pasadas = {num_pasadas}\n\n")
    
    #NUMERO DE FOTOS POR PASADA 
    num_fotos = (larg_parce/base_aer)+1
    c_fotos = num_fotos - int(num_fotos)
    if c_fotos >0 and c_fotos <1 :
        c_fotos = 1-c_fotos
        num_fotos = num_fotos + c_fotos
        num_fotos = int(num_fotos)
    textResult.insert(tk.END, f"Numero de Fotos por Pasada = {num_fotos}\n\n")
    
    #NUMERO DE FOTOS POR VUELO 
    num_f_v= num_fotos*num_pasadas
    c_fv = num_f_v - int(num_f_v)
    if c_fv >0 and c_fv<1 :
        c_fv = 1-c_fv
        num_f_v = num_f_v + c_fv
        num_f_v = int(num_f_v)
    textResult.insert(tk.END, f"Numero de Fotos por Vuelo = {num_f_v}\n\n")
    
    #DISTANCIA DE VUELO
    dist_vuelo = (num_pasadas*larg_parce)+anch_parce
    textResult.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo}m\n\n")
    
    #DURACION DEL VUELO 
    t_vuelo= ((num_f_v * t_fotos)/60)
    textResult.insert(tk.END, f"Duracion del Vuelo = {t_vuelo}min")
    
    popup_showinfo()
    #VENTANA EMERGENTE
def popup_showinfo():
    message ="¡Listo!"
    showinfo(message)
    
#SE PRENDIÓ ESTA PAPADA (BOTÓN DE INICIO)
incheboton = tk.Button(text = "CALCULAR", font= 'Helvetica 10', command = resultados)
incheboton.grid(row = 9, column = 2, columnspan = 2)

#TITULO DE LA VENTANA
ventana.title("Calculadora de parametros de vuelo de drone")

ventana.mainloop()