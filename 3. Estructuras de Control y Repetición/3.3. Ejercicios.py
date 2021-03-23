#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas. 
# Como ejemplos de ejecución:
#
# Introduce la hora: 8
# Introduce los minutos: 57
# Son las 08:57 AM
# Introduce la hora: 21
# Introduce los minutos: 31
# Son las 09:31 PM
# Introduce la hora: 26:
# Hora inválida. Deben ser entre 0 y 23.
#-----------------------------------------------------------------------------------------------------------
from datetime import datetime
hora  = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
if hora>12:
    hora_formato_12h = datetime.strptime(str(hora)+":"+str(minutos), "%H:%M")
    print(hora_formato_12h.strftime("%I:%M %p"))
else:
    hora_formato_12h = datetime.strptime(str(hora)+":"+str(minutos), "%H:%M")
    print(hora_formato_12h.strftime("%I:%M %p"))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Se nos ha solicitado programar el calculador de la tarifa a pagar por los 
# usuarios de una compañía de telefonía móvil. Todos los usuarios pagan una tarifa base de 10 euros al mes
# siempre que no hablen más de 180 minutos al mes. A partir de los 180 minutos, los usuarios pagan 
# 10 céntimos por cada minuto hablado desde los 180 hasta los 240 minutos. 
# A partir de ese momento, los usuarios pagan 20 céntimos por cada minuto por cada minuto extra consumido
# a partir de los 240. El calculador debe pedir al usuario los minutos hablados y devolver los euros 
# a pagar.
#-----------------------------------------------------------------------------------------------------------
tarifa_base = 10
centimos_por_minuto = 10

minutos_hablados =  int(input("Introduce minutos hablados: "))

if minutos_hablados == 180:
    euros_a_pagar = tarifa_base
elif minutos_hablados > 180 and minutos_hablados <= 240:
    centimos_a_pagar = (minutos_hablados-180)*centimos_por_minuto
    euros_a_pagar = centimos_a_pagar//100
    print("Debes pagar: " + str(euros_a_pagar))
elif minutos_hablados > 240:
    centimos_a_pagar = (minutos_hablados-240)*(centimos_por_minuto*2)
    euros_a_pagar = centimos_a_pagar//100
    print("Debes pagar: " + str(euros_a_pagar))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Otra persona y tú queréis reservar mesa en un restaurante. 
# Queremos un programa que nos pregunte el estilo de vestir nuestro y el de nuestro compañero, 
# que serán valores entre 0 y 10. Si uno de los dos tenemos un estilo de 8 o superior, 
# entonces sí que tendremos mesa para cenar y deberá mostrar un mensaje por pantalla. 
# Esto es así siempre y cuando uno de los dos no tenga un 2, en cuyo caso no tendremos mesa. 
# En cualquier otro caso, el mensaje que debe mostrar es que no sabemos si tendremos mesa.
#-----------------------------------------------------------------------------------------------------------
swag_o_meter = int(input("¿En una escala de 0 al 10, cuál es tú nivel de swag?"))
swag_o_meter_pal = int(input("¿En una escala de 0 al 10, cuál el nivel de swag de tu compañero?"))
if((swag_o_meter >= 8 or swag_o_meter_pal >= 8) and (swag_o_meter != 2 and swag_o_meter_pal != 2)):
    print("Vuestro nivel de swag os hace merecedores de la mejor de nuestras mesas")
elif ((swag_o_meter >= 8 or swag_o_meter_pal >= 8) and (swag_o_meter == 2 or swag_o_meter_pal == 2)):
    print("¡La gente con swag de nivel 2 no tiene cabida en esta sociedad!")
else:
    print("Preferimos esperar a futuras reservas. Puede que sean más importante que la vuestra")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Realiza un programa que pregunte por un día de la semana y si estamos o no de vacaciones. 
# El programa deberá mostrar un mensaje indicando a qué hora nos suena la alarma. 
# Entre semana, la alarma sonará a las 8:00 y los fines de semana a las 10:00. 
# Sin embargo, si estamos de vacaciones, los días entre semana sonará a las 10:00 y los fines de semana 
# estará apagada.
#-----------------------------------------------------------------------------------------------------------
dia_de_la_semana = str(input("Introduce día de la semana: "))
vacaciones = bool(input("Indica si tienes vacaciones (True=si/False=no): "))
if (not vacaciones and (dia_de_la_semana == "lunes" or dia_de_la_semana == "martes" or dia_de_la_semana == "miercoles" or dia_de_la_semana == "jueves" or dia_de_la_semana == "viernes")):
    print("La alarma sonará a las 8:00")
elif (vacaciones and (dia_de_la_semana == "lunes" or dia_de_la_semana == "martes" or dia_de_la_semana == "miercoles" or dia_de_la_semana == "jueves" or dia_de_la_semana == "viernes")):
    print("La alarma sonará a las 10:00")
else:
    if (not vacaciones and (dia_de_la_semana == "sabado" or dia_de_la_semana == "domingo")):
        print("La alarma está apagada")
    else:
        print("La alarma sonará a las 10:00")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 4
# ----------------------------------------------------------------------------------------------------------
# Realiza un programa que pregunte tres valores enteros y muestre un mensaje por pantalla indicando
# si los dos primeros tienen una diferencia máxima de 1 mientras que el tercero tiene una diferencia mayor
# que 2 con los otros dos. Utiliza la función abs(sum) para calcular el valor absoluto de un número.
#-----------------------------------------------------------------------------------------------------------
valor_1 = int(input("Introduce el primer valor: "))
valor_2 = int(input("Introduce el segundo valor: "))
valor_3 = int(input("Introduce el tercer valor: "))

diferencia_1_con_2 = abs(valor_1 - valor_2)
diferencia_3_con_1_mas_2 = abs((valor_1 + valor_2) - valor_3)

if(diferencia_1_con_2 <= 1):
    print("Los dos primeros valores tienen una diferencia máxima de 1")
elif(diferencia_3_con_1_mas_2 > 2):
    print("El tercer valor tiene una diferencia mayor que 2 con los otros dos")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------