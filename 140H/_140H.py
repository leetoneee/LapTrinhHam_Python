import math

def GiaiBacHai(aa, bb, cc):
	delta = bb * bb - 4 * aa * cc
	if (delta != 0):
		if (delta > 0):
			x1 = (- bb - math.sqrt(delta)) / (2 * aa)
			x2 = (- bb + math.sqrt(delta)) / (2 * aa)
			print(x1, x2)
		else:
			print("VN")
	else:
		x0 = - bb / (2 * aa)
		print(x0)

def main():
	a = float(input("Nhap a: "))
	b = float(input("Nhap b: "))
	c = float(input("Nhap c: "))

	GiaiBacHai(a, b, c)

if __name__ == "__main__":
    main()
