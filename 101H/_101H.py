def Tinh():
	s = 0
	i = 1
	e = 1
	epsilon = 10**-6
	while (e >= epsilon):
		e = 1 / i
		s = s + e
		i = i + 1
	return s

def main():
	print("Ket qua:", Tinh())

if __name__ == "__main__":
    main()

