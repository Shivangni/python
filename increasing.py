def printseriesincreasing(symbol,n):
    count=0
    while(count<n):
        print(symbol * count)
        count+=1
    return None
a=input("enter symbol:")
b=int(input("enter a number:"))
printseriesincreasing(a,b)

