#Dictionary is a KEY : VALUE pair 

def main():
    lang={"C":4,"C++":3,"Java":2,"Python":1}   
    print(lang)

    print(type(lang))
    print(lang["Java"])
    print(" ")

    for val in lang:
        print(val)

    # for i in range(len(lang)):
    #     print(lang[i])         Such kind of indexing is not allowed !!
    print(" ")
    for val in lang:
        print(val,lang[val])


if __name__=="__main__":
    main()    