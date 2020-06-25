{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Nupur Dave\
ncd2123\
Effects.py and Effects_tester.py\
\
\ul Info:\
\ulnone I made all of these images compatible for turing your own images into ppm format with GIMP.\
I also included three files (object_filter.ppm, shades_of_gray.ppm, horizontal_flip.ppm) which\
demonstrates all the effects on the \'91tetons1.ppm\'92 image. \
\
\ul Effects.py\ulnone \
object_filter: This function takes in 3 ppm files and takes the mode of each\
    pixel to remove uncommon objects in the picture\
 shades_of_gray: This function takes in a ppm image and output file name and\
    recreates the input image in black and white into the output file\
 horizontal_flip: This function takes in a ppm file and produces a mirror image\
    of the picture into the output file.\
 read_metadata: reads and stores the first 3 lines of each image which has the\
   dimensions, pixel value, etc.\
 skip_lines: stores the rest of the values (not metadata) into an array called pixels\
 write_metadata: writes the metadata into the new blank output file\
 get_average: gets the average of the first 3 parameters\
 test_mode: gets the mode of a list that it takes in\
    }