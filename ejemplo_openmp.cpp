#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    int n = 100;
    std::vector<int> data(n);

    #pragma omp parallel for
    for (int i = 0; i < n; ++i) {
        data[i] = i * 2;
        // El siguiente código muestra el ID del hilo que ejecuta cada iteración (opcional)
        int thread_id = omp_get_thread_num();
        std::cout << "Thread " << thread_id << " processed index " << i << std::endl;
    }

    // Imprimir los primeros elementos para verificar (opcional)
    for (int i = 0; i < 5; ++i) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
