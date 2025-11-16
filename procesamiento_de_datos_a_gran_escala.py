# procesar_logs.py
from datos_logs import logs_simulados


# PROCESAR DATOS CON WHILE



logs_procesados = []  # copia local de los registros

i = 0
while i < len(logs_simulados):
    registro = logs_simulados[i]
    # Cada registro tiene: [usuario, entrada, salida]
    if len(registro) == 3:
        usuario, entrada, salida = registro
        logs_procesados.append([usuario, entrada, salida])
    i += 1  # siguiente registro


# 2. CONTAR ACCESOS CON FOR


usuarios_unicos = []

# Sacar usuarios sin repetir
for registro in logs_procesados:
    usuario = registro[0]
    if usuario not in usuarios_unicos:
        usuarios_unicos.append(usuario)

# Contar accesos por cada usuario
resultados = []  # [nombre_usuario, numero_de_accesos]

for usuario in usuarios_unicos:
    conteo = 0 #variable de conteo para sumar 1 por cada acceso
    for registro in logs_procesados:
        if registro[0] == usuario:
            conteo += 1
    resultados.append([usuario, conteo])


# 3. MOSTRAR RESULTADOS


print("Número de accesos por usuario:")
for usuario, num_accesos in resultados:
    print(f"{usuario}: {num_accesos}")

print("\nLista resultados (para el informe):")
print(resultados)