from procesamiento import convertidora_a_mayusculas, removedora_de_espacios

TEXTO_A_PROCESAR = '  muestra  '

# El siguiente codigo realiza procesamiento de texto
texto_procesado = convertidora_a_mayusculas(TEXTO_A_PROCESAR)
texto_procesado = removedora_de_espacios(texto_procesado)
# Imprime el resultado
print(texto_procesado)
