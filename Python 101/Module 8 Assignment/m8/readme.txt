1. Name: Andrew Taylor, atayl136
2. Module Info: Module 8 Linear Feedback Shift Registers , (Sunday, April 3, 2022 11:59 PM)
3. Approach:
    3.1 LFSR
        1. define areas (methods) within the class
        2. with given instruction on tap and seed indexing (reverse order), chose to index
           from the back instead of re-sorting in bit method
        3. on step() method, used XOR to generate and save new number
        4. print(string) calls __str__ native method. overrided str() to customize our 
           print() function output.
        5. finally, list the process in main() function to operate steps in order.
    3.2 image_encrypter
        1. define areas (methods) within the class
        2. initialize by inheriting LFSR class, so we can reuse methods such as "step" "bit" from LFSR
        3. pixelate method will open the image, save the pixel size which will be used in loop,
           and returns back both image and pixel number objects
        4. then we encrypt each pixel with for loop using LFSR numbers. Each of upcoming RGB numbers are
           XOR-ed with new LFSR number. The problem is that in each pixel, three RGB numbers exist in tuple
           which cannot be altered. Thus we save our LFSR assignment in list, and assign new RGB values
           together in conversion of list to tuple. 
        5. finally, save the altered image. We chose to include full filename with extension as initial input,
           so on saving stage the script will check if filename includes extension.

4. Known Bugs
    4.1 since we are using tap as index bit information to generate new LFSR number, 
    we could get "out of index" string error if "tap" number is greater than the bit length
    of either seed or last lfsr string.

    4.2 there is no enforcement on types of initial inputs "seed" & "tap". If other input
    types gets inserted when creating the object, the script will throw error.

    4.3 we are loading few files as the inputs. there is no checking on whether file exists
    on current working directory so if the script cannot find the specified files will throw
    file not found error.

5. Partner Collaboration
    Andrew
    Dana
    Jiyong 

For our project, Jiyong took the lead with the LFSR script, and Andrew handled the image encrypter script. Rosie assisted with the LFSR and wrote the LFSR test script. Everyone in the group shared each other' files and we all spent significant time looking over each other's work and optimizing where we were able. We all made contributions to the final project and did not encounter any complexities working with each other, since we have been partners in another class previously.