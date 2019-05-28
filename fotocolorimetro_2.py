from tkinter import *
from tkinter.ttk import Progressbar
import time
#from tkinter import ttk, font

#------------------------------------

class programa:
	def __init__(self):
		self.window = Tk()
		self.window.title('')
		self.window.geometry('360x530+0+0')
		self.window.resizable(width=False, height=False)

		self.salida_0()
		self.salida_1()
		self.salida_2()
		self.boton_0()

		self.window.mainloop()

	#------------ Ventanas -------------------------------
	
	def ventana_1(self):
		self.window1 = Toplevel()
		self.window1.title('Fotocolorímetro')
		self.window1.geometry('360x530+167+50')
		self.window1.resizable(width=False, height=False)
		self.window1.transient([self.window])

		self.boton_1()

		self.window1.mainloop()

	#----------- Entradas -------------------------------------
	
	def entrada_0(self):
		txt = Entry(self.window1, width=10)
		#txt.grid(column=0, row=0)
		txt.pack()
		txt.config(font=('Arial', 9))
		txt.focus()

	#------------ Salidas ------------------------------------

	def salida_0(self):
		lbl = Label(self.window, text=('Fotocolorímetro'), justify="center")
		lbl.pack()
		#lbl.grid(column=0, row=0)
		lbl.config(padx=0, pady=30, font=('Arial', 16,'bold'))

	def salida_1(self):
		lbl = Label(self.window, text=('INSTRUCCIONES:\n\nAntes de comenzar con la prueba, verifique\nque el recipiente esté completamente limpio\ny bien posicionado.'), justify="left")
		lbl.pack()
		#lbl.grid(column=0, row=1)
		lbl.config(padx=0, pady=0, font=('Arial', 9))

	def salida_2(self):
		lbl = Label(self.window, text=('Para comenzar prueba presione "Aceptar".'), justify="left")
		lbl.pack()
		#lbl.grid(column=0, row=2)
		lbl.config(padx=0, pady=30, font=('Arial', 9, 'bold'))

	#----------- Botones --------------------------------

	def boton_0(self):
		
		def click_1():
			lbl.configure(text=txt.get())

		btn = Button(self.window, text='Aceptar', command=self.ventana_1, justify='center')
		btn.pack()
		#btn.grid(column=0, row=3)
		btn.config(bd=2, padx=5, pady=1, font=('Arial', 10))

	def boton_1(self):

		lbl = Label(self.window1, text=('Prueba de Fotocolorimetría'), justify="center")
		lbl.pack()
		#lbl.grid(column=0, row=0)
		lbl.config(padx=0, pady=20, font=('Arial', 12, 'bold'))

		lbl1 = Label(self.window1, text=('Ingrese código de muestra\n(Numérico)'), justify="center")
		lbl1.pack()
		#lbl.grid(column=0, row=0)
		lbl1.config(padx=0, pady=20, font=('Arial', 9))

		txt = Entry(self.window1, width=30)
		#txt.grid(column=0, row=0)
		txt.pack()
		txt.config(font=('Arial', 9))
		txt.focus()

		lbl2 = Label(self.window1, text=('Ingrese descripción de la muestra\n(Nombre, color, característica, etc.)'), justify="center")
		lbl2.pack()
		#lbl.grid(column=0, row=0)
		lbl2.config(padx=0, pady=20, font=('Arial', 9))

		txt1 = Entry(self.window1, width=30)
		#txt.grid(column=0, row=0)
		txt1.pack()
		txt1.config(font=('Arial', 9))

		lbl3 = Label(self.window1, text=('Para confirmar datos presione "Aceptar"'), justify="center")
		lbl3.pack()
		#lbl.grid(column=0, row=0)
		lbl3.config(padx=0, pady=20, font=('Arial', 9, 'bold'))


		def click_1():
			lbl.configure(text=txt.get())

		btn = Button(self.window1, text='Aceptar', command=click_1, justify='center')
		btn.pack()
		#btn.grid(column=0, row=3)
		btn.config(bd=2, padx=5, pady=1, font=('Arial', 10))

	#----------- Opciones ----------------------------

	def opcion_0(self):
		rad = Radiobutton(self.window, text='texto', value=1, command=d)
		rad.pack()
		#rad.grid(column=0, row=0)
		rad.config(padx=10, pady=10, font=('Arial', 16))

	#----------- Contenedores ---------------------------------

	def contenedor_0(self):
		frame = Frame()
		frame.pack()
		#frame.grid(column=0, row=0)
		frame.config(bd=1, relief='sunken', width=370, height=50)

		self.salida_0()

	#----------- Textos ----------------------------------------

	def texto_0(self):
		text = Text(self.window)
		text.insert(INSERT, '\n             Instrucciones\n\n    Antes de comenzar con la prueba de       fotocolorimetría, verifique que el       *** esté completamente limpio y          bien posicionado.\n\n    Para comenzar presione "Aceptar"')
		text.pack()
		#text.grid(column=1, row=2)

#-------- Menú ----------------------------------------------

def main():
	a = programa()
	return 0

#----------------------------------------

if __name__ == '__main__':
	main()




