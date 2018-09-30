row,mylist=int(input("Enter The No of Rows: ")),["{0:5}".format(1)]
for i in range(row):#hybrid
    print("   "*(row-i),*mylist[:])
    mylist=["{0:5}".format(int(mylist[j])+int(mylist[j+1])) for j in range(len(mylist)-1)]
    mylist.append("{0:5}".format(1))
    mylist.insert(0,"{0:5}".format(1))
