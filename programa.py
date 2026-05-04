#-------------------------------------------------------------------
#Programa que solicita nombre y edad y muestra mensaje de bienvenida
#Autor: Amelia Bozano <abozano@est.ups.du.ec>
#Fecha: 04/05/2026
#-------------------------------------------------------------------

def main ():
    nombre = input("Cuál es tu nombre:")
    edad = int(input("Cuántos años tienes: "))
    print(f"Hola, {nombre}, sientete bienvenid@")
    print(f"El usuario tiene {edad} años")
    print("-----BIENVENID@ AL MUNDO DE HELLO KITTY-----")
    ascii_art = r"""
      .-. __ _ .-.
      |  `  / \  |
      /     '.()--\
     |         '._/
    _| O   _   O |_
    =\    '-'    /=
      '-._____.-'
      /`/\___/\`\
     /\/o     o\/\
    (_|         |_)
 jgs  |____,____|
      (____|____)
"""

    print(ascii_art)
    print("----------------------------------------")

if __name__ == "__main__":  #indica que si el nombre es main se debe ejecutar
    main()