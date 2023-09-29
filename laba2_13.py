import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)

"""list пуст, потому что у каждого процесса есть свое собственное пространство памяти, и они не используют одно и то же 

пространство памяти совместно. В этом коде модуль многопроцессорной обработки используется для создания нескольких процессов. 

Каждый процесс имеет свою собственную копию объекта list, и когда рабочая функция добавляет элемент в list, 

она добавляет его к своей собственной копии списка, а не к глобальному объекту list."""