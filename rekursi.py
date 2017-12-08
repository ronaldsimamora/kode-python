import sys

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

def main():
    bil = int(input("Masukkan bilangan yang akan di hitung: "))

    if bil < 0:
        print("Error: Bilangan tidak boleh negatif")
        sys.exit(1)

    print("%d! = %d" % (bil, faktorial(bil)))

if __name__ == "__main__":
    main()    
