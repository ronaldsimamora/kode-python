def main():
    f = open(r"data.txt", "w+")
    
    print("Nama file\t: ", f.name)
    print("Tertutup?\t: ", f.closed)
    print("Mode akses\t: ", f.mode)
    
if __name__ == "__main__":
    main()