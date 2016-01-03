# 最大公約数を求める
def gcd(x, y):
	while y:
		x, y = y, x % y
	return x

