# EJEMPLO 2: COMPUTACIÓN DISTRIBUIDA SIMULADA
# Cálculo distribuido de pi usando el método de Monte Carlo
import random
import math
import time
import multiprocessing as mp

def calculate_pi_chunk(points):
    """Calcula puntos dentro del círculo para un número dado de puntos totales"""
    points_in_circle = 0
    for _ in range(points):
        # Generar punto aleatorio en el cuadrado unitario
        x = random.random()
        y = random.random()
        
        # Verificar si el punto está dentro del círculo unitario
        if x*x + y*y <= 1.0:
            points_in_circle += 1
            
    return points_in_circle

def calculate_pi_sequential(total_points):
    """Calcula pi secuencialmente"""
    start_time = time.time()
    
    points_in_circle = calculate_pi_chunk(total_points)
    pi_estimate = 4.0 * points_in_circle / total_points
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"Estimación de π (secuencial): {pi_estimate}")
    print(f"Valor real de π: {math.pi}")
    print(f"Error: {abs(pi_estimate - math.pi)}")
    print(f"Tiempo de ejecución (secuencial): {elapsed:.4f} segundos")

def calculate_pi_distributed(total_points):
    """Calcula pi con simulación de distribución usando multiprocesamiento"""
    # Número de procesos = núcleos disponibles
    num_processes = mp.cpu_count()
    
    # Puntos por proceso
    points_per_process = total_points // num_processes
    
    print(f"Simulando computación distribuida con {num_processes} procesos")
    
    start_time = time.time()
    
    # Crear pool de procesos
    with mp.Pool(processes=num_processes) as pool:
        # Cada proceso calcula su parte
        points_list = [points_per_process] * num_processes
        results = pool.map(calculate_pi_chunk, points_list)
    
    # Sumar todos los puntos dentro del círculo
    total_points_in_circle = sum(results)
    
    # Calcular estimación final de pi
    pi_estimate = 4.0 * total_points_in_circle / total_points
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"Estimación de π (distribuido): {pi_estimate}")
    print(f"Valor real de π: {math.pi}")
    print(f"Error: {abs(pi_estimate - math.pi)}")
    print(f"Tiempo de ejecución (distribuido): {elapsed:.4f} segundos")

def main_distributed():
    total_points = 100000000  # 100 millones de puntos
    
    print("Cálculo secuencial de π...")
    calculate_pi_sequential(total_points)
    
    print("\nCálculo distribuido de π...")
    calculate_pi_distributed(total_points)

if __name__ == "__main__":
    print("=== EJEMPLO DE COMPUTACIÓN DISTRIBUIDA ===")
    main_distributed()
