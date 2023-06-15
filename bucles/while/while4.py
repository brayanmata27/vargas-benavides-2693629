x,y=1,1
resta=0
while x!=0:
    print("Si quieres salirte, digita dos veces cero ")
    x= int(input("Digite un numero: "))
    y= int(input("Digite un numero: "))
    if x<y:
        resta=y%x
    if x>y:
        resta=x%y
    print("Lo que sobra de la resta es: " ,resta)
print("Haz salido del sistema con exito!")