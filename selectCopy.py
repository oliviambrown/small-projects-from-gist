#! python3

#selectiveCopy.py - Program that chooses what to copy based on certain parameters such as file extension
#Note: This script is dependent on where it's located in a file system on account of it's use of the path function
#Copyright Olivia Brown

import os, shutil

#Create the function
def selectCopy(oFolder, cFolder, ex):
    
    #Aboslute path check for source and destination
    oFolder = os.path.abspath(oFolder)
    cFolder = os.path.abspath(cFolder)

    print('Destination: ' + cFolder)

    #Check if folder exists, if not create a folder
    if not os.path.exists(cFolder):
        os.makedirs(cFolder)
        print('New folder created.')
    
    #Walks through folder tree
    #The filenames is in a list, why I was getting errors, need a for statment to check each file
    for folderlist, subfolderlist, filelist in os.walk(oFolder):

        for filename in filelist:

            #Aearch for file extension
            if filename.endswith(ex):
                print('Copying %s to %s..' % (filename, cFolder))
                #Copy file to new folder
                #Needed the absolute path for the file as well in order for the copy function to work.
                shutil.copy(os.path.join(folderlist,filename), cFolder)
       
    print('Done.')           


selectCopy('Dental', 'scriptdent', '.pdf')
