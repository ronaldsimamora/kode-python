def main():
    str1 = "I Like Python! I Like C++! I Like C!"

    print("str1: ", str1)
    str2 = str1.replace("Like", "love")
    str3 = str1.replace("Like", "love", 2)

    print("str2: ", str2)
    print("str3: ", str3)

if __name__ == "__main__":
    main()
