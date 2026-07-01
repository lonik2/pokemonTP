from pokemon import (Pokedex, Registro_medallas, lista_lideres, equipo, pc, centro_pokemon, transferencias, capturar_pokemon, curar, transferir_pokemon, deshacer_transferencia, desafiar_lider, ver_equipo, ver_registro, ver_pc, ordenar_pc, buscar_en_equipo, consultar_pokedex)


def menu():
    while True:
        print("")
        print("---POKEMON---")
        print("1. Capturar Pokemon")
        print("2. Ver equipo")
        print("3. Curar equipo")
        print("4. Ver PC")
        print("5. Ordenar PC")
        print("6. Transferir Pokemon al Profesor Oak")
        print("7. Deshacer ultima transferencia")
        print("8. Desafiar lider de gimnasio")
        print("9. Ver registro de medallas")
        print("10. Buscar Pokemon en equipo")
        print("11. Consultar pokedex")
        print("12. Ver pokedex completa")
        print("13. Salir")

        opcion = input("Elegi una opción: ").strip()

        if opcion == "1":
            capturar_pokemon(Pokedex, equipo, pc)

        elif opcion == "2":
            ver_equipo()

        elif opcion == "3":
            if not equipo:
                print("Tu equipo esta vacio")
            else:
                curar(equipo, centro_pokemon)

        elif opcion == "4":
            ver_pc(pc)

        elif opcion == "5":
            ordenar_pc(pc)

        elif opcion == "6":
            transferir_pokemon(pc, transferencias)

        elif opcion == "7":
            deshacer_transferencia(pc, transferencias)

        elif opcion == "8":
            desafiar_lider(lista_lideres, Registro_medallas)

        elif opcion == "9":
            ver_registro(lista_lideres, Registro_medallas)

        elif opcion == "10":
            buscar_en_equipo(equipo)

        elif opcion == "11":
            consultar_pokedex(Pokedex)

        elif opcion == "12":
            print("---Pokedex Nacional---")
            Pokedex.mapa()

        elif opcion == "13":
            print("Hasta luego")
            break

        else:
            print("Opcion invalida.")


menu()