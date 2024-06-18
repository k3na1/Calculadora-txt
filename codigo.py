import statistics as st



try:
    with open('datos.txt', 'r') as datos:
        numeros = datos.read().splitlines()
        intConvertor = [int (i) for i in numeros]                   # Convertidor de string a integer
        numeros = intConvertor

        mediana = st.median(numeros)
        print(mediana)
        promedio = sum(numeros) / len(numeros)
        promFinal = round(promedio,1)
        print(promFinal)
except:
    print("ERROR: ERROR EN EL PROGRAMA. CONSULTAR AL DUEÑO")