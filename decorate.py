def test(func):
	def new_func(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return new_func


