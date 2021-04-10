from math import sqrt

def calcDistance(points_pair):
    p1, p2 = points_pair
    d1 = p1[0] - p2[0]
    d2 = p1[1] - p2[1]
    return sqrt(d1 ** 2 + d2 ** 2)

def pointsToEdges(points):
    n = len(points)
    if n < 2: return []
    edges = [(points[0], points[n - 1])]
    for i in range(0, n - 1):
        edges.append((points[i], points[i + 1]))
    return edges

def calcPerimeter(edges):
    return sum(map(calcDistance, edges))

def getPoints():
    points = []
    while True:
        line = input("Enter point coordinates: ")
        if not line: break
        x, y = tuple(map(float, line.split()))
        points.append((x, y))
    return points

points    = getPoints()
edges     = pointsToEdges(points)
perimeter = calcPerimeter(edges)
print("Perimeter:", perimeter)
