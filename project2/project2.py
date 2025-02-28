
import numpy as np
import sympy as sp

def solveMatrix():
    None


def findSolutionFromInput():
    #recieve input and set to x1
    print("Please Enter Value for x1 to solve for other variables.")
    userInput = input()
    try:
        x1 = round(float(userInput), 3)
        
        #use x1 with other algebra from equations to solve for other variables
        x2 = x1 - 100
        x3 = x2 + 50
        x4 = x3 -120
        x5 = x4 + 150
        x6 = x5 - 80

        #print out variables
        if(x1 == round(x6 + 100, 3)):
            print("\nSolution Found!")
            print("x1 = ", x1)
            print("x2 = ", x2)
            print("x3 = ", x3)
            print("x4 = ", x4)
            print("x5 = ", x5)
            print("x6 = ", x6)
        else:
            print("\nNo Solution Found.")
    except ValueError:
        print("Invalid Input. Re-run program to try again.")

    



#Output Part A Equations
print("A -> x1 - 100 = x2\nB -> x2 + 50 = x3\nC -> x3 - 120 = x4\nD -> x4 + 150 = x5\nE -> x5 - 80 = x6\nF -> x6 + 100 = x1\n\n")

#make matrix from our original equations
augmentedMatrix = np.array([[1, -1, 0, 0, 0, 0, 100], [0, 1, -1, 0, 0, 0, -50], [0, 0, 1, -1, 0, 0, 120], [0, 0, 0, 1, -1, 0, -150], [0, 0, 0, 0, 1, -1, 80], [-1, 0, 0, 0, 0, 1, -100]])
spAugmentedMatrix = sp.Matrix(augmentedMatrix)  #Translate to sympy matrix

#find and print ref and rref of augmented matrix using sympy
REF = spAugmentedMatrix.echelon_form()
RREF = spAugmentedMatrix.rref()[0]

#translate sympy matrix back into sumpy matrixes
npREF = np.matrix(REF)
npRREF = np.matrix(RREF)

#print results
print("Original Matrix: ")
print(augmentedMatrix)
print("\nEchelon-Form:")
print(npREF)
print("\nReduced Echelon-Form: ")
print(npRREF)
print("\n\n")

#get input from user to solve for x2, x3, ... and x6, using x1 = input
findSolutionFromInput()

