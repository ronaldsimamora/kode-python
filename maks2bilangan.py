def main():
    # menampilkan judul program
    print("Nilai maksimum dari Dua Bilangan")
    
    # meminta user memasukkan dua bilangan
    a = int(input("\nMasukkan bilangan ke-1 \t: "))
    b = int(input("Masukkan bilangan ke-2 \t: "))
    
    # menentukan nilai maksimum
    if a > b:
        maks = a
    else:
        maks = b
        
    # menampilan nilai maksimum
    print("\nNilai maksimum adalah %d : " %maks)
    
if __name__ == "__main__":
    main()