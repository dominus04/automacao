![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
# Automação para trabalhos repetitivos

O objetivo deste código foi facilitar o envio do código ZPL (Formato de código zebra para comunicação com impressora.) para o PLC da omrom, via CX-Programmer, antigamente os programadores que eu conhecia criavam tudo manualmente, que consistia em transformar cada carctere em HEX para adicionar manualmente um bloco no CX-Programer que enviasse para um área de memória o hexcode de dois carcteres, e o programador tinha que fazer esses passos um a um manualmente, eu achei que era muito complicado ficar passando 1 a 1 e percebi que me custaria pelo menos uma semana de trabalho, então desenvolvi esse código e este processo demora certa de 10 minutos, e me dá muito menos trabalho, o primeiro passo é colocar o nome da variável que você está utilizando na memória do PLC, o segundo é digitar o nome da tela do CX-Programmer, para que o python consiga acessar a tela correta, terceiro passo é colar o código zpl da etiqueta e então apertar CTRL-D e esperar ele fazer todo o processo automaticamente.

Claro que após o programa rodar, é necessário fazer alguns ajustes manualmente na programação do PLC, porém a parte mais custosa, já fica pronta.

#Automation for repetitive jobs

The objective of this code was to facilitate the sending of the ZPL code (Zebra code format for printer communication.) to the omrom PLC, via CX-Programmer, in the past the programmers I knew created everything manually, which consisted of transforming each character into HEX to manually add a block in the CX-Programer that sends the two-character hexcode to a memory area, and the programmer had to do these steps one by one manually, I thought it was very complicated to keep going 1 to 1 and I realized that it would cost me at least a week of work, so I developed this code and this process takes about 10 minutes, and it gives me much less work, the first step is to put the name of the variable you are using in the PLC memory, the second is type the name of the CX-Programmer screen, so that python can access the correct screen, the third step is to paste the zpl code of the label and then press CTRL-D and wait for it to do the whole process automatically.

Of course, after the program runs, it is necessary to manually make some adjustments in the PLC programming, but the most expensive part is already done.
