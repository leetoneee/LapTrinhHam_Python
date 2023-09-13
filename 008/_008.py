import math

def main():
	n = int(input("Nhap n: "))
	r = float(input("Nhap r: "))

	p = 2 * n * r * math.sin(math.pi / n)
	print("Chu vi:", p)

if __name__ == "__main__":
    main()
