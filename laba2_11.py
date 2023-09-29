import threading
import time

def find_sum(arr):
    return sum(arr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 4  # Количество потоков

start_time = time.time() # время старта
threads = []
results = []

# Вычисляем размер фрагмента для каждого потока
chunk_size = len(arr) // N
remainder = len(arr) % N

for i in range(N):
    # Вычисляем начальный и конечный индексы для каждого потока
    start = i * chunk_size
    end = start + chunk_size

    # Распределяем оставшиеся элементы
    if i == N - 1:
        end += remainder

    # запуск каждого потока
    thread = threading.Thread(target=lambda r=arr[start:end]: results.append(find_sum(r)))
    thread.start()
    threads.append(thread)

# завершение всех потоков
for thread in threads:
    thread.join()

# окончательная сумму по результатам
final_sum = sum(results)

end_time = time.time() # конечное время
execution_time = end_time - start_time

print("Sum:", final_sum)
print("Execution Time:", execution_time, "seconds")
