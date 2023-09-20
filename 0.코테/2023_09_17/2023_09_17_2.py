# 인프런 다익스트라

import heapq
from collections import defaultdict


def dijkstra(times, n, k):
    grpah = defaultdict(list)

    for time in times:
        grpah[time[0]].append((time[2], time[1]))

    costs = {}
    pq = []

    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)

        if cur_v not in costs:
            costs[cur_v] = cur_cost

            for cost, next_v in grpah[cur_v]:
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_v))

    for node in range(1, n + 1):
        if node not in costs:
            return -1

    return max(costs.values())


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]

print(dijkstra(times, 4, 2))
