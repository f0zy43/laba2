import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

def main():
    N = int(input("кол-во точек: "))
    points = []

    for _ in range(N):
        coordinates = input("Введите координаты (x,y,z): ").split(',')
        x, y, z = map(float, coordinates)
        points.append(Vector(x, y, z))

    # Найдем точку, наиболее удаленную от начала координат
    furthest_point = max(points, key=lambda point: point.magnitude())
    print("Точка, наиболее удаленная от начала координат:", furthest_point)

    # подсчет центра масс
    center_of_mass = sum(points, Vector(0, 0, 0)) * (1 / N)
    print("Центр масс:", center_of_mass)

    if N >= 2:
        v1 = points[0]
        v2 = points[1]
        parallelogram_area = abs(v1.x * v2.y - v1.y * v2.x)
        print("Площадь параллелограмма:", parallelogram_area)

    if N == 3:
        v1 = points[0]
        v2 = points[1]
        v3 = points[2]
        parallelepiped_volume = abs(v1.x * (v2.y * v3.z - v2.z * v3.y) + v1.y * (v2.z * v3.x - v2.x * v3.z) + v1.z * (v2.x * v3.y - v2.y * v3.x))
        print("Объем параллелепипеда:", parallelepiped_volume)

    if N >= 3:
        # Найдем три точки, образующие треугольник с наибольшим периметром
        max_perimeter = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    perimeter = (points[i] - points[j]).magnitude() + (points[j] - points[k]).magnitude() + (points[k] - points[i]).magnitude()
                    max_perimeter = max(max_perimeter, perimeter)
        print("Самый большой периметр среди треугольников:", max_perimeter)

        # Найдем три точки, образующие треугольник с наибольшей площадью
        max_area = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    area = 0.5 * abs((points[j] - points[i]).magnitude() * (points[k] - points[i]).magnitude() * math.sin(math.acos((points[j] - points[i]).dot(points[k] - points[i]) / ((points[j] - points[i]).magnitude() * (points[k] - points[i]).magnitude()))))
                    max_area = max(max_area, area)
        print("Самая большая площадь среди треугольников:", max_area)

if __name__ == "__main__":
    main()