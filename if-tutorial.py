def main():
    x = float(input("Masukkan bilangan pertama\t : "))
    y =float(input("Masukkan bilangan kedua\t\t : "))
    op = input("Masukkan operator (+, -, *, /)\t\t : ")

    if op == "+":
        print("%.2f + %.2f = %.2f" % (x, y, x+y))
    elif op == "-":
        print("%.2f - %.2f = %.2f" % (x, y, x-y))
    elif op == "*":
        print("%.2f * %.2f = %.2f" % (x, y, x*y))
    elif op == "/":
        print("%.2f / %.2f = %.2f" % (x, y, x/y))
    else:
        print("ERROR: Gunakan operator +, -, *, atau /")

if __name__ == "__main__":
    main()
