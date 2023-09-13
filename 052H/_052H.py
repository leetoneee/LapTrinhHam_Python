def DemUocSo(nn):
	dem = 0
	i = 1
	while (i <= nn):
		if (nn % i == 0):
			dem += 1		
		i = i + 1
	return dem

def main():
	n = int(input("Nhap n: "))

	print("So luong uoc so:", DemUocSo(n))

if __name__ == "__main__":
    main()

