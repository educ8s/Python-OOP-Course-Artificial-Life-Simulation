class Report:
    def __init__(self, cells_list):
        self.cells = cells_list

    def update(self, cells_list):
        self.cells = cells_list

class CellReport(Report):
    def print(self):
        print("\n\nCell Report:")
        print("------------")
        for cell in self.cells:
            print(f"Cell ID: {cell.id}, Position: ({int(cell.x)}, {int(cell.y)}), Type: {cell.type}, Size: {cell.size.get_size()} Energy: {cell.energy}")

class HealthReport(Report):
    def print(self):
        print("\n\nHealth Report:")
        print("--------------")
        for cell in self.cells:
            print(f"Cell ID: {cell.id:<3} Type: {cell.type:<8} Energy: {cell.energy:<3}")