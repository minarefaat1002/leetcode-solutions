from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        def topological_sort():
            indegree = {}
            for u in graph:
                if u not in indegree:
                    indegree[u] = 0
                for v in graph[u]:
                    if v not in indegree:
                        indegree[v] = 0
                    indegree[v] += 1
            queue = deque()
            for vertex in graph:
                if indegree[vertex] == 0:
                    queue.append(vertex)
            ordering = []
            while queue:
                vertex = queue.popleft()
                ordering.append(vertex)
                for neighbour in graph[vertex]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
            return ordering
        
        ingredients = {recipes[i]: set(ingredients[i]) for i in range(len(ingredients))}
        supplies = set(supplies)
        graph = {recipe:[] for recipe in recipes}
        for u in recipes:
            for v in recipes:
                if u in ingredients[v]:
                    graph[u].append(v)
        ordering = topological_sort()
        prepared = []
        for recipe in ordering:
            if ingredients[recipe].issubset(supplies):
                prepared.append(recipe)
                supplies.add(recipe)
        return prepared
    