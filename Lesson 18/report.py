class Report:
	def __init__(self):
		self._cells = []

	def update(self, cells_list):
		self._cells = cells_list


class CellReport(Report):

	def print(self):
		print("\n\nCell Report:")
		print("--------------")
		for cell in self._cells:
			print(f"Cell ID: {cell.get_id():<3} Position: {cell.get_position():<12} Type: {cell.get_type():<8} Energy: {cell.get_energy_level():<8}")

class HealthReport(Report):

	def print(self):
		print("\n\nHealth Report:")
		print("--------------")
		for cell in self._cells:
			print(f"Cell ID: {cell.get_id():<3} Type: {cell.get_type():<8} Energy: {cell.get_energy_level():<8}")