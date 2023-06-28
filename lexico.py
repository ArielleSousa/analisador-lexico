estado = 0
caracter =''
linha = 1
cadeia_reconhecida = ""

# Funções gerais
def letra(char):
    return 'a' <= char <= 'z'
def espacamento(char):
   if char in [' ','\n', '\t']:
      return True
palavras_reservadas = {
    "program": True,
    "if": True,
    "then": True,
    "else": True,
    "while": True,
    "do": True,
    "until": True,
    "int": True,
    "double": True,
    "char": True,
    "case": True,
    "switch": True,
    "end": True,
    "procedure": True,
    "function": True,
    "for": True,
    "begin": True,
}
# Função léxica
def lexico():
    global estado, cadeia_reconhecida, linha
    pos = 0
    while pos < len(conteudo):
        caracter = conteudo[pos]
        #print(estado)

        if estado == -1:
          verifica_token(cadeia_reconhecida)

        if caracter == "\n":
          linha += 1

        if estado == 0:
            if letra(caracter):
                estado = 1
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter.isdigit():
                estado = 4
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '-':
                estado = 7
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter in (';,.-*(){}'):
                estado = 8
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter in (':>='):
                estado = 9
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '<':
                estado = 11
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '+':
                estado = 13
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '@':
              estado = 15
              cadeia_reconhecida += caracter
              pos += 1
            elif caracter == '/':
              estado = 19
              cadeia_reconhecida += caracter
              pos += 1
            elif caracter == '*':
              estado = 24
              cadeia_reconhecida += caracter
              pos += 1
            else:
              pos += 1
        elif estado == 1:
            if caracter.isalnum():
                estado = 2
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '@' or caracter == '_':
                estado = 3
                cadeia_reconhecida += caracter
                pos += 1
            else:
              if espacamento(caracter):
                pos += 1
              verifica_token(cadeia_reconhecida)

        elif estado == 2:
            if caracter.isalnum():
                estado = 2
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter == '_' or caracter =='@':
               estado = -1
               cadeia_reconhecida += caracter
               pos+=1
              #  
            else:
                if espacamento(caracter):
                  pos += 1
                verifica_token(cadeia_reconhecida)
        elif estado == 3:
            if caracter.isalnum():
                estado = 2
                cadeia_reconhecida += caracter
                pos += 1
            else:
              if espacamento(caracter):
                pos += 1
              verifica_token(cadeia_reconhecida)
        elif estado == 4:
            if caracter == ',':
                estado = 5
                cadeia_reconhecida += caracter
                pos += 1
            elif caracter.isdigit():
                estado = 4
                cadeia_reconhecida += caracter
                pos += 1
            else:
                if espacamento(caracter):
                  pos += 1
                verifica_token(cadeia_reconhecida)
        elif estado == 5:
            if caracter.isdigit():
                estado = 6
                cadeia_reconhecida += caracter
                pos += 1
        elif estado == 6:
            if caracter.isdigit():
                estado = 6
                cadeia_reconhecida += caracter
                pos += 1
            else:
                if espacamento(caracter):
                  pos += 1
                verifica_token(cadeia_reconhecida)
        elif estado == 7:
            if caracter.isdigit():
                estado = 4
                cadeia_reconhecida += caracter
                pos += 1
            else:
              if espacamento(caracter):
                pos += 1
              verifica_token(cadeia_reconhecida)
               

        elif estado == 8:
           verifica_token(cadeia_reconhecida)
        elif estado == 9:
            if caracter == '=':
                estado = 10
                cadeia_reconhecida += caracter
                pos += 1
            else:
                if espacamento(caracter):
                  pos += 1
                verifica_token(cadeia_reconhecida)
        elif estado == 10:
           verifica_token(cadeia_reconhecida)
        elif estado == 11:
            if caracter in ('=>'):
                estado = 12
                cadeia_reconhecida += caracter
                pos += 1
            else:
                if espacamento(caracter):
                  pos += 1
                verifica_token(cadeia_reconhecida)
        elif estado == 12:
           verifica_token(cadeia_reconhecida)
        elif estado == 13:
          if caracter == '+':
            estado = 14
            cadeia_reconhecida += caracter
            pos += 1
          else:
            if espacamento(caracter):
              pos += 1
            verifica_token(cadeia_reconhecida)
        elif estado == 14:
           verifica_token(cadeia_reconhecida)
        elif estado == 15:
          if caracter =='@':
            estado = 16
            cadeia_reconhecida += caracter
            pos += 1
          else:
            if espacamento(caracter):
              pos += 1
            verifica_token(cadeia_reconhecida)
        elif estado == 16:
          estado = 17
          cadeia_reconhecida += caracter
          pos += 1
        elif estado == 17:
          if caracter == '\n':
            estado = 18
            cadeia_reconhecida += caracter
          else:
            estado = 17
            pos += 1
        elif estado == 18:
           verifica_token(cadeia_reconhecida)
        elif estado == 19:
          if caracter == '*':
            estado = 24
            cadeia_reconhecida += caracter
            pos += 1
          elif caracter == '/':
            estado = 20
            cadeia_reconhecida += caracter
            pos += 1
          else:
            if espacamento(caracter):
               pos += 1
            verifica_token(cadeia_reconhecida)
        elif estado == 20:
          estado = 21
          cadeia_reconhecida += caracter
          pos += 1
        elif estado == 21:
          if caracter == '/':
            estado = 22
            cadeia_reconhecida += caracter
            pos += 1
          else:
            estado = 21
            cadeia_reconhecida += caracter
            pos += 1
        elif estado == 22:
          if  caracter == '/':
            estado = 23
            cadeia_reconhecida += caracter
            pos += 1
          else:
            estado = 21
            cadeia_reconhecida += caracter
            pos += 1
        elif estado == 23:
           pos += 1
           verifica_token(cadeia_reconhecida)
        elif estado == 24:
          estado = 25
          cadeia_reconhecida += caracter
          pos += 1
        elif estado == 25:
          if caracter == '*':
            estado = 26
            cadeia_reconhecida += caracter
            pos += 1
          else:
            estado = 25
            cadeia_reconhecida += caracter
            pos += 1
        elif estado == 26:
          if caracter == '/':
            estado = 23
            cadeia_reconhecida += caracter
            pos += 1
          else:
            estado = 25
            cadeia_reconhecida += caracter
            pos += 1

    if espacamento(caracter):
      pos += 1

    if cadeia_reconhecida != "":
      verifica_token(cadeia_reconhecida)
    

def verifica_token(token):
    global cadeia_reconhecida, estado, caracter, linha
    if estado in [1, 2]:
        if token in palavras_reservadas:
            print('Token', token, '-> PALAVRA RESERVADA')
        else:
            print('Token', token, '-> IDENTIFICADOR')
    elif estado in [4, 6]:
        print('Token', token, '-> DIGITO')
    elif estado in [7,8, 9, 10, 11, 12, 13, 14, 15, 19]:
        print('Token', token, '-> SIMBOLO ESPECIAL')
    elif estado in [18,23]:
       pass
    else:
        print(f'Linha: {linha} - inválido -> {token}')
        exit()
    cadeia_reconhecida = ""
    estado = 0



# Lê o arquivo e chama a função léxica
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()

lexico()
