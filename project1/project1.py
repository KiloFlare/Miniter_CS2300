#############     MATH FUNCTIONS     ####################
#adds two matrix
def AddMatrix(matrix1, matrix2, numRows, numCols):
    sumMatrix = [[0 for x in range(cols)] for y in range(rows)]
    
    for row in range(numRows):
        for column in range(numCols):
            sumMatrix[row][column] = matrix1[row][column] + matrix2[row][column]
    
    return sumMatrix

#subtracts two matrix
def SubMatrix(matrix1, matrix2, numRows, numCols):
    subMatrix = [[0 for x in range(cols)] for y in range(rows)]
    
    for row in range(numRows):
        for column in range(numCols):
            subMatrix[row][column] = matrix1[row][column] - matrix2[row][column]
    
    return subMatrix

#multiplies matrix by a scalar
def MultiplyMatrix(matrix1, scalar, numRows, numCols):
    mulMatrix = [[0 for x in range(cols)] for y in range(rows)]
    
    for row in range(numRows):
        for column in range(numCols):
            mulMatrix[row][column] = matrix1[row][column] * scalar
    
    return mulMatrix

#prints matrix in more readable way
def DisplayMatrix(matrix1, numRows, numCols):
    for row in range(numRows):
        print("row #", row + 1, ": ", end="")
        for column in range(numCols):
            print(matrix1[row][column], " ", end="")

        print()
        




#################     MAIN     ########################
#intro print statements
print("Welcome to Matrix Calculator!")
print("Please select an option! (Enter 1-4)")
print("1. Addition\n2. Subtraction\n3. Scalar Multiplication\n4. Exit")

#get input from user
x = input()
inputValidated = False  #boolean flag for verification of input
chosenMath = 0  #var for chosen process
matrix1 = [[]]
matrix2 = [[]]

#verification loop
while (not inputValidated):
    inputValidated = True
    #depending on input, choose math matrix, or return to loop after recieving new input
    if x == "1":
        print("You chose Addition")
        chosenMath = 1
    elif x == "2":
        print("You chose Subtraction")
        chosenMath = 2
    elif x == "3":
        print("You chose Scalar Multiplication")
        chosenMath = 3
    elif x == "4":
        print("Fine, Leave me")
        quit
    else:
        print(x)
        print("Please enter a valid input")
        inputValidated = False
        x = input()


#vars for number of columns/rows
rows = -1
cols = -1

while rows <= 0 and cols <= 0:
    print("Enter rows and columns of the matrices (Seperate with one space): ")

    #recieves input and splits into array elements based on spaces
    rowsAndCol = input()
    rowsAndColArray = rowsAndCol.split(" ")

    #converts string numbers to integers
    rows = int(rowsAndColArray[0])
    cols = int(rowsAndColArray[1])

#redefine size of matrix
matrix1 = [[0 for x in range(cols)] for y in range(rows)]


#nested for loop to get input for each row, and column space of each matrix
print("Enter each value for first ", rows, "x", cols, " matrix:")
for row in range(rows):
    for column in range(cols):
        print("Enter value in row ", row, " and column ", column, ": ")
        temp = input()
        matrix1[row][column] = int(temp)

#if the choice isn't for multiplication, get another matrix
if chosenMath != 3:
    matrix2 = [[0 for x in range(cols)] for y in range(rows)]

    print("Enter each value for second ", rows, "x", cols, " matrix:")
    for row in range(rows):
        for column in range(cols):
            print("Enter value in row ", row, " and column ", column, ": ")
            temp = input()
            matrix2[row][column] = int(temp)
    
    print("Original Matrixes: \n")
    print("Matrix One:")
    DisplayMatrix(matrix1, rows, cols)
    print("Matrix Two:")
    DisplayMatrix(matrix2, rows, cols)
    print()

else:
    print("Input scalar you would like to multiply by: ")
    scalarText = input()
    scalar = int(scalarText)

    print("Original Matrix: \n")
    print("Matrix One:")
    DisplayMatrix(matrix1, rows, cols)
    print("Scalar: ")
    print(scalar)
    print()



#based on earlier chosen math, do required calculations


print("Results-------------------------")
match chosenMath:
    case 1:
        DisplayMatrix(AddMatrix(matrix1, matrix2, rows, cols), rows, cols)
    case 2:
        DisplayMatrix(SubMatrix(matrix1, matrix2, rows, cols), rows, cols)
    case 3:
        DisplayMatrix(MultiplyMatrix(matrix1, scalar, rows, cols), rows, cols)

    
        









