import random                                           

nove_digitos = ''                                       

for i in range(9):                                         
    nove_digitos += str(random.randint(0, 9))           


lista_num = nove_digitos[:9]                            
contador = 10                                          
soma = 0                                                

for num in lista_num:                                  
    num = int(num)                                     
    resultado = num * contador                         
    soma = resultado + soma                            
    contador -= 1                                      

digito1 = (soma * 10) % 11                              
digito1 = digito1 if digito1 <= 9 else 0                

contador = 11                                           
soma = 0                                                

for num in lista_num:                                   
    num = int(num)                                      
    resultado = num * contador                          
    soma = resultado + soma                             
    contador -= 1                                       

digito2 = (soma * 10) % 11                             
digito2 = digito2 if digito2 <= 9 else 0               

cpf = str(nove_digitos) + str(digito1) + str(digito2)   
print(f'O número de CPF é: {cpf}')                      