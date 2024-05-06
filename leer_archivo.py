noticia = open("noticia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)

#para que se note tildes 
print("\n")
noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
