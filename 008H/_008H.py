import math

def ChuVi(nn, rr):
	return 2 * nn * rr * math.sin(math.pi / nn)

def main():
	n = int(input("Nhap n: "))
	r = float(input("Nhap r: "))

	print("Chu vi:", ChuVi(n, r))

if __name__ == "__main__":
    main()
