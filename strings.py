def sem_espaco(texto):
    return texto.strip()
    
def main():
    
    frase = "   Hoje eu ganho   "
    tudo_junto = sem_espaco(frase)
    
    #no tudo_junto eu atribuo o valor da funçao 
    #que passa a valer sem_espaco(texto)aonde esta escrito texto sustituio pela variavel frase
    #quando execurta no print ele vai usar a primeira funcao dentro da variavel frase e remover os espaços
    
    
    print(f"Sem espaços: {tudo_junto}")
    print(f"Substring [2:15]: {tudo_junto[2:15]}") # vai pegar a substring do indice 2 até o 15
   
        
    
main()
