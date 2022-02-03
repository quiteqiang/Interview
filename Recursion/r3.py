class Employee:
    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]

mp = {employee.id: employee for employee in employees}

print(mp)
