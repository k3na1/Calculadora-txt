import statistics as st



try:
    with open('datos.txt', 'r') as datos:
        numeros = datos.read().splitlines()
        intConvertor = [int (i) for i in numeros]                   # Convertidor de string a integer
        numeros = intConvertor

        mediana = st.median(numeros)
        
        modas = st.mode(numeros)
       

except:
    print("ERROR: ERROR EN EL PROGRAMA. CONSULTAR AL DUEÑO")


