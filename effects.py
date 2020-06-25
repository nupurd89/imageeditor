##################################
# Nupur Dave
# ncd2123
# Effects.py
# object_filter: filters out the odd object in 3 pictures
# shades_of_gray: turns a picture into black and white
# horizontal_flip: creates a mirror image of an image
# read_metadata: reads the first 3 lines of a ppm file
# skip_lines: skips first 3 lines and returns a list of pixels
# write_metadata: writes the first 3 lines onto the new output file
# get_average: gets the average of 3 numbers
# test_mode a mode function
##################################

from statistics import mode
from collections import Counter
import numpy as np
        
def object_filter(inputFile1, inputFile2, inputFile3, outputFile ):
    ''' This function takes in 3 ppm files and takes the mode of each
    pixel to remove uncommon objects in the picture'''
    
    #opens each input/output file
    file1 = open(inputFile1, "r")
    file2 = open(inputFile2, "r")
    file3 = open(inputFile3, "r")
    out= open(outputFile, "w")
    
    # calls read_metadata to read the dimensions, pixel color, etc of
    # the file and skip_lines to get an array of each pixel for each image
    
    metadata = read_metadata(file1)
    read_metadata(file2)
    read_metadata(file3)
    
    pixel_array1 = skip_lines(file1)
    pixel_array2 = skip_lines(file2)
    pixel_array3 = skip_lines(file3)
    
    # creates an array of none of the same length of pixel array
    pixel_array_out = [None] * len(pixel_array1)

    # writes metadata onto the new file
    write_metadata(out, metadata)
    
    # the for loop gets the mode of each pixel from the three files
    # and puts the result into a new array
    for i in range(0, len(pixel_array1)):
        tempList = [pixel_array1[i], pixel_array2[i], pixel_array3[i]]
        mode_num = test_mode(tempList)
        pixel_array_out[i] = mode_num

    
    # writes pixel_array_out onto the output file with arbritary 
    # number of rows (in this case I chose 21 rows)
    k = 0
    j = 0
    n = 0
    while(n < len(pixel_array_out)):
        while( j < 21):
            n =  j + (k * 21) 
            if(n < len(pixel_array_out)):
                out.write(str(pixel_array_out[n] ) + " ")
                j = j+1
            else:
                break
        out.write("\n")
        j = 0
        k = k+1
    
    #closes al the files
    file1.close()
    file2.close()
    file3.close()
    out.close()
    
    # alternate method is commented out - this one does not account
    # for files that use GIMP to convert into ppn because each line
    # only has one pixel
    '''
    line1 = file1.readline()
    line2 = file2.readline()
    line3 = file3.readline()
    
    while(len(line1) > 0):
        line1_list = line1.split()
        line2_list = line2.split()
        line3_list = line3.split()
        
        print(len(line1_list))
        print(len(line2_list))
        print(len(line3_list))
        for i in range(0,len(line1_list)):
            tempList = [line1_list[i], line2_list[i], line3_list[i]]
            out.write(mode(tempList))
            out.write(" ")
        out.write("\n")
        line1 = file1.readline()
        line2 = file2.readline()
        line3 = file3.readline()
    '''
    
    
    
def shades_of_gray(inputFile, outputFile):
    '''This function takes in a ppm image and output file name and
    recreates the input image in black and white into the output file'''
    #opens each file
    file = open(inputFile, "r")
    out = open(outputFile, "w")
    
    #reads the metadata and returns an array of pixels
    metadata = read_metadata(file)
    pixel_array = skip_lines(file)
    
    #writes out the metadata in the new file
    write_metadata(out, metadata)
           
    #a while loop that goes through each pixel and gets the average
    # of each RGB triplet and write it into the pixel_array
    i = 0
    while(i < len(pixel_array)-2):
        avg = int(get_average(int(pixel_array[i]), int(pixel_array[i+1]),
                              int(pixel_array[i+2])))
        pixel_array[i] = str(avg)
        pixel_array[i + 1] = str(avg)
        pixel_array[i + 2] = str(avg)
        i = i + 3

    # writes pixel_array onto the output file with arbritary 
    # number of rows (in this case I chose 21 rows)
    
    k = 0
    j = 0
    n = 0
    while(n < len(pixel_array)):
        while( j < 21):
            n =  j + (k * 21) 
            if(n < len(pixel_array)):
                out.write(str(pixel_array[n] ) + " ")
                j = j+1
            else:
                break
        out.write("\n")
        j = 0
        k = k+1

    
def horizontal_flip(inputFile, outputFile):
    '''This function takes in a ppm file and produces a mirror image
    of the picture into the output file.'''
    
    #opens all the files and reads meta and writes it out into the new file.
    # Also returns an array of pixels from the input file.
    file = open(inputFile, "r")
    out = open(outputFile, "w")
    metadata = read_metadata(file)
    pixel_array = skip_lines(file)
    write_metadata(out, metadata)
   
    #defines x_dim and y_dim from the metadata
    x_dim = int(metadata[1])
    y_dim = int(metadata[2])   
    
    #creates a new array and reshapes it 
    arr = np.array(pixel_array)
    arr = arr.reshape(y_dim, 3 * x_dim)

    # flips each rgb triplet from each line utilizing the x_dim
    # and y_dim variables to create the mirror image
    xdiv2 = int(x_dim/2)
    newxdim = x_dim-1
    for j in range(0, y_dim):
        line_arr = arr[j]
        line_arr_split = line_arr.reshape(x_dim, 3)
        for i in range(0, xdiv2):
            temp = np.copy(line_arr_split[i,:])
            line_arr_split[i,:] = line_arr_split[newxdim-i,:]
            line_arr_split[newxdim-i,:] = temp
    
    #reshapes the array so that it is a 1x(number of pixels) np array
    arr = arr.reshape(x_dim*y_dim*3, 1)
    
    # writes pixel_array onto the output file with arbritary 
    # number of rows (in this case I chose 21 rows)
    k = 0
    j = 0
    n = 0
    while(n < len(pixel_array)):
        while( j < 21):
            n =  j + (k * 21) 
            if(n < len(pixel_array)):
                out.write("".join(map(str, arr[n])) + " ")
                j = j+1
            else:
                break
        out.write("\n")
        j = 0
        k = k+1
    
    # closes the files
    file.close()
    out.close()
    
        
def read_metadata(file): 
    '''this function reads the first 3 lines (metadata) and returns
    listattr which holds each piece of metadata as a different
    element'''
    typepic = file.readline()
    dim = file.readline()
    dim_list = dim.split()
    x_dim = dim_list[0]
    y_dim = dim_list[1]
    pixel = file.readline()
    listattr = [typepic, x_dim, y_dim, pixel]
    return listattr

def skip_lines(file):
    '''reads the file and splits each pixel into its own element
    in a list and returns that list'''
    inputf = file.read()
    data = inputf.split()
    pixels = data[0:]
    return pixels

    
def write_metadata(out, metadata):
    '''writes the metadata into the new, blank file'''
    out.write(metadata[0] + "\n")
    out.write(metadata[1] + " " + metadata[2] + "\n")
    out.write(metadata[3] + "\n")    
    
def get_average(a, b, c):
    '''gets the average of the 3 numbers inputted as paramters'''
    the_sum = int(a + b + c)
    avg = the_sum/3
    return avg
    
    
def test_mode(alist):
    '''gets the mode of a list'''
    data = Counter(alist)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    r = ''.join(map(str, mode_val))
    res = r[:3]
    return res
    

    
        
    