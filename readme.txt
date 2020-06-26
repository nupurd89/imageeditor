
This project creates an image editor. There are three options: object filtering, black and white,
and horizontal flip. Object filtering takes in three ppm images as its parameter. Each one has
a different object in it. It returns a picture with the common background in all pictures,
taking away the disparities. The black and white option takes in one ppm image as a parameter
and turns it into greyscale. The last option, horizontal flip, flips the picture sideways. 



 I made all of these images compatible for turing your own images into ppm format with GIMP.
I also included three files (object_filter.ppm, shades_of_gray.ppm, horizontal_flip.ppm) which
demonstrates all the effects on the tetons1.ppm image.



Function Descriptions:

object_filter: This function takes in 3 ppm files and takes the mode of each
    pixel to remove uncommon objects in the picture
 shades_of_gray: This function takes in a ppm image and output file name and
    recreates the input image in black and white into the output file
 horizontal_flip: This function takes in a ppm file and produces a mirror image
    of the picture into the output file.\
 read_metadata: reads and stores the first 3 lines of each image which has the
   dimensions, pixel value, etc.
 skip_lines: stores the rest of the values (not metadata) into an array called pixels
 write_metadata: writes the metadata into the new blank output file
 get_average: gets the average of the first 3 parameters
 test_mode: gets the mode of a list that it takes in
    
