import os, compileall

def main():
    dir = "C:\\simulasi\kodepython"
    compileall.compile_dir(dir)
    print("Semua file dalam %s telah dikompilasi" % dir)
    os.system("pause")
    
if __name__ == "__main__":
    main()