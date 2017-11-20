def main():
    # menampilkan judul program
    print("Nilai Maksimum dari Tiga Bilangan")
    
    # meminta user memasukkan Tiga Bilangan
    a = int(input("\nMasukkan nilai bilangan ke-1\t: "))
    b = int(input("Masukkan nilai bilangan ke-2\t: "))
    c = int(input("Masukkan nilai bilangan ke-3\t: "))
    
    # menentukan nilai maksimum menggunakan CARA III
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c
        
    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d" %maks)
    
if __name__ == "__main__":
    main()