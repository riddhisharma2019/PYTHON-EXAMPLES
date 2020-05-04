def person(name,**data):                    # double star data is for the contain multiples element by given keywords 
    print(name)
    print(data)

person('Riddhi',age=20,city='Mumbai', mob= 8370432 )    




def person(name,**data):               
    print(name)
    for i,j in data.items():                          #for thr given data we written the functions items
        print(i,j)
person('Riddhi',age=20,city='Mumbai', mob= 8370432 )             