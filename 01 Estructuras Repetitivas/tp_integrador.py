"""
Trabajo Práctico Integrador: Resolución de Ejercicios Propuestos
Autor: Gonzalo Gabriel Mayorga
"""

# =========================================================
# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Autor: Gonzalo Gabriel Mayorga
# =========================================================


def pedir_texto_solo_letras(mensaje, mensaje_error="Error: Solo se permiten letras."):
    dato = input(mensaje).strip()
    while dato == "" or not dato.isalpha():
        print(mensaje_error)
        dato = input(mensaje).strip()
    return dato


def pedir_entero_positivo(mensaje, permitir_cero=False):
    dato = input(mensaje).strip()
    while (not dato.isdigit()) or ((not permitir_cero) and int(dato) == 0):
        if not dato.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Debe ser mayor a 0.")
        dato = input(mensaje).strip()
    return int(dato)


def pedir_s_o_n(mensaje):
    dato = input(mensaje).strip().lower()
    while dato not in ("s", "n"):
        print("Error: Ingrese S o N.")
        dato = input(mensaje).strip().lower()
    return dato


def pedir_opcion_rango(mensaje, minimo, maximo):
    dato = input(mensaje).strip()
    while (not dato.isdigit()) or not (minimo <= int(dato) <= maximo):
        if not dato.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Opción fuera de rango.")
        dato = input(mensaje).strip()
    return int(dato)


# Ejercicio 1
def ejercicio_1():
    print("\n=== Ejercicio 1 — Caja del Kiosco ===")

    cliente = pedir_texto_solo_letras("Cliente: ", "Error: El nombre debe tener solo letras y no puede estar vacío.")
    cantidad = pedir_entero_positivo("Cantidad de productos: ")

    total_sin_descuentos = 0
    total_con_descuentos = 0.0

    for i in range(1, cantidad + 1):
        precio = pedir_entero_positivo(f"Producto {i} - Precio: ")
        descuento = pedir_s_o_n(f"Producto {i} - Descuento (S/N): ")

        total_sin_descuentos += precio

        precio_final = float(precio)
        if descuento == "s":
            precio_final = precio * 0.90

        total_con_descuentos += precio_final

    ahorro = total_sin_descuentos - total_con_descuentos
    promedio = total_con_descuentos / cantidad

    print(f"\nCliente: {cliente}")
    print(f"Total sin descuentos: ${total_sin_descuentos}")
    print(f"Total con descuentos: ${total_con_descuentos:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2
def ejercicio_2():
    print("\n=== Ejercicio 2 — Acceso al Campus y Menú Seguro ===")

    usuario_correcto = "alumno"
    clave_correcta = "python123"

    intento = 1
    acceso = False

    while intento <= 3 and not acceso:
        usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
        clave = input("Clave: ").strip()

        if usuario == usuario_correcto and clave == clave_correcta:
            acceso = True
            print("Acceso concedido.")
        else:
            print("Error: credenciales inválidas.")
            intento += 1

    if not acceso:
        print("Cuenta bloqueada.")
        return

    while True:
        print("\n1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")
        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        else:
            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                print("Error: opción fuera de rango.")
            elif opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                nueva_clave = input("Nueva clave: ").strip()
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar nueva clave: ").strip()
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave actualizada correctamente.")
                    else:
                        print("Error: las claves no coinciden.")
            elif opcion == 3:
                print("Seguí adelante: cada práctica te acerca más a tu objetivo.")
            else:
                print("Saliendo del sistema...")
                break


# Ejercicio 3
def ejercicio_3():
    print("\n=== Ejercicio 3 — Agenda de Turnos con Nombres ===")

    operador = pedir_texto_solo_letras("Nombre del operador: ")

    lunes1 = ""
    lunes2 = ""
    lunes3 = ""
    lunes4 = ""

    martes1 = ""
    martes2 = ""
    martes3 = ""

    while True:
        print(f"\nOperador: {operador}")
        print("1. Reservar turno")
        print("2. Cancelar turno")
        print("3. Ver agenda del día")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")

        opcion = pedir_opcion_rango("Opción: ", 1, 5)

        if opcion == 1:
            dia = pedir_opcion_rango("Elegir día (1=Lunes, 2=Martes): ", 1, 2)
            paciente = pedir_texto_solo_letras("Nombre del paciente: ")

            if dia == 1:
                if (paciente == lunes1 or paciente == lunes2 or
                        paciente == lunes3 or paciente == lunes4):
                    print("Error: ese paciente ya tiene turno en Lunes.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes - Turno 1.")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes - Turno 2.")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes - Turno 3.")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes - Turno 4.")
                else:
                    print("No hay turnos disponibles en Lunes.")
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: ese paciente ya tiene turno en Martes.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes - Turno 1.")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes - Turno 2.")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes - Turno 3.")
                else:
                    print("No hay turnos disponibles en Martes.")

        elif opcion == 2:
            dia = pedir_opcion_rango("Elegir día (1=Lunes, 2=Martes): ", 1, 2)
            paciente = pedir_texto_solo_letras("Nombre del paciente a cancelar: ")

            encontrado = False

            if dia == 1:
                if lunes1 == paciente:
                    lunes1 = ""
                    encontrado = True
                elif lunes2 == paciente:
                    lunes2 = ""
                    encontrado = True
                elif lunes3 == paciente:
                    lunes3 = ""
                    encontrado = True
                elif lunes4 == paciente:
                    lunes4 = ""
                    encontrado = True
            else:
                if martes1 == paciente:
                    martes1 = ""
                    encontrado = True
                elif martes2 == paciente:
                    martes2 = ""
                    encontrado = True
                elif martes3 == paciente:
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print("Turno cancelado correctamente.")
            else:
                print("No se encontró ese paciente en la agenda indicada.")

        elif opcion == 3:
            dia = pedir_opcion_rango("Elegir día (1=Lunes, 2=Martes): ", 1, 2)

            if dia == 1:
                print("\nAgenda del Lunes:")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            else:
                print("\nAgenda del Martes:")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        elif opcion == 4:
            ocupados_lunes = 0
            ocupados_martes = 0

            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1

            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1

            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print("\nResumen general:")
            print(f"Lunes -> Ocupados: {ocupados_lunes} | Disponibles: {disponibles_lunes}")
            print(f"Martes -> Ocupados: {ocupados_martes} | Disponibles: {disponibles_martes}")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Día con más turnos: Empate")

        else:
            print("Sistema cerrado.")
            break


# Ejercicio 4
def ejercicio_4():
    print("\n=== Ejercicio 4 — Escape Room: La Bóveda ===")

    agente = pedir_texto_solo_letras("Nombre del agente: ")

    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    forzar_seguidas = 0
    bloqueado = False

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
        print("\n--- ESTADO ---")
        print(f"Agente: {agente}")
        print(f"Energía: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
        print(f"Alarma: {'ON' if alarma else 'OFF'}")
        print(f"Código parcial: {codigo_parcial}")

        print("\n1. Forzar cerradura")
        print("2. Hackear panel")
        print("3. Descansar")

        opcion = pedir_opcion_rango("Acción: ", 1, 3)

        if opcion == 1:
            forzar_seguidas += 1
            energia -= 20
            tiempo -= 2

            if forzar_seguidas == 3:
                alarma = True
                print("La cerradura se trabó por forzar 3 veces seguidas. ¡Alarma activada!")
            else:
                if energia < 40:
                    numero = pedir_opcion_rango("Riesgo de alarma. Elija un número del 1 al 3: ", 1, 3)
                    if numero == 3:
                        alarma = True
                        print("¡Se activó la alarma!")
                if not alarma and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("Abriste una cerradura.")

        elif opcion == 2:
            forzar_seguidas = 0
            energia -= 10
            tiempo -= 3

            print("Iniciando hackeo...")
            for paso in range(1, 5):
                codigo_parcial += "A"
                print(f"Paso {paso}/4 - Progreso: {codigo_parcial}")

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""
                print("Hackeo exitoso: se abrió una cerradura automáticamente.")

        else:
            forzar_seguidas = 0
            energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1

            if alarma:
                energia -= 10
                print("La alarma encendida te desgasta: -10 energía extra.")

            print("Descansaste para recuperar energía.")

        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            bloqueado = True
            print("El sistema se bloqueó por alarma. Derrota.")

    if cerraduras_abiertas == 3:
        print("\n¡VICTORIA! Abriste la bóveda.")
    elif bloqueado:
        print("DERROTA por bloqueo.")
    elif energia <= 0 or tiempo <= 0:
        print("\nDERROTA. Te quedaste sin energía o sin tiempo.")


# Ejercicio 5
def ejercicio_5():
    print("\n=== Ejercicio 5 — La Arena del Gladiador ===")
    print("--- BIENVENIDO A LA ARENA ---")

    nombre = pedir_texto_solo_letras("Nombre del Gladiador: ")

    vida_jugador = 100
    vida_enemigo = 100
    pociones = 3
    dano_base_pesado = 15
    dano_base_enemigo = 12
    turno_gladiador = True
    juego_activo = True

    print("\n=== INICIO DEL COMBATE ===")

    while juego_activo and vida_jugador > 0 and vida_enemigo > 0:
        if turno_gladiador:
            print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
            print("Elige acción:")
            print("1. Ataque Pesado")
            print("2. Ráfaga Veloz")
            print("3. Curar")

            opcion = input("Opción: ").strip()

            while (not opcion.isdigit()) or not (1 <= int(opcion) <= 3):
                if not opcion.isdigit():
                    print("Error: Ingrese un número válido.")
                else:
                    print("Error: Opción fuera de rango.")
                opcion = input("Opción: ").strip()

            opcion = int(opcion)

            if opcion == 1:
                dano_final = float(dano_base_pesado)
                if vida_enemigo < 20:
                    dano_final = dano_base_pesado * 1.5
                    print("¡Golpe Crítico!")
                vida_enemigo -= dano_final
                print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

            elif opcion == 2:
                print(">> ¡Inicias una ráfaga de golpes!")
                for _ in range(3):
                    vida_enemigo -= 5
                    print("> Golpe conectado por 5 de daño")

            else:
                if pociones > 0:
                    vida_jugador += 30
                    pociones -= 1
                    print("¡Te curaste 30 puntos de vida!")
                else:
                    print("¡No quedan pociones!")

            if vida_enemigo > 0:
                print(f">> ¡El enemigo contraataca por {dano_base_enemigo} puntos!")
                vida_jugador -= dano_base_enemigo

            turno_gladiador = True

        if vida_jugador <= 0 or vida_enemigo <= 0:
            juego_activo = False

    print("\n=== FIN DEL JUEGO ===")
    if vida_jugador > 0:
        print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
    else:
        print("DERROTA. Has caído en combate.")


def mostrar_menu():
    print("\n==============================")
    print("TP INTEGRADOR - PROGRAMACIÓN 1")
    print("Autor: Gonzalo Gabriel Mayorga")
    print("==============================")
    print("1. Ejercicio 1 - Caja del Kiosco")
    print("2. Ejercicio 2 - Acceso al Campus")
    print("3. Ejercicio 3 - Agenda de Turnos")
    print("4. Ejercicio 4 - Escape Room: La Bóveda")
    print("5. Ejercicio 5 - La Arena del Gladiador")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion_rango("Seleccione una opción: ", 1, 6)

        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        else:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    main()
