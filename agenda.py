import sys
comandos = sys.argv

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)

#>>>SEM TAREFA:
#(Confere se são um número de 1 a 9, se sim retorna True)

def soDigitos(string):
  for x in string :
    if x < '0' or x > '9' :
      return False
  return True

#>>> TAREFA 3:
#(Para verificar se a hora é valida, a função primeiro verifica se o valor digitado é diferente de 4 caracteres, se sim, a função finaliza, se não, a função continua para as próximas etapas
# no qual verifica se os dois primeiros digitos vão de 0 a 23(hora) e o dois ultimos digitos se vão de 0 a 59(minutos), se sim, retorna True)

def horaValida(horaMinuto):
  if len(horaMinuto) != 4:
    return False
  hora = []
  for x in horaMinuto:
    hora.append(x)
  for x in hora:
    if soDigitos(x) == False:
      return False
  x = [int(hora[0]+hora[1]), int(hora[2]+hora[3])]
  if(x[0] < 0 or x[0]> 23):
    return False
  else:
    if (x[0] >= 0 and x[0] <= 23) and (x[1] < 0 or x[1] > 59):
      return False
    elif (x[0] >= 0 and x[0] <= 23) and (x[1] >= 0 and x[1] <= 59):
      return True
    
#>>> TAREFA 4:
#(Para validar a data, primeiro verifica se o valor digitado é diferente de 8 caracteres, se sim, retorna false, se não prossegue para as próximas etapas;
#adiciona dia,mes,anos em cada tupla e verifica se ele atendem as regras de dia(1-31),mes(1-12),ano(1-n))


"""
  - Meses que terminam com 31,30 e 28.
  1 jan = 31
  2 fev = 28
  3 mar = 31
  4 abril = 30
  5 maio = 31
  6 junho = 30
  7 julho = 31
  8 agosto = 31
  9 setembro = 30
  10 outubro = 31
  11 novembro = 30
  12 dezembro = 31
"""

def dataValida(string):
  if len(string) != 8:
    return False
  data = []
  for x in string:
    data.append((x))
  for x in data:
    if soDigitos(x) == False:
      return False
  x = [int(data[0]+data[1]), int(data[2]+data[3]), int(data[4]+data[5]+data[6]+data[7])]
  #Confere se a data entra nas regras:
  #listaata = [(14),(01),(1999)]
  if (x[0] < 1 or x[0] > 31):
      return False
  else:
    if (x[0] >= 1 and x[0] <= 31) and (x[1] < 1 or x[1] > 12):
      return False
    else:
      if (x[0] >= 1 and x[0] <= 31) and (x[1] == 1 or x[1] == 3 or x[1] == 5 or x[1] == 7 or x[1] == 8 or x[1] == 10 or x[1] == 12):
        return True
      elif (x[0] >= 1 and x[0] <= 28) and (x[1] == 2):
        return True
      elif (x[0] >= 1 and x[0] <= 30) and (x[1] == 4 or x[1] == 6 or x[1] == 9 or x[1] == 11):
        return True
      else:
        return False

#>>> TAREFA 5:
#(Para validar o projeto verifica se o primeiro caractere é "+" e se existe exatamente 2 caracteres)
def projetoValido(string):
  if len(string) < 2:
    return False
  elif string[0] == "+":
    return True
  return False

#>>> TAREFA 6:
#(Para validar o contexto verifica se o primeiro caractere é "@" e se existe exatamente 2 caracteres)
def contextoValido(string):
  if len(string) < 2:
    return False
  elif string[0] == "@":
    return True
  return False

#>>> TAREFA 7:
#(Para validar a prioridade verifica se o primeiro e terceiro caractere é "(" e ")" respectivamente e se existe exatamente 3 caracteres, além disso se está entre A-Z)
def prioridadeValida(string):
  if len(string) < 3:
    return False
  if string[0] != "(" or string[2] != ")":
    return False
  if (string[1] >= "A" and string[2] <= "Z") or (string[1] >= "a" and string[2] <= "z"):
    return True
  return False

#>>> SEMTAREFA:
#Função para checar se a descrição é realmente uma descrição!

def descricaoValida(string):
  if dataValida(string) == True:
    return False
  elif horaValida(string) == True:
    return False
  elif projetoValido(string) == True:
    return False
  elif contextoValido(string) == True:
    return False
  elif prioridadeValida(string) == True:
    return False
  return True

#___________________________________________________________________________________________ OUTROS CÓDIGOS ___________________________________________________________________________________________________________________

#Essas funções utilizam as funções de validez(horaValida, dataValida, etc) e retorna true apenas o primeiro elemento de cada item, caso o usuário digite por exemplo duas datas, ele retornará apenas a primeira data!
def data(lista):
  for x in lista:
    if dataValida(x) == True:
      return x
  return False

def hora(lista):
  for x in lista:
    if horaValida(x) == True:
      return x
  return False

def projeto(lista):
  for x in lista:
    if projetoValido(x) == True:
      return x
  return False

def prioridade(lista):
  for x in lista:
    if prioridadeValida(x) == True:
      return x
  return False

def contexto(lista):
  for x in lista:
    if contextoValido(x) == True:
      return x
  return False

#PARA VERIFICAR A DESCRIÇÃO PRIMEIRO É NECESSÁRIO PEGAR UM INDEX PARA QUE
def index(lista,string):
  x = 0
  while x < len(lista):
    if lista[x] == string:
      return x
    x += 1
  return False

#>>> OBSERVAÇÃO: O igual a string, serve para comparar nas funções feitas acima já que elas retornam falso ou string.
#>>> A (FUNÇÃO DESCRIÇÃO) ABAIXO SE UTILIZA DA (FUNÇÃO INDEX) PARA PEGAR TODOS OS ELEMENTOS QUE NÃO SÃO DESCRIÇÃO(Data, Hora, Projeto, Prioridade, Contexto) E REMOVER DA LISTA.

def descricao(lista):
  flagstring = ""
  listaFlag = lista[:] # [:] — CRIA COPIA DA LISTA, PARA NÃO ALTERAR A LISTA ORIGINAL.
  if type(data(listaFlag)) == str:
    listaFlag.pop(index(listaFlag,data(listaFlag)))
  if type(hora(listaFlag)) == str:
    listaFlag.pop(index(listaFlag,hora(listaFlag)))
  if type(projeto(listaFlag)) == str:
    listaFlag.pop(index(listaFlag,projeto(listaFlag)))
  if type(prioridade(listaFlag)) == str:
    listaFlag.pop(index(listaFlag,prioridade(listaFlag)))
  if type(contexto(listaFlag)) == str:
    listaFlag.pop(index(listaFlag,contexto(listaFlag)))
  #DEPOIS QUE VERIFICAR TODAS AS FUNÇÕES, ADICIONA APENAS A DESCRIÇÃO A FLAG STRING:
  for palavra in listaFlag:
    flagstring += palavra 
    flagstring += ' '
    #Adiciona palavra>espaço>palavra>espaço.
  return flagstring
#____________________________________________________________________________________________________________________________________________________________________________________________

#>>> TAREFA 8:
#(Organiza a linha de modo que fique: (DESC, (DATA, HORA, PRIORIDADE, CONTEXTO, PROJETO))).

def organizar(linha):
  itens = []
  dataW = '' 
  horaW = ''
  prioridadeW = ''
  contextoW = ''
  projetoW = ''
  linha = linha.strip() #RETIRA OS ESPAÇOS DO COMEÇO E DO FINAL.
  tokens = linha.split() #QUEBRA EM LISTA DE PALAVRAS. ["DGDFGD","GJGHJGHJ","FGJHFGHJFGJH"]
  descricaoW = descricao(tokens)
  #Para podermos organizar o arquivo primeiro pegamos cada elemento(Data, Hora, Prioridade, Contexto, Projeto) 
  if type(data(tokens)) == str:
    dataW += data(tokens)
  if type(hora(tokens)) == str:
    horaW += hora(tokens)
  if type(prioridade(tokens)) == str:
    prioridadeW += prioridade(tokens)
  if type(contexto(tokens)) == str:
    contextoW += contexto(tokens)
  if type(projeto(tokens)) == str:
    projetoW += projeto(tokens)
  #Adiciona a descrição a lista e informações
  itens = (descricaoW.strip(),) #Tira os espaços da descrição e coloca a "," devido ser tupla, adicionando em itens.
  
  # Um problema que pode acontecer é que caso o usuário não digite uma data ou uma hora por exemplo, o print ficara vazio como no exemplo abaixo
  # Verificando se o arquivo está vazio, exemplo = ('eu quero taca fogo nos homofobicos amanha 14012015', ('14012020', '', '', '', ''))
  itensFlag = ()
  if dataW != "":
    itensFlag += dataW,
  if horaW != "":
    itensFlag += horaW,
  if prioridadeW != "":
    itensFlag += prioridadeW,
  if contextoW != "":
    itensFlag += contextoW,
  if projetoW != "":
    itensFlag += projetoW,
  itens += itensFlag,
  return itens

#>>> TAREFA 9:
#(A função adicionar tem como foco em primeiro lugar ter uma descrição, opcionalmente os outros elementos).

def adicionar(tupla):
  arquivo = open("todo.txt", "r") #"r" = ler o arquivo.
  palavra = arquivo.readlines() #Quebra cada linha do arquivo em uma lista com todas as palavras

  #O motivo de ter criado dois IF's.
  #(Data, Hora e Prioridade vem primeiro) e depois (Descrição, contexto e Projeto).

  if len(tupla) == 2:
    for x in tupla[1]:
      if dataValida(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif horaValida(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif prioridadeValida(x) == True: 
        palavra.append(x)
        palavra.append(' ')
  palavra.append(tupla[0])
  palavra.append(' ')
  if len(tupla) == 2: 
    for x in tupla[1]:
      if contextoValido(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif projetoValido(x) == True:
        palavra.append(x)
  palavra.append("\n")
  if palavra[len(palavra) -1] == ' ':
    palavra.pop(len(palavra) -1)
  arquivo = open("todo.txt","w")
  arquivo.writelines(palavra) #Aqui, o programa de fato pega tudo que foi adicionado em palavras e adiciona ao arquivo.
  arquivo.close
  return



#>>> TAREFA 11:
#(A função vai listar todos os arquivos pegando em primeiro lugar a prioridade, depois data e por ultimo hora, caso não tenha nenhum, ficaram por ultimo.)


#OBS: Para começarmos a ordernar precisamos separar todos o que tem prioridades primeiro para depois utilizarmos um bubblesort em data/hora e assim ficar ordenado.
#1: Reune todas as prioridades dentro de uma tupla.
def todasPrioridades():
  arquivo = open("todo.txt","r")
  tuplasOrganizadas = ()
  for x in arquivo:
    tuplasOrganizadas += organizar(x),
  lista = list(tuplasOrganizadas) #Aqui retornar uma lista com várias tuplas organizadas.
  lista1 = []
  x = 0
  while x < len(lista):
    contato = lista[x][1]
    w = 0
    while w < len(contato):
      if prioridadeValida(contato[w]) == True: #Confere se cada elemento dentro da tupla [exemplo: ('(A)', '+Service')] tem uma prioridade, se sim, adiciona a lista.
        lista1.append(lista[x])
      w+=1
    x+=1
  arquivo.close()
  return lista1
""
#2: Fazendo um bubblesort na lista com tuplas que tem prioridades.
def ordenarPrioridade():
  listaOrdenadaPrioridade = todasPrioridades()
  x = 0
  while x < len(listaOrdenadaPrioridade):
    w = 0
    while w < len(listaOrdenadaPrioridade)-1:
      if prioridade(listaOrdenadaPrioridade[w][1])[1] > prioridade(listaOrdenadaPrioridade[w+1][1])[1]:
        flag = listaOrdenadaPrioridade[w]
        listaOrdenadaPrioridade[w] = listaOrdenadaPrioridade[w+1]
        listaOrdenadaPrioridade[w+1] = flag
      w+=1
    x+=1
  return listaOrdenadaPrioridade

#3: Agora criamos uma função para todo o resto que não tem prioridade.
def todosSemSerPrioridades():
  arquivo = open("todo.txt","r")
  lista = []
  for linha in arquivo:
    linhaFlag = organizar(linha)
    if prioridade(linhaFlag[1]) == False:
      lista.append(linhaFlag)
  arquivo.close()
  return lista

#4: Nessa função juntamos tudo em uma só lista de tuplas e transforma isso em lista de listas, isso vai ajudar futuramente.
def transformarEmLista():
  listaComTuplas = ordenarPrioridade() + todosSemSerPrioridades() #Junta lista ordenada com prioridades + todos os outros.
  listaTotal = []
  for x in listaComTuplas:
    x = list(x)
    x[1] = list(x[1])
    listaTotal.append(x)   
  return listaTotal

#5: Ambas funções embaixo vão servir para um bubblesort entre data/hora.
#(Se invertermos duas datas ou horas, você verá quem é o maior ou menor, exemplo: 14011999-15011999 (invertido: 19990114-19990115))
def inverterData(data):
  inverterData = data[4:] + data[2:4] + data[:2]
  return inverterData

def inverterHora(hora):
  inverterHora = hora[2:] + hora[:2]
  return inverterHora

#6: Essa função irá listar de fato todo o arquivo e irá utilizar todas as outras funções anteriores:
def listar():
  lista = transformarEmLista()
  x = 0
  while x < len(lista):
    w = 0
    while w < len(lista)-1:
      #Primeiro vamos checar sem a prioridade de uma lista e outra lista retorna uma string.
      if (type(prioridade(lista[w][1])) == str) and (type(prioridade(lista[w+1][1])) == str):
        if prioridade(lista[w][1]) == prioridade(lista[w+1][1]):
          if type(data(lista[w][1])) == str and type(data(lista[w+1][1])) == str:
            #Se a prioridade de duas listas forem iguais e a primeira data for MAIOR que a outra, vamos utilizar um bubblesort:
            if inverterData(data(lista[w][1])) > inverterData(data(lista[w+1][1])):
              flag = lista[w]
              lista[w] = lista[w+1]
              lista[w+1] = flag
            #Se a prioridade de duas listas forem iguais e a primeira data for IGUAL que a outra, vamos checar agora a hora:
            elif inverterData(data(lista[w][1])) == inverterData(data(lista[w+1][1])):
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                #Se a prioridade de duas listas forem iguais e a data das duas listas também forem iguais, e a primeira hora for MAIOR que a segunda hora, vamos utilizar um bubblesort:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
          #Caso o primeiro não seja uma data e a segunda seja uma data, pegamos a segunda lista e jogamos para frente, fazendo um bubblesort:
          elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) == str:
            flag = lista[w]
            lista[w] = lista[w+1]
            lista[w+1] = flag
      elif (type(prioridade(lista[w][1])) != str) and (type(prioridade(lista[w+1][1])) != str):
        if type(data(lista[w][1])) == str and type(data(lista[w+1][1])) == str:
            if inverterData(data(lista[w][1])) > inverterData(data(lista[w+1][1])):
              flag = lista[w]
              lista[w] = lista[w+1]
              lista[w+1] = flag
            elif inverterData(data(lista[w][1])) == inverterData(data(lista[w+1][1])):
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
                elif type(hora(lista[w][1])) != str and type(hora(lista[w+1][1])) == str:
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag 
        elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) == str:
          flag = lista[w]
          lista[w] = lista[w+1]
          lista[w+1] = flag
        elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) != str:
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
              elif type(hora(lista[w][1])) != str and type(hora(lista[w+1][1])) == str:
                flag = lista[w]
                lista[w] = lista[w+1]
                lista[w+1] = flag 
      w+=1
    x+=1
  linha = 0
  while linha < len(lista):
    print((linha +1), printarOrganizado(lista[linha]))
    linha += 1
  return

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  return cor + texto + RESET
  
#(Essa função pega a função LISTAR e printa para o usuário organizado por - (DDMMAAAA HHMM (PRI) DESC @CTX +PROJ))
def printarOrganizado(lista):
  flag = ''
  if type(prioridade(lista[1])) == str:
    flag += (prioridade(lista[1])) + ' '
  if type(data(lista[1])) == str:
    flag += (data(lista[1])[:2]) + "/" + (data(lista[1])[2:4]) + "/" + (data(lista[1])[4:]) + " "
  if type(hora(lista[1])) == str:
    flag += (hora(lista[1])[:2]) + ":" + (hora(lista[1])[2:])
  flag += " " + lista[0] + " "
  if type(contexto(lista[1])) == str:
    flag += (contexto(lista[1])) + " "
  if type(projeto(lista[1])) == str:
    flag += (projeto(lista[1]))

  if type(prioridade(lista[1])) == str:
    if prioridade(lista[1]) == "(A)":
      flag = printCores(flag,YELLOW)
    elif prioridade(lista[1]) == "(B)":
      flag = printCores(flag,RED)
    elif prioridade(lista[1]) == "(C)":
      flag = printCores(flag,BLUE)
    elif prioridade(lista[1]) == "(D)":
      flag = printCores(flag,GREEN)
  return flag.strip()


#(Para removermos, precisamos primeiro de um index e por isso repetimos grande parte do listar para fazermos isso.)
def auxiliarRemover():
  lista = transformarEmLista()
  x = 0
  while x < len(lista):
    w = 0
    while w < len(lista)-1:
      if (type(prioridade(lista[w][1])) == str) and (type(prioridade(lista[w+1][1])) == str):
        if prioridade(lista[w][1]) == prioridade(lista[w+1][1]):
          if type(data(lista[w][1])) == str and type(data(lista[w+1][1])) == str:
            if inverterData(data(lista[w][1])) > inverterData(data(lista[w+1][1])):
              flag = lista[w]
              lista[w] = lista[w+1]
              lista[w+1] = flag
            elif inverterData(data(lista[w][1])) == inverterData(data(lista[w+1][1])):
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
          elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) == str:
            flag = lista[w]
            lista[w] = lista[w+1]
            lista[w+1] = flag
      elif (type(prioridade(lista[w][1])) != str) and (type(prioridade(lista[w+1][1])) != str):
        if type(data(lista[w][1])) == str and type(data(lista[w+1][1])) == str:
            if inverterData(data(lista[w][1])) > inverterData(data(lista[w+1][1])):
              flag = lista[w]
              lista[w] = lista[w+1]
              lista[w+1] = flag
            elif inverterData(data(lista[w][1])) == inverterData(data(lista[w+1][1])):
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
                elif type(hora(lista[w][1])) != str and type(hora(lista[w+1][1])) == str:
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag 
        elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) == str:
          flag = lista[w]
          lista[w] = lista[w+1]
          lista[w+1] = flag
        elif type(data(lista[w][1])) != str and type(data(lista[w+1][1])) != str:
              if type(hora(lista[w][1])) == str and type(hora(lista[w+1][1])) == str:
                if inverterHora(hora(lista[w][1])) > inverterHora(hora(lista[w+1][1])):
                  flag = lista[w]
                  lista[w] = lista[w+1]
                  lista[w+1] = flag
              elif type(hora(lista[w][1])) != str and type(hora(lista[w+1][1])) == str:
                flag = lista[w]
                lista[w] = lista[w+1]
                lista[w+1] = flag 
      w+=1
    x+=1
  listaFinal = []
  linha = 0
  while linha < len(lista):
    listaFlag = []
    listaFlag.append(linha+1) #Numero
    listaFlag.append(lista[linha]) #Lista (Descrição, prioridade. etc)
    listaFinal.append(listaFlag) #Numero + lista
    linha += 1
  return listaFinal

#>>> TAREFA 16:
#(Essa função de fato vai remover o elemento do arquivo).
def remover(numero):
  lista = auxiliarRemover()
  copia = lista[:]
  for x in lista:
    if str(x[0]) == numero:
      lista.pop(int(numero)-1)
  if lista == copia:
    print("Não existe na lista!")
    return
  arquivo = open("todo.txt","w")
  for w in lista:
    adicionar(w[1])
  arquivo.close()
  return

#(Para fazermos a função FAZER é necessário um index, para isso repetimos grande parte da função ADICIONAR)
def adicionarFAZER(tupla):
  arquivo = open("done.txt", "r")
  palavra = arquivo.readlines()
  if len(tupla) == 2:
    for x in tupla[1]:
      if dataValida(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif horaValida(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif prioridadeValida(x) == True: 
        palavra.append(x)
        palavra.append(' ')
  palavra.append(tupla[0])
  palavra.append(' ')
  if len(tupla) == 2: 
    for x in tupla[1]:
      if contextoValido(x) == True:
        palavra.append(x)
        palavra.append(' ')
      elif projetoValido(x) == True:
        palavra.append(x)
  palavra.append("\n")
  if palavra[len(palavra)-1] == ' ':
    palavra.pop(len(palavra)-1)
  arquivo = open("done.txt","w")
  arquivo.writelines(palavra) #Aqui, o programa de fato pega tudo que foi adicionado em palavras e adiciona ao arquivo.
  arquivo.close
  return

#>>>TAREFA 20:
#(Essa função remove do arquivo e guarda em done.txt, um outro arquivo com todas as tarefas feitas.)
def fazer(numero):
  lista = auxiliarRemover()
  feito = ''
  for x in lista:
    if str(x[0]) == numero:
      feito = lista.pop(int(numero)-1)[1]
  if feito == '':
    print("Não existe na lista!")
    return
  arquivo = open("todo.txt","w")
  for w in lista:
    adicionar(w[1])
  arquivo.close()
  if type(feito) == list: 
    adicionarFAZER(feito)
  return


#(Para a função prioridade, seguimos a mesma ideia que precisamos de um index).
def prioridadeINDEX(lista):
  cont = 0
  while cont < len(lista):
    if prioridadeValida(lista[cont]) == True:
      return cont
    cont += 1
  return False

#>>>TAREFA 18:
#(Essa função recebe do usuário um numero e uma prioridade no qual ele queira pegar da lista e prioriza-la).
def priorizar(numero,prio):
  lista = auxiliarRemover()
  for x in lista:
    if str(x[0]) == numero:
      if type(prioridade(x[1][1])) == str:
        x[1][1].pop(prioridadeINDEX(x[1][1]))
        x[1][1].append('(' + prio + ')')
  arquivo = open("todo.txt","w")
  for w in lista:
    adicionar(w[1])
  arquivo.close()  
  return

#PARTE FINAL:
def processarComandos(comandos) :
  if comandos[1] == "a":
    copia = comandos[2:]
    stringFlag = ''
    for item in copia:
      stringFlag += item + ' '
    stringFlag = stringFlag.strip()
    adicionar(organizar(stringFlag))
    return
  elif comandos[1] == "r":
    remover(comandos[2])
    return    
  elif comandos[1] == "l":
    listar()
    return    
  elif comandos[1] == "f":
    fazer(comandos[2])
    return    
  elif comandos[1] == "p":
    priorizar(comandos[2],comandos[3])
    return
  elif comandos[1] == "help":
    print("""
█████████████████████████████ Seja bem vindo a nossa agenda! █████████████████████████████

▶▶▶ SOBRE O PROGRAMA: 
O programa é um pequeno programa onde o usuário faz as anotações de compromissos e
horários e informações diversas, geralmente utilizado para fins pessoais.

▶▶▶ ANTES DE UTILIZARMOS OS COMANDOS:
Para podermos utilizar os comandos devemos primeiro abri-lo digitando o seu nome pela sua extensão (Exemplo: agenda.py):
Exemplo: "agenda.py a (21062019 Ouvir todos os álbuns de Nicki Minaj)"
Sem asteriscos e sem parenteses, você abre o arquivo e logo em seguida escolhe um dos comandos abaixo:

▶▶▶ COMANDOS:
▶ ADICIONAR: Para adicionarmos uma tarefa a agenda, digite o comando 'a' (sem aspas).
▶ REMOVER: Para removermos uma tarefa da agenda, digite o comando 'r' (sem aspas) e o número correspondente a tarefa.
▶ FAZER: Para marcar uma tarefa como feita, digite o comando 'f' (sem aspas) e o número correspondente a tarefa.
▶ PRIORIZAR = Para modificar a prioridade de uma tarefa, digite o comando 'p' (sem aspas), o número corresponde a tarefa e a nova prioridade.
▶ LISTAR = 'l' Para listarmos todas as atividades ordenada, digite o comando 'l' (sem aspas).
""")
  else :
    print("Comando inválido.")
    
processarComandos(comandos)
