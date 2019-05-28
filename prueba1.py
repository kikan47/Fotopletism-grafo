import os
import serial
import time

def menu():
	os.system('cls')
	print('\n     MENU\n')
	print('**************')
	print('1 - Rojo')
	print('\n2 - Verde')
	print('\n3 - Azul')
	print('\n9 - salir')
	print('**************')

def arduino1():
	arduino = serial.Serial('COM13',9600)
	time.sleep(2)

	arduino.write(b'r')

	arduino.close()

	bucle()

def arduino2():
	arduino = serial.Serial('COM13',9600)
	time.sleep(2)

	arduino.write(b'v')

	arduino.close()

	bucle()

def arduino3():
	arduino = serial.Serial('COM13',9600)
	time.sleep(2)

	arduino.write(b'a')

	arduino.close()

	bucle()

def bucle():
	while True:
		menu()
		opcionMenu = input('\ninserta una opción: ')

		if opcionMenu=='1':
			arduino1()

		elif opcionMenu=='2':
			arduino2()

		elif opcionMenu=='3':
			arduino3()

		elif opcionMenu=='9':
			break

		else:
			print('')
			input('\nNo has pulsado ninguna opción correcta... pulsa una tecla para continuar')
			bucle()

bucle()