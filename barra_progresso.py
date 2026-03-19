#first try
from time import sleep
i = 0
while i <= 100:
    print("\r" + chr(9608) * i + " " + str(i), end="")
    sleep(.5)
    i += 1

from time import sleep
import os
print("\033[?25l") #some com o cursor
i = 0
tam, _ = os.get_terminal_size() #vai apenas até o final da tela do terminal
while i <= tam:
    print(chr(9608) * i + " " + str(i))
    sleep(.15) #tempo de demora da barra (p/ passar p/ o prx)
    os.system("cls") #limpar a tela e começar uma nova barra
    i += 1

#cls só funciona no Windows. Para outros OS são outros comandos