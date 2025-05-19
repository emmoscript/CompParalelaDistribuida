#include <iostream>
#include <vector>
#include <tbb/tbb.h>

int main() {
    int n = 100;
    std::vector<int> data(n);

    tbb::parallel_for(tbb::blocked_range<int>(0, n),
        [&](const tbb::blocked_range<int>& r) {
            for (int i = r.begin(); i!= r.end(); ++i) {
                data[i] = i * 2;
                // El siguiente código muestra el ID del hilo que ejecuta cada iteración (opcional)
                int thread_id = tbb::this_task_arena::current_thread_index();
                std::cout << "Thread " << thread_id << " processed index " << i << std::endl;
            }
        });

    // Imprimir los primeros elementos para verificar (opcional)
    for (int i = 0; i < 5; ++i) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
