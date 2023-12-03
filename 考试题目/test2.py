# import heapq
#
#
# def dijkstra(graph, start):
#     # 获取图的节点数量
#     n = len(graph)
#
#     # 初始化距离数组，用 -1 表示尚未到达的节点
#     dist = [-1] * n
#     # 起始节点到自身的距离为 0
#     dist[start] = 0
#
#     # 使用堆来实现优先队列，初始化堆为包含起始节点和距离的元组
#     heap = [(0, start)]
#
#     # 主循环，直到堆为空
#     while heap:
#         # 弹出当前堆中距离最小的节点及其距离
#         d, node = heapq.heappop(heap)
#
#         # 如果该节点已经被访问过，跳过
#         if dist[node] < 0:
#             # 更新节点的最短距离
#             dist[node] = d
#
#             # 遍历该节点的邻居
#             for neighbor, weight in graph[node]:
#                 # 如果邻居节点尚未被访问过，将其加入堆中
#                 if dist[neighbor] < 0:
#                     heapq.heappush(heap, (d + weight, neighbor))
#
#     # 返回最短路径长度数组
#     return dist
#
#
# def main():
#     # 输入图的节点数和边数
#     n, m = map(int, input("输入节点数和边数: ").split())
#
#     # 初始化图的邻接表
#     graph = [[] for _ in range(n)]
#     print(graph)
#
#     # 输入边的信息，构建图的邻接表
#     for _ in range(m):
#         u, v, w = map(int, input().split())
#         # 注意：节点编号从1开始，而Python中索引从0开始，需要减1
#         graph[u - 1].append((v - 1, w))
#         print(graph)
#
#     # 调用 Dijkstra 算法计算最短路径
#     shortest_paths = dijkstra(graph, 0)
#
#     # 输出最短路径长度数组
#     for dist in shortest_paths:
#         print(dist, end=" ")
#
#
# if __name__ == "__main__":
#     main()


import heapq

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

def dijkstra(start, graph, distances):
    n = len(graph)
    pq = []

    distances[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist_u, u = heapq.heappop(pq)

        if dist_u > distances[u]:
            continue

        for edge in graph[u]:
            v, weight = edge.to, edge.weight

            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))

def main():
    n, m = map(int, input().split())
    # print(m, n)

    graph = [[] for _ in range(n + 1)]  # 1-indexed graph
    distances = [float('inf')] * (n + 1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Edge(v, w))
        print(graph)

    dijkstra(1, graph, distances)

    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            print("-1", end=" ")
        else:
            print(distances[i], end=" ")

    print()

if __name__ == "__main__":
    main()
