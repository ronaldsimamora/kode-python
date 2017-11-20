def main():
    # menampilkan judul program
    print("Nilai maksimum dari Tiga Bilangan")
    
    # meminta user memasukkan tiga buah bilangan
    a = int(input("\nMasukkan bilangan ke-1\t: "))
    b = int(input("Masukkan bilangan ke-2\t: "))
    c = int(input("Masukkan bilangan ke-3\t: "))
    
    # menentukan nilai maksimum menggunakan Cara I
    if a > b:
        if a > c:
            maks = a
    else:
        if b > c:
            maks = b
        else:
            maks = c
            
    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d " %maks)
    
if __name__ == "__main__":
    main()