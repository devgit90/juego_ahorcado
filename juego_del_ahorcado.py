
import random


def obtener_palabra_secreta()-> str:
    palabras = ['python','java','css','django','perl','angular','react', 'typescript']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado=''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas =[]
    intentos=7
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta,letras_adivinadas), "La cantidad de letras de la spalabras es: ",len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce letra ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor  introduzca una letra válida")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien has asertado, la letra {adivinanza} está presente en la palabra")
            else:
                intentos -= 1
                print(f"Lo siento mucho la terla {adivinanza} no está presente en la palabra")
                print(f"Te quedan {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Felicitaciones has ganado, la palabra completa es {palabra_secreta}")

    if intentos == 0:
        print(f"Lo sentimos mucho, se han acabado los intentos. La palabra secreta era {palabra_secreta}")

juego_ahorcado()
