def main():
    #membuat prompt untuk bilangan integer
    bilbulat = int(input("Masukkan bilangan bulat : "))
    
    #menggunakan variabel untuk melakukan perhitungan
    hasil = bilbulat + 1
    
    #menampilkan variabel
    print("Bilangann yang dimasukkan adalah %d" %bilbulat)
    print("%d + 1 = %d" %(bilbulat, hasil))
    
if __name__ == "__main__":
    main()