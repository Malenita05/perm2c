#juego de ajedrez

import os
from importlib.abc import TraversableResources

#definiendo el tablero
tablero = [["  ","AA","BB","CC","DD","EE","FF","GG","HH","  "],
           ["01","bT","bP","  ","  ","  ","  ","wP","wT","01"],
           ["02","bC","bP","  ","  ","  ","  ","wP","wC","02"],
           ["03","bA","bP","  ","  ","  ","  ","wP","wA","03"],
           ["04","bQ","bP","  ","  ","  ","  ","wP","wQ","04"],
           ["05","bK","bP","  ","  ","  ","  ","wP","wK","05"],
           ["06","bA","bP","  ","  ","  ","  ","wP","wA","06"],
           ["07","bC","bP","  ","  ","  ","  ","wP","wC","07"],
           ["08","bT","bP","  ","  ","  ","  ","wP","wT","08"],
           ["  ","AA","BB","CC","DD","EE","FF","GG","HH","  "],]

#Leyenda:
# T = torre
# C = caballo
# A = alfil
# Q = reina
# K = rey
# P = peon
# w = white
# b = black

#las letras y numeros al rededor del tablero se usaran para ingresar las coordenadas de los movimientos en el juego

#se usa para dibujar el tablero de juego en la terminal
def imp_tablero():
  b="="*82
  resetear = '\x1b[0m'
  amarillo = '\x1b[1;30;43m'
  rosa = '\x1b[45m'
  blanco = '\x1b[1;30;47m'
  bandera = False
  bandera = ~bandera
  print('|'*26+"Bienvenidos al juego de Aledrez"+'|'*26)
  for c in range(10):
    print(b)
    for a in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*6 + resetear , end="")
      else:
        if a == 0 or a == 9:
          print("||" + blanco + " "*6 + resetear , end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*6 + resetear , end="")
          else:
            print("||" + rosa + " "*6 + resetear, end="")
      bandera = ~bandera
    print("||")
    for f in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*2+tablero[f][c]+" "*2 + resetear,end="")
      else:
        if f == 0 or f == 9:
          print("||" + blanco + " "*2+tablero[f][c]+" "*2 + resetear,end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*2+tablero[f][c]+" "*2 + resetear,end="")
          else:
            print("||" + rosa + " "*2+tablero[f][c]+" "*2 + resetear,end="")
      bandera = ~bandera
    print("||")
    for a in range(10):
      if c == 0 or c == 9:
        print("||" + blanco + " "*6 + resetear , end="")
      else:
        if a == 0 or a == 9:
          print("||" + blanco + " "*6 + resetear , end="")
        else:
          if(bandera):
            print("||" + amarillo + " "*6 + resetear , end="")
          else:
            print("||" + rosa + " "*6 + resetear, end="")
      bandera = ~bandera
    bandera = ~bandera
    print("||")
  print(b)
#usamos esta funcion para sacar las posiciones de las entradas (casilla actual y de destiono)
def extraer_pos(m,d):
  m_x = ord(m[0])-64
  m_y = int(m[3])
  d_x = ord(d[0])-64
  d_y = int(d[3])

  if (m_x < 1 or m_x > 8):
    m_x = False
  if (d_x < 1 or d_x > 8):
    d_x = False
  if (m[2] == 0):
    if (m_y < 1 or m_y > 8):
      m_y = False
    else:
      m_y = False
  if (d[2] == 0):
    if (d_y < 1 or d_y > 8):
      d_y = False
    else:
      d_y = False

  return m_x,m_y,d_x,d_y
#evaluamos las reglas para poder mover cada una de las 6 piezas:
#torres
def torres(m_y,m_x,d_y,d_x):
  if (m_y == d_y or m_x == d_x):
    return True
  else:
    return False
#caballos  
def caballos(m_y,m_x,d_y,d_x):
  if (d_x == m_x + 1 and d_y == m_y + 2):
    return True
  elif (d_x == m_x + 2 and d_y == m_y + 1):
    return True
  elif (d_x == m_x + 1 and d_y == m_y - 2):
    return True
  elif (d_x == m_x - 2 and d_y == m_y + 1):
    return True
  elif (d_x == m_x + 2 and d_y == m_y - 1):
    return True
  elif (d_x == m_x - 1 and d_y == m_y + 2):
    return True
  elif (d_x == m_x - 1 and d_y == m_y - 2):
    return True
  elif (d_x == m_x - 2 and d_y == m_y - 1):
    return True
  else:
    return False
#alfiles
def alfiles(m_y,m_x,d_y,d_x):
  if abs(d_x - m_x) == abs(d_y - m_y):
    return True
  else:
    return False
#rey 
def Rey(m_y,m_x,d_y,d_x):
  if (d_x == m_x + 1 and d_y == m_y):
    return True
  elif (d_x == m_x and d_y == m_y + 1):
    return True
  elif (d_x == m_x - 1 and d_y == m_y):
    return True
  elif (d_x == m_x and d_y == m_y - 1):
    return True
  elif (d_x == m_x + 1 and d_y == m_y + 1):
    return True
  elif (d_x == m_x - 1 and d_y == m_y + 1):
    return True
  elif (d_x == m_x - 1 and d_y == m_y - 1):
    return True
  elif (d_x == m_x + 1 and d_y == m_y - 1):
    return True
  else:
    return False
#reina  
def Reina(m_y,m_x,d_y,d_x):
  if (torres(m_y,m_x,d_y,d_x) == True or alfiles(m_y,m_x,d_y,d_x) == True):
    return True
  else:
    return False
#peones
def peones(m_y,m_x,d_y,d_x,player):
  if player == 1:
    if m_x == d_x and m_y == d_y-1:
      return True
    elif m_x == d_x and m_y == d_y-2:
      return True
  if player == 2:
    if m_x == d_x and m_y == d_y+1:
      return True
    elif m_x == d_x and m_y == d_y+2:
      return True
  else:
    return False
#usamos esta funcion para definir en que turno se pueden mover las piezas
def mover(m_y,m_x,d_y,d_x,player):
  if (player == 1):
    #turno uno piezas blancas
    if (tablero[m_x][m_y] == "wT"):
      if(torres(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "wC"):
      if(caballos(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "wA"):
      if(alfiles(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "wK"):
      if(Rey(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "wQ"):
      if(Reina(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "wP"):
      if(peones(m_y,m_x,d_y,d_x,player)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
      else:
        print("Casilla no valida")
        juego()
    else:
      print("Ficha no valida")
      juego() 
  if (player == 2):
    #truno 2, fichas negras
    if (tablero[m_x][m_y] == "bT"):
      if(torres(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "bC"):
      if(caballos(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "bA"):
      if(alfiles(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "bK"):
      if(Rey(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "bQ"):
      if(Reina(m_y,m_x,d_y,d_x)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
        # print(m_x,m_y,d_x,d_y)
      else:
        print("Casilla no valida")
        juego()
    elif (tablero[m_x][m_y] == "bP"):
      if(peones(m_y,m_x,d_y,d_x,player)==True):
        m = tablero[m_x][m_y]
        tablero[m_x][m_y] = "  "
        tablero[d_x][d_y] = m
      else:
        print("Casilla no valida")
        juego()
    else:
      print("Ficha no valida")
      juego()
# desarroyamos el orden y damos inicio al juego
def juego():
  bandera = True
  
  ficha_mover = ""
  casilla_destino = ""

  player = 0
  #en este bucle imprimimos el tablero y definimos los turnos para mover las fichas
  while(True):
    imp_tablero()
    if(bandera):
      print("Jugador 1")
      bandera = False
      player = 1
    else:
      print("Jugador 2")
      bandera = True
      player = 2
    #luego pedimos la posicion actual de la ficha y la casilla a la cual se la desea mover
    casilla_mover = input("Ingrese coordenadas a mover segun el tablero Formato(AA01): ")
    casilla_destino = input("Ingrese coordenadas de destino segun el tablero Formato(AA01): ")
    #sacamos los valores de las posiciones en la matriz del tablero
    m_x,m_y,d_x,d_y = extraer_pos(casilla_mover,casilla_destino)
    #y procedemos a moverlas
    if (m_x == False or m_y == False or d_x == False or d_y == False):
      print ("Posicion no valida")
      juego()
    else:
      mover(m_x,m_y,d_x,d_y,player)

juego()
