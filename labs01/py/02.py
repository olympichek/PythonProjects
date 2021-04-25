from math import sqrt

def pointsToEdges(points):
    n = len(points)
    if n < 2: return []
    edges = [(points[0], points[n - 1])]
    for i in range(0, n - 1):
        edges.append((points[i], points[i + 1]))
    return edges

def calcDistance(edge):
    (x1, y1), (x2, y2) = edge
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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
