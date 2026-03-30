from random import *
import string

def CodigoGerado():
    
    numeros = string.digits
    letras = string.ascii_lowercase
    especiais = ("!@#$")

    tudo = (numeros + letras + especiais)
    
    senha = ""
    
    for i in range(8):
        senha += choice(tudo)
        
    return senha    
    
    