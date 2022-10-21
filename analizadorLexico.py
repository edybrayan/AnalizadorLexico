import sys
import string

#definimos cuales serian los delimitadores
delim=['\t','\n',',',';','(',')','{','}','[',']','#','<','>']
#definimos cuales serian los operadores
oper=['+','-','*','/','%','=','!']
#definimos cuales son las palabras reservadas o keyword
key=["int","float","char","double","bool","void","extern","unsigned","goto","static","class","struct","for","if","else","return","register","long","while","do"]
#definimis cuales son los los 
predirect=["include","define"]
#definimos cuales son las librerias de los archivos o codigos
header=["stdio.h","conio.h","malloc.h","process.h","string.h","ctype.h"]

word_list1=" "
i=0
j=0
f=0

numflag=0

token=[0]*50

#definimos una funcion dende nos indicaran si el token es de tipo delimitador o no
def isdelim(c):
    for k in range(0,14):
        if c==delim[k]:
            return 1
        return 0

#funcion para definir si el token es un operador o no
def isop(c):
    for k in range(0,7):
        if c==oper[k]:
            ch=word_list1[i+1]
            i+=1
            for j in range(0,6):
                if ch==oper[j]:
                    fop=1
                    sop=ch
                    return 1
                #ungetc(ch,fp);
                return 1
                j+=1
        return 0;
        k+=1
#un funcion para definir si el token es un numero entero o es una cadena predictiva como el "include" o "iostream"
def check(t):
    print (t)
    if numflag==1:
        print ("\n numero "+str(t))
        return
    for k in range(0,2):#(i=0;i<2;i++)
        if strcmp(t,predirect[k])==0:
            print ("\n preprocessor directive "+str(t))
            return
    for k in range(0,6): #=0;i<6;i++)
        if strcmp(t,header[k])==0:
            print ("\n libreria "+str(t))
            return
    for k in range(0,21): #=0;i<21;i++)
        if strcmp(key[k],t)==0:
            print ("\n palabra reservada "+str(key[k]))
            return
        print ("\n identificador \t%s"+str(t))


#esta funcion hara que no lea los comentarios que esten con //
def skipcomment():
    ch=word_list[i+1]
    i+=1
    if ch=='/':
        while word_list1[i]!='\0':
            i+=1#ch=getc(fp))!='\0':
    elif ch=='*':
        while f==0:
            ch=word_list1[i]
            i+=1
        if c=='/':
            f=1
    f=0



#En esta funcion se realizara el llamdo del archivo .txt que se leera

a=input("Ingresar nombre de archivo:")
s=open(a,'r')
str1=s.read()
word_list1=str1.split()




i=0
#print word_list1[i]
for word in word_list1 :
    print (word_list1[i])
    if word_list1[i]=="/":
        print (word_list1[i])
    elif word_list1[i]==" ":
        print (word_list1[i])
    elif word_list1[i].isalpha():
        if numflag!=1:
            token[j]=word_list1[i]
            j+=1
        if numflag==1:
            token[j]='\0'
            check(token)
            numflag=0
            j=0
            f=0
        if f==0:
            f=1
    elif word_list1[i].isalnum():
        if numflag==0:
            numflag=1
            token[j]=word_list1[i]
            j+=1
        else:
    #en esta funcion definimos el isdelim para saber si el token es un delimitador o no
            if isdelim(word_list1[i]):
                if numflag==1:
                    token[j]='\0'
                    check(token)
                    numflag=0
                if f==1:
                    token[j]='\0'
                    numflag=0
                    check(token)
                j=0
                f=0
                print ("\n delimitador : " + word_list1[i])

# esta funcion definira si el token ingresado es una operador o no
    elif isop(word_list1[i]):
        if numflag==1:
            token[j]='\0'
            check(token)
            numflag=0
            j=0
            f=0
        if f==1:
            token[j]='\0'
            j=0 
            f=0
            numflag=0
            check(token)    
        if fop==1:
            fop=0
            print ("\n operador \t"+str(word_list1[i])+str(sop))
        else:
            print ("\n operador \t"+str(c))
    elif word_list1[i]=='.':
        token[j]=word_list1[i]
        j+=1
    i+=1
    