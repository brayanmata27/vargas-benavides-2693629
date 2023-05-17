import random
tupla=()
tam=int(random.randint(0,101))
    
for i in range(tam):
    num=int(random.randrange(100))
    tupla=tupla+(num,)
print(tupla)