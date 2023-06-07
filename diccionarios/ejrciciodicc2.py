diccionarioe={"gato": "cat" , 
            "perro": "dog" , 
            "abeja": "bee" , 
            "conejo": "rabbit" , 
            "gallina": "hen" , 
            "vaca": "cow" , 
            "serpiente": "snake" , 
            "cerdo": "pig",
            "pajaro": "bird",
            "araña": "spider"}

words=[input('ingrese animal del diccionario en español')]
for word in words:
    if word in diccionarioe:
        print(word, "-->", diccionarioe[word])
    else:
        print(word, 'no esta en el diccionario')


diccionarioi={"cat": "gato" , 
            "dog": "perro" , 
            "bee": "abeja" , 
            "rabbit": "conejo" , 
            "hen": "gallina" , 
            "cow": "vaca" , 
            "snake": "serpiente" , 
            "pig": "cerdo",
            "bird": "pajaro",
            "spider": "araña"}

words=[input('ingrese animal del diccionario en ingles')]
for word in words:
    if word in diccionarioi:
        print(word, "-->", diccionarioi[word])
    else:
        print(word, 'no esta en el diccionario' ,)

