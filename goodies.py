input_fl = open("sample_input.txt","r")
output_fl = open("sample_output.txt","w+")
goodie = {}
output_list=[]
for f in input_fl:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodie[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
print(goodie)
price = list(goodie.values()) #list of prices from the file dictionary

price=[int(i)for i in price] 
#list is sorted in decending order for the easy calculation
price.sort(reverse=True)
print(price)

no_employ=int(input("enter the no of employees: "))  #for entering the number of employees
length=(len(price)-no_employ)

print(length)

#for finding the difference between the highest and lowest price
for i in range(length):
    maxPrice=price[i]
    minPrice=price[no_employ]
    if i == 0:
        diff=maxPrice-minPrice
        founded_index=i
    elif (maxPrice-minPrice)<diff:
        diff=maxPrice-minPrice
        founded_index=i   
founded_price=price[founded_index:no_employ+founded_index]
diff=max(founded_price)-min(founded_price)
print("difference is:",diff)

#for printing the list of output
count=0
for key,value in goodie.items():
    price[count]
    print(value)
    if int(value) in founded_price and count<no_employ:
        str1=key+": "+value
        output_list.append(str1)
        count=count+1
        print(str1)


#for writing the final distribution to output file
output_fl.write("The goodies selected for distribution are:")       
output_fl.write("\n")
for i in output_list:
    output_fl.write(i)
    output_fl.write("\n")
output_fl.write("And the difference between the choosen goodies with maximum and minimum price is "+str(diff))    

#closing the files we have opened
input_fl.close()
output_fl.close()