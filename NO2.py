name = input("Masukkan nama :")

for i in range (len(name)):
    for j in range (i,7):
        if (i==0 and j==0):
            print(name[0], end=(" "))
        else:
            print("*"*6, end=(' '))
    print( )

                