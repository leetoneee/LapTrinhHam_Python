import math

def main():
	a = float(input("Nhap a: "))
	b = float(input("Nhap b: "))
	c = float(input("Nhap c: "))

	delta = b * b - 4 * a * c
	if (delta != 0):
		if (delta > 0):
			x1 = (- b - math.sqrt(delta)) / (2 * a)
			x2 = (- b + math.sqrt(delta)) / (2 * a)
			print(x1, x2)
		else:
			print("VN")
	else:
		x0 = - b / (2 * a)
		print(x0)

if __name__ == "__main__":
    main()