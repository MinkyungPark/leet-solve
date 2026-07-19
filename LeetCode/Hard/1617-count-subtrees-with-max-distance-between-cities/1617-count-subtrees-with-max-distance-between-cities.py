from collections import deque


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. 2 BFS per subset
        # subset > 2^n, O(2^n * 2n)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        def bfs(start, mask):
            q = deque([(start, 0)])
            visited_mask = 1 << start

            leaf_node = start
            max_dist = 0

            while q:
                u, dist = q.popleft()

                if dist > max_dist:
                    leaf_node = u
                    max_dist = dist
                
                for v in graph[u]:
                    if (
                        not (mask & (1 << v)) # not in subset mask
                        or visited_mask & (1 << v) # visited
                    ):
                        continue
                    
                    visited_mask |= (1 << v)
                    q.append((v, dist + 1))
                    
            return visited_mask, leaf_node, max_dist
        
        answer = [0] * (n - 1)
        for mask in range(1, 1 << n):
            if mask.bit_count() < 2:
                continue

            start = (mask & -mask).bit_length() - 1 # any node in subset
            visited_mask, leaf_node, _ = bfs(start, mask) # check if subset is connected

            if visited_mask != mask:
                continue
            
            _, _, dist = bfs(leaf_node, mask) # get dist from leaf node

            answer[dist - 1] += 1
        
        return answer


# 2. 1 BFS + tree DP
# O(2^n × n)
# DFS = connection check + (diameter = longest diameter + 2nd longest diamenter)
class Solution2:
    def countSubgraphsForEachDiameter(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1

            graph[u].append(v)
            graph[v].append(u)

        answer = [0] * (n - 1)

        def get_diameter(mask):
            start = (mask & -mask).bit_length() - 1

            visited_count = 0
            diameter = 0

            def dfs(node, parent):
                nonlocal visited_count, diameter

                visited_count += 1

                longest = 0
                second_longest = 0

                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue

                    if not (mask & (1 << neighbor)):
                        continue

                    child_depth = dfs(neighbor, node) + 1

                    if child_depth > longest:
                        second_longest = longest
                        longest = child_depth
                    elif child_depth > second_longest:
                        second_longest = child_depth

                # 현재 노드를 지나가는 가장 긴 경로
                diameter = max(
                    diameter,
                    longest + second_longest
                )

                # 현재 노드에서 아래로 내려가는 가장 긴 거리
                return longest

            dfs(start, -1)

            # 선택한 노드를 모두 방문하지 못했다면 연결되지 않음
            if visited_count != mask.bit_count():
                return -1

            return diameter

        for mask in range(1, 1 << n):
            if mask.bit_count() < 2:
                continue

            diameter = get_diameter(mask)

            if diameter == -1:
                continue

            answer[diameter - 1] += 1

        return answer

# 3. Floyd–Warshall
# dist preprocessing: O(n³)
# subset check: O(2^n × n²)
# total: O(n³ + 2^n × n²)
class Solution3:
    def countSubgraphsForEachDiameter(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[int]:

        normalized_edges = []
        distance = [[float("inf")] * n for _ in range(n)]

        for node in range(n):
            distance[node][node] = 0

        for u, v in edges:
            u -= 1
            v -= 1

            normalized_edges.append((u, v))

            distance[u][v] = 1
            distance[v][u] = 1

        # 모든 노드 쌍의 최단 거리 계산
        for middle in range(n):
            for start in range(n):
                for end in range(n):
                    distance[start][end] = min(
                        distance[start][end],
                        distance[start][middle]
                        + distance[middle][end]
                    )

        answer = [0] * (n - 1)

        for mask in range(1, 1 << n):
            node_count = mask.bit_count()

            if node_count < 2:
                continue

            edge_count = 0

            # 선택된 노드 사이의 간선 개수 계산
            for u, v in normalized_edges:
                if (
                    mask & (1 << u)
                    and mask & (1 << v)
                ):
                    edge_count += 1

            # 원래 그래프가 트리이므로 선택한 부분 그래프도 forest
            # 노드 k개와 간선 k-1개라면 연결된 트리
            if edge_count != node_count - 1:
                continue

            selected_nodes = [
                node
                for node in range(n)
                if mask & (1 << node)
            ]

            diameter = 0

            # 선택된 노드 사이의 최대 거리 계산
            for i in range(len(selected_nodes)):
                for j in range(i + 1, len(selected_nodes)):
                    u = selected_nodes[i]
                    v = selected_nodes[j]

                    diameter = max(
                        diameter,
                        distance[u][v]
                    )

            answer[diameter - 1] += 1

        return answer