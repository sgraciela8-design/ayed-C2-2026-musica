from src.config import TEMA
from src.dominio.Biblioteca import Biblioteca

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

# Instanciamos la clase Biblioteca
biblioteca = Biblioteca()


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def listar_catalogo():
    canciones = biblioteca.obtener_canciones()
    print("--- CATALOGO DE CANCIONES ---")
    # Usamos atributos de objeto (POO)
    for item in canciones:
        print(f"{item.id:>2} {item.titulo} - {item.artista} ({item.album}, {item.anio})")
    print("Esto es todo por ahora")


def operacion_recursiva():
    """Función para probar el Ítem 2: Recursión del dominio."""
    print("\n--- BUSCAR VERSIONES/DERIVADOS (RECURSIVO) ---")
    try:
        id_cancion = int(input("Ingresá el ID de la canción inicial: "))
        versiones = biblioteca.obtener_todas_las_versiones_recursivo(id_cancion)
        if versiones:
            print(f"\nVersiones encontradas ({len(versiones)}):")
            for v in versiones:
                print(f" -> [{v.id}] {v.titulo} - {v.artista}")
        else:
            print("\nEsta canción no tiene versiones o derivados (Caso Base cumplido).")
    except ValueError:
        print("Error: Debes ingresar un número de ID válido.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo()
        elif opcion == "5":
            operacion_recursiva()  # Ahora ejecuta la función recursiva
        elif opcion in {"2", "3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()