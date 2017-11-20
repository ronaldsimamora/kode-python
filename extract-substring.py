def main():
    s = "Python"
    
    print("S", s)
    print("s[0]     = ", s[0])      #karakter pertama didalam string S
    print("s[1]     = ", s[1])      #karakter kedua didalam string S
    print("s[-4]    = ", s[-4])     #karakter ke-4 dhitung dari kanan
    print("s[:2]    = ", s[:2])     #menampilkan 2 karakter pertama
    print("s[2:]    = ", s[2:])     #string S dikurangi 2 karakter pertama
    print("s[1:4]   = ", s[1:4])    #substring dari index ke1 sampai ke3 (4-1)
    print("s[2:5]   = ", s[2:5])    #substring dari index ke2 sampai ke4 (5-1)
if __name__ == "__main__":
    main()