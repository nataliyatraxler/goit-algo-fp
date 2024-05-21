import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))  # Якщо граф орієнтований, видаліть цей рядок

    def dijkstra(self, start_vertex):
        # Ініціалізація відстаней до нескінченності і відстані до стартової вершини як 0
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start_vertex] = 0
        
        # Використання бінарної купи для вибору найближчої вершини
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо знайдений шлях довший за вже знайдений, пропускаємо його
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях до сусіда, оновлюємо його відстань
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = graph.dijkstra(start_vertex)

print(f"Відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"До вершини {vertex}: {distance}")