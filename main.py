import math
import random
import time


def generate_digraph(v, e, max_weight):
    graph = []
    for i in range(0, v):  # инициализация матрицы смежности
        graph.append([])
        for j in range(0, v):
            if i == j:
                graph[i].append(0)
            else:
                graph[i].append(math.inf)

    for i in range(0, v-1):  # для связности графа
        graph[i][i+1] = random.randint(1, max_weight)

    if v-1 < e:  # добавляем недостающие ребра
        for i in range(v-1, e):
            row = random.randint(0, max_weight) % v
            col = random.randint(0, max_weight) % v
            if graph[row][col] == math.inf and row != col:
                graph[row][col] = random.randint(1, max_weight)
            else:
                while graph[row][col] != math.inf or row == col:
                    row = random.randint(0, max_weight) % v
                    col = random.randint(0, max_weight) % v
                graph[row][col] = random.randint(1, max_weight)
    return graph


def generate_graph(v, e, max_weight):
    graph = []
    for i in range(0, v):  # инициализация матрицы смежности
        graph.append([])
        for j in range(0, v):
            if i == j:
                graph[i].append(0)
            else:
                graph[i].append(math.inf)
    for i in range(0, e):
        row = random.randint(0, max_weight) % v
        col = random.randint(0, max_weight) % v
        if graph[row][col] == math.inf and graph[col][row] == math.inf and row != col and row < col:
            graph[row][col] = random.randint(1, max_weight)
            graph[col][row] = graph[row][col]
        else:
            while graph[row][col] != math.inf and graph[col][row] != math.inf or row == col and row > col:
                row = random.randint(0, max_weight) % v
                col = random.randint(0, max_weight) % v
            graph[row][col] = random.randint(1, max_weight)
            graph[col][row] = graph[row][col]
    return graph


def floyd(v, graph):
    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


print('input number of vertices: ')
number_of_vertices = int(input())
print('input number of edges: ')
number_of_edges = int(input())
max_weight = 100
print('press 1 for directed weighted graph, press 2 for weighted graph: ')
graph_class = input()
if number_of_edges < number_of_vertices - 1:
    print('not enough edges')
else:
    if graph_class == '1':
        if number_of_edges > number_of_vertices * (number_of_vertices - 1):
            print('too many edges')
        else:
            graph = generate_digraph(number_of_vertices, number_of_edges, max_weight)
    elif graph_class == '2':
        if number_of_edges > number_of_vertices * (number_of_vertices - 1) / 2:
            print('too many edges')
        else:
            graph = generate_graph(number_of_vertices, number_of_edges, max_weight)
print('generated graph: ', graph)
start = time.time()
matrix = floyd(number_of_vertices, graph)
end = time.time() - start
print('result of the algorythm: ', matrix)
print('time: ', end)
