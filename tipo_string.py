simple_string = 'Hola mundo'
doble_string = "Python es genial"

texto_grande = '''Parrafo de texto'''
texto_grande = """Texto grande"""

texto1 = "Hola"
texto2 = "Mundo"

nuevo_texto = texto1 + " " + texto2
multiple_texto = texto1 *3

print(nuevo_texto)
print("Hola" * 5)

texto = """ "Pyhton" es genial
 La luna en ingles es Moon's"""

print(texto)

nombre = "Juan"
edad = 30
talla = 1.75

print(f'Hola, me llamo {nombre}, tengo {edad}, y mido, {talla}, metros')

mensaje = "Hola, me llamo %s , tengo %d y mido %.2f metros" % (nombre, edad, talla)

print(mensaje)

mensaje = "Hola, me llamo {} , tengo {} y mido {:.2f} metros".format(nombre, edad, talla)

print(mensaje)

