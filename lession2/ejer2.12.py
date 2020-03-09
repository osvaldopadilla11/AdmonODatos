miArchivo = open("poem.txt")
elTexto = miArchivo.read()
miPoemaBinario= bytes(elTexto, encoding="utf")

print(miPoemaBinario)

ascci_E=miPoemaBinario[0] # valor ASCII del caracter E
ascci_l=miPoemaBinario[0] # valor ASCII del caracter l

print(ascci_E)
print(ascci_l)


f = open("poem_binario.Xcosa","wb")
f.write(miPoemaBinario)
f.close()

      