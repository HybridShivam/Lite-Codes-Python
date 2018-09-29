m=int((int(input("Enter the no of rows (ODD) in the diamond pattern:\n"))+1)/2)+1
for i in range(1,m):
    print(" "*(m-i)+"*"*(2*i-1))
for i in range(m-2,0,-1):
    print(" "*(m-i)+"*"*(2*i-1))