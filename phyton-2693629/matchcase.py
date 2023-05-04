num1,num2=100,25
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
selector=(input('Digite la opcion'))
match selector:
    case '1':
        print(num1+num2) #asi se suma
    case '2':
        print(num1-num2) #asi se resta
    case '3':
        print(num1*num2) #asi se multiplica
    case '4':
        print(num1/num2) #asi se divide