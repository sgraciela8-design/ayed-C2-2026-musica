import time
from src.dominio.Biblioteca import Biblioteca
from src.algoritmos.busqueda import busqueda_lineal_por_id, busqueda_binaria_por_id
from src.algoritmos.ordenamiento import ordenar_seleccion_por_id, ordenar_insercion_por_titulo

# 1. Cargamos el catálogo original (n)
biblioteca = Biblioteca()
canciones_n1 = biblioteca.obtener_canciones_como_lista()

# 2. Creamos la copia agrandada multiplicando por 10 (n x 10)
canciones_n10 = canciones_n1 * 10

print(f"Tamaño original (n): {len(canciones_n1)} canciones")
print(f"Tamaño agrandado (n x 10): {len(canciones_n10)} canciones\n")

# --- MEDIDA 1: BÚSQUEDA LINEAL ---
# Tamaño n
inicio = time.perf_counter()
busqueda_lineal_por_id(canciones_n1, 5)
fin = time.perf_counter()
t_lin_n1 = fin - inicio

# Tamaño n x 10
inicio = time.perf_counter()
busqueda_lineal_por_id(canciones_n10, 5)
fin = time.perf_counter()
t_lin_n10 = fin - inicio

# --- MEDIDA 2: BÚSQUEDA BINARIA ---
# Para la binaria pre-ordenamos las listas para cumplir la regla
lista_ord_n1 = ordenar_seleccion_por_id(canciones_n1.copy())
lista_ord_n10 = ordenar_seleccion_por_id(canciones_n10.copy())

# Tamaño n
inicio = time.perf_counter()
busqueda_binaria_por_id(lista_ord_n1, 5)
fin = time.perf_counter()
t_bin_n1 = fin - inicio

# Tamaño n x 10
inicio = time.perf_counter()
busqueda_binaria_por_id(lista_ord_n10, 5)
fin = time.perf_counter()
t_bin_n10 = fin - inicio

# --- MEDIDA 3: SELECTION SORT ---
# Tamaño n
inicio = time.perf_counter()
ordenar_seleccion_por_id(canciones_n1.copy())
fin = time.perf_counter()
t_sel_n1 = fin - inicio

# Tamaño n x 10
inicio = time.perf_counter()
ordenar_seleccion_por_id(canciones_n10.copy())
fin = time.perf_counter()
t_sel_n10 = fin - inicio

# --- MEDIDA 4: INSERTION SORT ---
# Tamaño n
inicio = time.perf_counter()
ordenar_insercion_por_titulo(canciones_n1.copy())
fin = time.perf_counter()
t_ins_n1 = fin - inicio

# Tamaño n x 10
inicio = time.perf_counter()
ordenar_insercion_por_titulo(canciones_n10.copy())
fin = time.perf_counter()
t_ins_n10 = fin - inicio

# --- RESULTADOS PARA IMPRIMIR EN PANTALLA ---
print("=== RESULTADOS PARA EL INFORME ===")
print(f"Búsqueda lineal (n={len(canciones_n1)}): {t_lin_n1:.8f} s")
print(f"Búsqueda lineal (n={len(canciones_n10)}): {t_lin_n10:.8f} s\n")

print(f"Búsqueda binaria (n={len(canciones_n1)}): {t_bin_n1:.8f} s")
print(f"Búsqueda binaria (n={len(canciones_n10)}): {t_bin_n10:.8f} s\n")

print(f"Selection Sort (n={len(canciones_n1)}): {t_sel_n1:.8f} s")
print(f"Selection Sort (n={len(canciones_n10)}): {t_sel_n10:.8f} s\n")

print(f"Insertion Sort (n={len(canciones_n1)}): {t_ins_n1:.8f} s")
print(f"Insertion Sort (n={len(canciones_n10)}): {t_ins_n10:.8f} s")
