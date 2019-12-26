import sys
import telepot
import time

compraFile = "fCompra"

def parser(mes):
    if(mes.lower() == "ad"):
        return "ad"
    if(mes.lower() == "pr"):
        return "pr"
    if(mes.lower() == "dl"):
        return "dl"
    if(mes.lower() == "cl"):
        return "cl"
    else:
        return "none"

def toAdd(element):
    print("Anadiendo " + element)
    oCompra = open(compraFile,"a")
    oCompra.write(element + "\n")
    oCompra.close()

def handle(msg):
    chat_id=msg['chat']['id']
    recCommand = msg['text']
    command = parser(recCommand.split()[0])
    print("chatid:     " + str(chat_id))
    if(len(recCommand.split()) > 1):
        element = recCommand[3:]

    ## Command Parser ##
    print('Got command: %s ' % command)

    ## Add Command ##
    if (command == 'ad'):
        if(len(recCommand.split()) <= 1):
            bot.sendMessage(chat_id, 'No se ha podido leer ningun elemento')
            return
        toAdd(element)
        bot.sendMessage(chat_id,'Anadido: ' + element)

    ## Print Command ##
    elif((command == 'pr')):
        print("Print")
        LlistaToPrint = 'Hay que comprar: \n'
        oCompra = open(compraFile,"r")
        c = 0
        for line in oCompra:
            c = c+1
            LlistaToPrint = LlistaToPrint + ' ' + str(c) + '. ' + line
        bot.sendMessage(chat_id, LlistaToPrint)
        oCompra.close()

    ## Clear Command ##
    elif(command == 'cl'):
        open(compraFile, "w").close()
        bot.sendMessage(chat_id, 'La lista se ha borrado correctamente')

    ## Delete Command ##
    elif(command == 'dl'):
        newCompraArray = []
        oCompra = open(compraFile,"r")
        if(len(recCommand.split()) <= 1):
            bot.sendMessage(chat_id, 'No se ha borrado ningun elemento')
            return
        try:
            flagElement = 0
            elementoBorrado = ''
            for line in oCompra:
                if(line.find(element) == -1):
                    newCompraArray.append(line)
                else:
                    flagElement = 1
                    elementoBorrado = line
            oCompra.close()
            oCompra = open(compraFile,"w")
            for i in range(len(newCompraArray)):
                oCompra.write(newCompraArray[i])
            del newCompraArray[:]
            if(flagElement == 0):
                bot.sendMessage(chat_id, 'Elemento no encontrado')
            else:
                bot.sendMessage(chat_id,'Se ha borrado: ' + elementoBorrado)
        except ValueError:
            bot.sendMessage(chat_id, 'Elemento no encontrado')
            return
    else:
        bot.sendMessage(chat_id, 'Unknown command')

bot = telepot.Bot(' Añadir aqui el Token')
bot.message_loop(handle)
print 'I am listening ...'
print(bot.getMe())

while 1:
    #Should never reach here
    time.sleep(10)