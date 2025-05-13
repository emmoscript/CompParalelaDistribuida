import time
import multiprocessing as mp
import numpy as np

def sum_array_sequential():
    """Versión secuencial de la suma de un array grande"""
    SIZE = 100000000
    numbers = np.ones(SIZE, dtype=np.int32)  # Array de 100 millones de unos
    
    start_time = time.time()
    total = sum(numbers)
    end_time = time.time()
    
    print(f"Suma secuencial: {total}")
    print(f"Tiempo (secuencial): {end_time - start_time:.4f} segundos")

def sum_chunk(chunk):
    """Suma un trozo del array"""
    return sum(chunk)

def sum_array_parallel():
    """Versión paralela de la suma de un array grande"""
    SIZE = 100000000
    numbers = np.ones(SIZE, dtype=np.int32)  # Array de 100 millones de unos
    
    # Determinar número de procesos
    num_processes = mp.cpu_count()
    
    # Dividir el array en trozos
    chunk_size = SIZE // num_processes
    chunks = [numbers[i:i+chunk_size] for i in range(0, SIZE, chunk_size)]
    
    start_time = time.time()
    
    # Crear pool de procesos
    with mp.Pool(processes=num_processes) as pool:
        # Aplicar la función de suma a cada trozo en paralelo
        results = pool.map(sum_chunk, chunks)
    
    # Sumar los resultados parciales
    total = sum(results)
    end_time = time.time()
    
    print(f"Suma paralela: {total}")
    print(f"Tiempo (paralelo): {end_time - start_time:.4f} segundos")
    print(f"Usando {num_processes} procesos")

# Asegúrate de usar este bloque para evitar problemas en Windows
if __name__ == "__main__":
    print("Comenzando cálculo secuencial...")
    sum_array_sequential()
    
    print("\nComenzando cálculo paralelo...")
    sum_array_parallel()
