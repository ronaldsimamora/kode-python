def infoKaryawan(nama, usia, gaji):
    print("Nama: %s" % nama)
    print("Usia: %s" % usia)
    print("Gaji: %s" %gaji, end="\n\n")
    return

def main():
    # memanggil fungsi
    infoKaryawan(nama="Bimo",usia=35,gaji=6000000)
    infoKaryawan(usia=36,nama="Sakti",gaji=5000000)
    infoKaryawan(gaji=7000000,usia=37,nama="Dewa")

if __name__ == "__main__":
    main()
