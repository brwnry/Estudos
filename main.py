def media(*num):                
    soma = 0                   
    for n in num:               
        soma += n               
    return soma / len(num)     
print(media(2, 3, 4, 5, 6, 7, 8, 9, 10))