M = int(input())
S = int(input())
A = input()
B = input()
print(f"{A[::S]}_Alvin{B*M}")



"""

¡Oh no!

La computadora de Alvin ha sido hackeada, y sus contraseñas han sido secuestradas por el malvado Issem Lenoil. Como Alvin tiene un gran corazón, la contraseña que más le importa recuperar es la de su cuenta de Moodle, puesto que sus alumnos necesitan su nota del control 1.

Tras una ardua negociación con Issem, se llegó a un acuerdo: Issem revelará la forma de decodificar la contraseña, a cambio de una camiseta del Real Madrid Club de Fútbol, firmada por su ex-mejor amigo, Odlanor Onaitsirc.

Los pasos a seguir son los siguientes:

Recibirás dos enteros M y S, así como dos strings A y B.
La primera parte de la contraseña, serán los caracteres presentes cada S saltos en la string A, comenzando en la primera posición. Por ejemplo, si A es "HxOxLxA" y S=2, la cadena resultante será "hola".
La segunda parte de la contraseña, será la cadena "_Alvin".
La parte final de la contraseña, la cadena B, escrita M veces.
Cabe aclarar que, en ningún momento se escribirá un espacio (" ").

¿Puedes ayudar a Alvin?

PD: Se cree que el motivo del hackeo es que ALGUIEN (el Profe Pleités) pensó que era buena idea descargar Roblox en Minecraft comprado por Temu con el internet de la ESEN.

Entrada
La primera línea presenta un único entero M, la cantidad de veces que se debe imprimir la cadena B.
La siguiente línea, un único entero S, los saltos entre caracteres que se deben imprimir en la cadena A.
La tercera línea, contiene la cadena A.
La última línea, presenta la cadena B.
Salida
Imprime una única cadena, la contraseña decodificada.

Restricciones
A y B contienen únicamente caracteres del alfabeto inglés
Input	Output
3
2
hxoxlxa
_qhace?
hola_Alvin_qhace?_qhace?_qhace?

"""