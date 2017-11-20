def main():
    d = {'satu':10, 'dua':20, 'tiga':30}
    
    #elemen dictionary sebelum di ubah
    print("Elemen dictionary sebelum di ubah")
    print(d)
    
    #mengubah nilai elemen d ['satu'] dan d ['tiga']
    d['satu'] = 60
    d['tiga'] = 90
    
    #elemen dictionary setelah diubah
    print("\"Elemen dictionary setelah diubah: ")
    print(d)
    
if __name__ == "__main__":
    main()