##################################
# Nupur Dave
# ncd2123
# Effects.py
# main - asks the user to choose which effect they would like and
# for the name of the files they want to use.
##################################

from effects import object_filter, shades_of_gray, horizontal_flip

def main():
    print('Welcome to the Portable Pixmax (PPM) Image Editor!')
    print('-----------------------------------------------------------------')
    print('Which effect would you like to use?')
    print()
    print('1) An Object Filter')
    print('2) Shades of Gray')
    print('3) Horizontal Flip')
    print('-----------------------------------------------------------------')
    incorrInput = True
    while(incorrInput):
        chosenEffect = input('Please enter your choice (1,2,3):')
        if chosenEffect == "1" or chosenEffect == "2" or chosenEffect == "3":
            incorrInput =  False
        else:
            print("Your choice was not valid. Please try again!")
        
    outputFile = input('Enter the name of your output file (.ppm): ')
    print(outputFile + ' has been created')
    
    if "1" in chosenEffect:
        inputFile1 = input('Enter the name of your first input file: ')
        inputFile2 = input('Enter the name of your second input file: ')
        inputFile3 = input('Enter the name of your third input file ')
        print("Please wait while your image is created...")
        object_filter(inputFile1, inputFile2, inputFile3, outputFile) 
        print("The file, " + outputFile + ", was succesfully created and the object filter was succesful!")
        
    elif "2" in chosenEffect:
        inputFile = input('Enter your input file name: ')
        print("Please wait while your image is created...")
        shades_of_gray(inputFile, outputFile)
        print("The file, " + outputFile + ", was succesfully created and turned to grayscale!")
        
    elif "3" in chosenEffect:
        inputFile = input('Enter your input file name: ')
        print("Please wait while your image is created...")
        horizontal_flip(inputFile, outputFile)
        print("The file, " + outputFile + ", was succesfully created and horizontally flipped!")
        
    
    
    
if __name__ == "__main__":
    main()