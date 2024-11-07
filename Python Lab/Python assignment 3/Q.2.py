with open('RAUNAK PYTHON ASSIGNMENT 3/Python.txt','r') as firstfile, open('RAUNAK PYTHON ASSIGNMENT 3/Python1.txt','w') as secondfile: 
    for line in firstfile:
        for char in line:
            if not char.isnumeric() : 
                secondfile.write(char)