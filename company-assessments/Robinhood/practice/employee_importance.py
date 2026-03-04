"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        visited = {}
        emp_map = {emp.id: emp for emp in employees}
        self.dfs(emp_map, emp_map[id], visited)
        
        return sum(visited.values())
    
    # def _find_employee(self, employees, id):
    #     i = 0
    #     while i < len(employees) and employees[i].id != id: 
    #         i += 1
    #     if i < len(employees):
    #         return employees[i]
    #     return -1

    def dfs(self, emp_map, node, visited):
        visited[node.id] = node.importance
        
        neighbors = node.subordinates
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(emp_map, emp_map[neighbor], visited)
        return visited
            