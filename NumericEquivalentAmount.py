#input = 12,45,8125.78
def Return20percent():
    b=input("Enter a n to find its 20 percent")
    c=float(b.replace(",",""))*0.2
    # c=b.replace(",","")
    # # print(b.isdigit())
    # # b=int(b)
    # d=0.2
    # e=c*d
    print("20% of ",b,"is",c)

Return20percent()