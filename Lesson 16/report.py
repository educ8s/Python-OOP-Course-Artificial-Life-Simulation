class CellReport:

    def __init__(self):
        self.__cells = []
 
    def update(self, cells_list):
        self.__cells = cells_list

    def print(self):
        print("\n\nCell Report:")
        print("--------------") 
        for cell in self.__cells:
            print(f"Cell ID: {cell.get_id()} Position: {cell.get_position():<12}  Type: {cell.get_type():<8} Energy: {cell.get_energy_level()}")

class HealthReport:

    def __init__(self):
        self.__cells = []

    def update(self, cells_list):
        self.__cells = cells_list

    def print(self):
        print("\n\nHealth Report:")
        print("--------------") 
        for cell in self.__cells:
            print(f"Cell ID: {cell.get_id():<3} Type: {cell.get_type():<8} Energy: {cell.get_energy_level()}")