from src.config import TEMA
from src.dominio.Biblioteca import Biblioteca
from src.tads.cola import Cola
from src.tads.pila import Pila
from src.excepciones import ColaVaciaError, PilaVaciaError, ColeccionLlenaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

biblioteca = Biblioteca()#Instanciamos la clase Biblioteca
historial = Pila()
cola_reproduccion = Cola()


def ejecutar_historial():
    """Opción 7: Historial (pila) para deshacer."""
    try:
        accion = historial.desapilar()
        print(f"Acción deshecha: {accion}")
    except PilaVaciaError:
        print("No hay acciones en el historial para deshacer.")

def atender_cola():
    """Opción 8: Cola para atención/turnos."""
    try:
        elemento = cola_reproduccion.desencolar()
        print(f"Atendiendo/reproduciendo: {elemento}")
    except ColaVaciaError:
        print("No hay elementos en la cola.")

#def pendiente():
   # print("Todavía no está implementado. Completae en la entrega que corresponde.")


def agregar_a_coleccion_principal():
    """Opción 6: Colección principal (playlist / equipo de 6)."""
    # Ejemplo solicitando id o elemento a agregar
    id_elem = input("Ingresá el ID a agregar a la colección: ").strip()
    try:
        # Aquí llamas al método de tu biblioteca/colección que agrega
        biblioteca.agregar_cancion(id_elem)
        print("Elemento agregado exitosamente.")
    except ColeccionLlenaError:
        print("El equipo está lleno (máximo 6). No se puede agregar más.")


def listar_catalogo():
    canciones = biblioteca.obtener_canciones()
    print("--- CATALOGO DE CANCIONES ---")
    # Usamos atributos de objeto (POO)
    for item in canciones:
        #print(type(item))
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

def mostrar_historial():
    if historial.esta_vacia():
        print("No hay canciones en el historial. ")
        return

    print("Última canción escuchada: ")
    print(historial.ver_tope())

def mostrar_cola():
    if cola_reproduccion.esta_vacia():
       print("La cola está vacía.")
       return

    print("Próxima canción:")
    print(cola_reproduccion.ver_frente())


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
        elif opcion == "2":
             ver_detalle() 
        elif opcion == "5":
            operacion_recursiva() # Ahora ejecuta la función recursiva       
        elif opcion == "6":
            agregar_a_coleccion_principal()
        elif opcion == "7":
            mostrar_historial()
        elif opcion == "8":
            mostrar_cola()
        elif opcion in { "3","4","9"}:
            print("Todavía no está implementado. Completae en la entrega que corresponde.")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
