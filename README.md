# Python
SLR cameras have the option to save photos in JPG and RAW (.NEF) formats.
This piece of code will loop into your Photos directories and subdirectories, will create new subdirectories with the same name as the current directory padded with NEF in front, and move all .NEF files into the corresponding NEF directories.

e.g folder structure
   2015 
      -----> February2015
      -----> March2015
 will result in
 2015
      -----> NEF.February2015
      -----> NEF.March2015
      
moving the .NEF files in NEF.* dirs.   
