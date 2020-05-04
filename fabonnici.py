def fib(n):
      a= 0                     
      b= 1

    print(a)           
    print(b)

    for i in range(2,n):                   # range is from 2 bcz 0 and 1 is already print
        c= a+b                                   #this swapping is used for the forward nos
        a=b
        b=c
        print(c)
fib(10)          