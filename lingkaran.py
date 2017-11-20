import math

def main():
    # menampilkan informasi program
    print("Luas dan Keliling Lingkaran")
    
    # input nilai jari-jari
    r = float(input("Masukkan nilai jari-jari: "))
    
    # menghitung luas lingkaran
    L = math.pi * (r ** 2)
    
    # menghitung keliling lingkaran
    K = 2 * math.pi * r
    
    # menampilkan hasil perhitungan ke layar
    print("Luas \t\t: %.2f" %L)
    print("Keliling \t: %.2f" %K)
    
if __name__ == "__main__":
    main()