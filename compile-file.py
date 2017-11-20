import os, py_compile

def main():
    os.chdir("C:\\simulasi\kodepython")
    py_compile.compile("helo.py")
    print("File helo.pyc telah terbuat..")
    os.system("pause")
    
if __name__ == "__main__":
    main()