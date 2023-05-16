#==============================================================================
#
# Class : CS 6420
#
# Author : Tyler Martin
#
# Project Name : Project 1 | Porter Duff Operators
# Date: 2/15/2023
#
# Description: This project implements the Porter-Duff operators
#
# Notes: Since I know you prefer to read and work in C++, this file is set
#        up to mimic a standard C/C++ flow style, including a __main__()
#        declaration for ease of viewing. Also, while semi-colons are not 
#        required in python, they can be placed at the end of lines anyway, 
#        usually to denote a specific thing. In my case, they denote globals, 
#        and global access, just to once again make it easier to parse my code
#        and see what it is doing and accessing.
#
#==============================================================================

#"header" file imports
from imports import *
from checkImages import *
from averagePixels import *
from intensitySampling import *
from getMetaData import *
from pixelDeletion import *
from pixelDuplication import *
from saveJson import *
from grayScaleImage import *
from saveImage import *
from operators import *

#================================================================
#
# NOTES: THE OUTPATH WILL HAVE THE LAST / REMOVED IF IT EXISTS
#        THE imageType WILL HAVE A . APPLIED TO THE FRONT AFTER
#        CHECKING VALIDITY
#
#================================================================


#================================================================
#
# Function: __main__
#
# Description: This function is the python equivalent to a main
#              function in C/C++ (added just for ease of your
#              reading, it has no practical purpose)
#
#================================================================

def __main__(argv):

    #variables that contain the command line switch
    #information
    inPath = "nothing"
    depth = 1
    mode = 1
    intensity = 1
    primary = "nothing"
    secondary = "nothing"
    maskone = "nothing"
    masktwo = "nothing"
    direction = 0

    # get arguments and parse
    try:
      opts, args = getopt.getopt(argv,"h:t:s:z:x:m:b:")

    except getopt.GetoptError:
        print("porter-duff.py -t imagefile -s imagefile -tm mask -sm mask -m mode")
        print("===========================================================================================================")
        print("-t : Target Image (I1)")
        print("-s : Secondary Image (I2)")
        print("-z : Target Mask")
        print("-x : Secondary Mask")  
        print("-m : mode (1 = clear | 2 = copy | 3 = over | 4 = in | 5 = out | 6 = atop | 7 = xor | 8 = display images | 9 = all)")
        print("-b : apply operator in both directions (0/1)")
        sys.exit(2)

    for opt, arg in opts:

        if opt == ("-h"):
            print("porter-duff.py -t imagefile -s imagefile -tm mask -sm mask -m mode -b 0/1")
            print("===========================================================================================================")
            print("-t : Target Image (I1)")
            print("-s : Secondary Image (I2)")
            print("-z : Target Mask")
            print("-x : Secondary Mask")  
            print("-m : mode (1 = clear | 2 = copy | 3 = over | 4 = in | 5 = out | 6 = atop | 7 = xor | 8 = display images | 9 = all)")
            print("-b : apply operator in both directions (0/1)")
            sys.exit(2)

        elif opt == ("-m"):
            if (int(arg) < 10 and int(arg) > 0):
                mode = int(arg)
            else:
                print("Invalid Mode Supplied. Only Values 1 through 9 Are Accepted.")

        elif opt == ("-t"):
            primary = arg
        elif opt == ("-s"):
            secondary = arg
        elif opt == ("-z"):
            maskone = arg
        elif opt == ("-x"):
            masktwo = arg
        elif opt == ("-b"):
            direction = arg

    #create images if we are not supplied any
    if (primary == "nothing"):
        primary = np.zeros((480, 640,3), np.uint8)
        cv2.circle(primary, (320, 240), 150, (255, 0, 0), -1)

        if (mode == 9 or mode == 8):
            cv2.imshow("circle (image1)", primary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        primary = cv2.imread(primary)
        
    if (secondary == "nothing"):
        secondary = np.zeros((480, 640,3), np.uint8)
        cv2.rectangle(secondary, (64, 192), (576, 288), (0, 0, 255), -1)
        cv2.rectangle(secondary, (256, 48), (384, 432), (0, 0, 255), -1)

        if (mode == 9 or mode == 8):
            cv2.imshow("cross (image2)", secondary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        secondary = cv2.imread(secondary)

    if (maskone == "nothing"):
        maskone = grayScaleImage(primary)
        #maskone = cv2.threshold(maskone, 70,255,0)
        maskone[maskone > 0] = 255

        if (mode == 9 or mode == 8):
            cv2.imshow("circle_binary (mask1)", maskone)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        maskone = cv2.imread(maskone)
    
    if (masktwo == "nothing"):
        masktwo = grayScaleImage(secondary)
        masktwo[masktwo > 0] = 255

        if (mode == 9 or mode == 8):
            cv2.imshow("cross_binary (mask2)", masktwo)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        masktwo = cv2.imread(masktwo)
    
    if (mode == 9 or mode == 1):
        cv2.imshow("clear image1", opCLEAR(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("clear image2", opCLEAR(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 2):
        cv2.imshow("copy image1", opCOPY(primary, True, maskone));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("copy image2", opCOPY(secondary, True, masktwo));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 3):
        cv2.imshow("image1 over image2", opOVER(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("image2 over image1", opOVER(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 4):
        cv2.imshow("image1 in image2", opIN(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("image2 in image1", opIN(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 5):
        cv2.imshow("image1 out image2", opOUT(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("image2 out image1", opOUT(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 6):
        cv2.imshow("image1 atop image2", opATOP(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("image2 atop image1", opATOP(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if (mode == 9 or mode == 7):
        cv2.imshow("image1 xor image2", opXOR(primary, secondary, maskone, masktwo));
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (direction != 0):
            cv2.imshow("image2 xor image1", opXOR(secondary, primary, masktwo, maskone));
            cv2.waitKey(0)
            cv2.destroyAllWindows()

#start main
argv = ""
__main__(sys.argv[1:])