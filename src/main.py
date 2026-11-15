from src.persistencia.binario import cargar_binario, guardar_binario
from src.persistencia.texto import cargar_csv, guardar_csv
#from src.algoritmos import ordenamiento
from src.config import TEMA
from src.dominio.cancion import Cancion
from src.dominio.Biblioteca import Biblioteca, ENCABEZADOS, RUTA_BIN, RUTA_TXT
from src.tads.cola import Cola
from src.tads.pila import Pila
from src.algoritmos.busqueda import (
    busqueda_binaria_por_id,
    busqueda_lineal_por_id,
    busqueda_lineal_por_titulo)
from src.algoritmos.ordenamiento import(
    ordenar_seleccion_por_id,
    ordenar_insercion_por_titulo
)
from src.excepciones import (
      ArchivoInvalidoError,
      ColaVaciaError,
      ColeccionLlenaError,
      PilaVaciaError,
  )

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
    """Opción 8: Cola de reproducción."""
    try:
         cancion = cola_reproduccion.desencolar()

         if cancion is None:
             print("No hay canciones en la cola.")
             return

         historial.apilar(cancion)

         print(f"Reproduciendo: {cancion.titulo} - {cancion.artista}")
    except ColaVaciaError:
        print("No hay canciones en la cola.")

def  ver_detalle():
    print("\n--- VER DETALLE DE UNA CANCIÓN ---")

    try:
        id_cancion = int(input("Ingresá el ID de la canción: "))
        cancion = biblioteca.buscar_cancion_por_id(id_cancion)

        if cancion is None:
            print("No existe una canción con ese ID.")
            return
        #guardar en el historial la canción que se está buscando
        historial.apilar(cancion)

        print(f"\nDetalle de la canción [{cancion.id}]:")
        print(f"Título: {cancion.titulo}")
        print(f"Artista: {cancion.artista}")
        print(f"Álbum: {cancion.album}")
        print(f"Año: {cancion.anio}")

    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        
def buscar():
    """Se habilita la opción buscar lineal y búsquedda binaria"""
    print("\n---Buscar Canción---")
    print("1. Buscar lineal por ID")
    print("2. Buscar lineal por título")
    print("3. Buscar binaria por ID")

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        buscar_por_id()

    elif opcion == "2":
        buscar_por_titulo()

    elif opcion == "3":
        buscar_binaria()
        #print ("Búsqueda binaria")

    else:
        print("Opción invalida.")


def buscar_por_id(): #opcion 3
    """Cumple consigna, la búsqueda está en algoritmos,
    es propia, no usa (in - .index())
    se ejecuta desde la op. Buscar del menú, recorre manualmente la colección""" 
    try:
        id_cancion = int(input("Ingresa el ID de la canción: "))

        canciones = biblioteca.obtener_canciones()

        cancion = busqueda_lineal_por_id(canciones, id_cancion)

        if cancion is None:
            print(3)
            return
        
        print(f"ID: {cancion.id}")
        print(f"Título: {cancion.titulo}")
        print(f"Artista: {cancion.artista}")
        print(f"Álbum: {cancion.album}")
        print(f"Año: {cancion.anio}")

    except ValueError:
        print("Debes ingresar un número válido.")

def buscar_por_titulo(): #opción 3

    titulo = input("Ingresa el título de la canción: ").strip()

    canciones = biblioteca.obtener_canciones ()

    cancion  = busqueda_lineal_por_titulo(canciones, titulo)

    if cancion is None:
        print("No se encontró la cancion.")
        return

    print(f"ID: {cancion.id}")
    print(f"Título: {cancion.titulo}")
    print(f"Artista: {cancion.artista}")
    print(f"Álbum: {cancion.album}")
    print(f"Año: {cancion.anio}")

def buscar_binaria():

    try:
        id_cancion = int(input("Ingresa el ID de la canción: "))

        canciones = biblioteca.obtener_canciones_como_lista()

        canciones = ordenar_seleccion_por_id(canciones)

        cancion = busqueda_binaria_por_id(canciones, id_cancion)

        if cancion is None:
            print("No se encontró la canción.")
            return

        print(f"ID: {cancion.id}")
        print(f"Título: {cancion.titulo}")
        print(f"Artista: {cancion.artista}")
        print(f"Album: {cancion.album}")
        print(f"Año: {cancion.anio}")

    except ValueError:
        print("Debes ingresar un número válido.")

def ordenar():

    print("\n ---Ordenar---")
    print("1. Selection Sort por ID")
    print("2. Insertion Sort por título")

    opcion = input("> ").strip()

    canciones = biblioteca.obtener_canciones_como_lista()

    if opcion == "1":

        canciones = ordenar_seleccion_por_id(canciones
    )

    elif opcion == "2":

        canciones = ordenar_insercion_por_titulo(canciones
    )
    else:
        print("Opción inválida.")
        return

    print("\n ---Resultado---")

    for cancion in canciones:
        print(
            f"{cancion.id} -"
            f"{cancion.titulo} "
        )


def gestionar_abm_coleccion():
    """Opción 6: Alta, Baja y Modificación persistentes."""
    print("\n--- ABM DE CANCIONES (PERSISTENTE) ---")
    print("1. Alta (agregar nueva canción)")
    print("2. Baja (eliminar canción por ID)")
    print("3. Modificación (editar título por ID - Acceso directo)")
    print("4. Encolar canción existente para reproducir")
    sub = input("Elegí una opción: ").strip()

    try:
        if sub == "1":
            id_nueva = int(input("ID de la nueva canción: "))
            if biblioteca.buscar_cancion_por_id(id_nueva) is not None:
                print("Ya existe una canción con ese ID.")
                return
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            album = input("Álbum: ").strip()
            anio = int(input("Año: "))

            nueva = Cancion(id_nueva, titulo, artista, album, anio)
            biblioteca.agregar_cancion(nueva)
            print(f"Canción '{titulo}' agregada y guardada en disco.")

        elif sub == "2":
            id_borrar = int(input("ID de la canción a eliminar: "))
            if biblioteca.eliminar_cancion(id_borrar):
                print("Canción eliminada y archivos actualizados.")
            else:
                print("No se encontró una canción con ese ID.")

        elif sub == "3":
            id_mod = int(input("ID de la canción a modificar: "))
            nuevo_titulo = input("Nuevo título: ").strip()
            if biblioteca.modificar_titulo(id_mod, nuevo_titulo):
                print(
                    "Título modificado (registro actualizado en binario y texto)."
                )
            else:
                print("No se encontró una canción con ese ID.")

        elif sub == "4":
            id_elem = int(input("Ingresá el ID a encolar: "))
            cancion = biblioteca.buscar_cancion_por_id(id_elem)
            if cancion is None:
                print("No existe una canción con ese ID.")
                return
            cola_reproduccion.encolar(cancion)
            print(f"Encolada: {cancion.titulo}")
        else:
            print("Subopción inválida.")

    except ValueError:
        print("Error: Debes ingresar un valor numérico válido.")
    except ColeccionLlenaError as e:
        print(f"Error: {e}")
    except ArchivoInvalidoError as e:
        print(f"Error de archivo: {e}")

def listar_catalogo():
    canciones = biblioteca.obtener_canciones()
    print("--- CATALOGO DE CANCIONES ---")
    # Usamos atributos de objeto (POO)
    for item in canciones:
        #print(type(item))
        print(f"{item.id:>2} {item.titulo} {item.artista} ({item.album}, {item.anio})")
    print("Esto es todo por ahora")


def operacion_recursiva():
    """Función para probar el Ítem 5: Recursión del dominio."""
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
    print("6. Colección principal (playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def mostrar_historial():
    try:
        ultima = historial.ver_tope()

        if ultima is None:
            print("No hay canciones en el historial.")
            return

        print(f"Última canción escuchada: "
              f"{ultima.titulo} - {ultima.artista} "
              f"({ultima.album} - {ultima.anio})")
            
    except PilaVaciaError:
        print("No hay canciones en el historial.")

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
        elif opcion == "3":
            buscar()
        elif opcion == "4":
            ordenar()
        elif opcion == "5":
            operacion_recursiva() # Ahora ejecuta la función recursiva       
        elif opcion == "6":
            gestionar_abm_coleccion()
        elif opcion == "7":
            mostrar_historial()
        elif opcion == "8":
            atender_cola()
        elif opcion == "9":
            print("\n--- ARCHIVOS ---")
            print("a) Cargar catálogo desde texto")
            print("b) Guardar catálogo en texto")
            print("c) Guardar catálogo en binario")
            print("d) Cargar catálogo desde binario")

            sub = input("subopción > ").strip().lower()
            try:
                if sub == "a":
                    biblioteca.cargar_desde_csv(RUTA_TXT)
                    print(
                        f"Catálogo cargado desde texto ({biblioteca.canciones.tamanio()} canciones)."
                    )
                elif sub == "b":
                    guardar_csv(
                        RUTA_TXT, biblioteca.obtener_filas(), ENCABEZADOS
                    )
                    print("Catálogo guardado en texto.")
                elif sub == "c":
                    guardar_binario(RUTA_BIN, biblioteca.obtener_canciones())
                    print("Catálogo guardado en binario.")
                elif sub == "d":
                    biblioteca.canciones = cargar_binario(RUTA_BIN)
                    print(
                        f"Catálogo cargado desde binario ({biblioteca.canciones.tamanio()} canciones)."
                    )
                else:
                    print("Subopción inválida.")
            except ArchivoInvalidoError as e:
                print(f"Archivo inválido: {e}")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
