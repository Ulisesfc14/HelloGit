print("Bienbenido al parque de diversiones, por favor elija una atracción escribiendo el numero correspondiente a continuacion" )
juegos = int(input("montaña rusa (1) o viaje en tren (2)"))
if(juegos == 1):
	estatura = float(input("Ingrese su estatura"))
	if (estatura >= 1.61):
		print("Diviertete en la montaña rusa")
	else:
		print("Estatura no permitida")
elif(juegos == 2):
	print("Diviertete en el tren")
print("fin programa")