class Size:

	def get_size(self):
		return self._size

	def get_scale(self):
		return self._scale

class Small(Size):
	_size = "Small"
	_scale = 0.6

class Medium(Size):
	_size = "Medium"
	_scale = 0.8

class Large(Size):
	_size = "Large"
	_scale = 1.0

class Tiny(Size):
	_size = "Tiny"
	_scale = 0.5