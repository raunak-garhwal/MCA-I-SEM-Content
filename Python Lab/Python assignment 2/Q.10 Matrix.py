def insertInMatrix(matrix,row,col):
    for i in range(row): 	
        a = []
        for j in range(col): 
            a.append(int(input()))
        matrix.append(a)

def printMatrix(matrix,row,col):
    for r in range(0,row):
        for c in range(0,col):
            print(matrix[r][c],end=" ")
        print()

def addMatrix(A,B,row,col): 
    result = []
    for i in range(0,row):
        b=[]
        for j in range(0,col):
            b.append(A[i][j]+B[i][j])
        result.append(b)
    return result

def subMatrix(A,B,row,col):
    result = []
    for i in range(0,row):
        b=[]
        for j in range(0,col):
            b.append(A[i][j]-B[i][j])
        result.append(b)    
    return result

def mulMatrix(matrix1,matrix2):

    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*matrix2)] for row1 in matrix1]

    # rows1, cols1 = len(matrix1), len(matrix1[0])
    # rows2, cols2 = len(matrix2), len(matrix2[0])

    # result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # for i in range(rows1):
    #     for j in range(cols2):
    #         for k in range(cols1):
    #             result[i][j] += matrix1[i][k] * matrix2[k][j]

    # return result

print("\nWelcome to the Matrix Menu Driven Program :-\n")
print("What Operation would you like to perform :-\n")

while(True):
    print("\nPress 1 for Matrix Addition.")
    print("Press 2 for Matrix Subtraction.")
    print("Press 3 for Matrix Multiplication.")
    print("Press 4 to exit.")
    choice=int(input("\nEnter Your Choice(1,2,3,4) :- "))

    if choice == 1:

        matrixA = []
        matrixB = []
        print("\nProgram for Matrix Addition :- \nNOTE :- For Matrix Addition,the order of the two Matrices must be equal.\n")
        row = int(input("Enter the number of rows in Matrix :- "))
        col = int(input("Enter the number of columns in Matrix :- "))

        print("\nEnter the entries of first Matrix A row wise :- ")
        insertInMatrix(matrixA,row,col)

        print("\nEnter the entries of second Matrix B row wise :- ")
        insertInMatrix(matrixB,row,col)

        print("\nResultant Matrix after Addition :- ")
        printMatrix(addMatrix(matrixA,matrixB,row,col),row,col)

    elif choice == 2:

        matrixA = []
        matrixB = []
        print("\nProgram for Matrix Subtraction :-\nNOTE :- For Matrix Subtraction, the order of the two Matrices must be equal.\n")
        row = int(input("Enter the number of rows in Matrix :- "))
        col = int(input("Enter the number of columns in Matrix :- "))

        print("\nEnter the entries of first Matrix A row wise :- ")
        insertInMatrix(matrixA,row,col)

        print("\nEnter the entries of second Matrix B row wise :- ")
        insertInMatrix(matrixB,row,col)

        print("\nResultant Matrix after Subtraction :- ")
        printMatrix(subMatrix(matrixA,matrixB,row,col),row,col)
        
    elif choice == 3:
        
        matrixA = []
        matrixB = []
        print("\nProgram for Matrix Multiplication :- \nNOTE :- For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix.\n")

        print("Enter data for first Matrix :- ")
        r1 = int(input("Enter the number of rows in first Matrix :- "))
        c1 = int(input("Enter the number of columns in first Matrix :- "))
        print("\nEnter the entries of first Matrix A row wise :- ")
        insertInMatrix(matrixA,r1,c1)

        print("\nEnter data for second Matrix :- ")
        r2 = int(input("Enter the number of rows in second Matrix :- "))
        c2 = int(input("Enter the number of columns in second Matrix :- "))
        if c1 != r2:
            print("\nLogical Error :- The number of columns in the first matrix does not equal to the number of rows in the second matrix.\n")
            break
        print("\nEnter the entries of second Matrix B row wise :- ")
        insertInMatrix(matrixB,r2,c2)
    
        print("\nResultant Matrix after Multiplication :- ")
        printMatrix(mulMatrix(matrixA,matrixB),r1,c2)
    
    elif choice == 4:
        
        print("\nThanks for using this program.\nPlease Come back soon......\n")
        break

    else:
        print("\nERROR :- Invalid User Input.Please choose a Valid Option.")

