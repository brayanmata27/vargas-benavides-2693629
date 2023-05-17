diccionario={"rojo": "red" , 
            "amarillo": "yellow" , 
            "verde": "green" , 
            "azul": "blue" , 
            "rosa": "pink" , 
            "blanco": "white" , 
            "negro": "black" , 
            "marron": "brown",
            "morado": "purple",
            "lila": "lilac"}

words=[input('ingrese color')]
for word in words:
    if word in diccionario:
        print(word, "->", diccionario[word])
    else:
        print(word, 'no esta en el diccionario')