# Daisy Intelligence Hackathon 2022
Group Members: Robert Ren, Mark Zhao, Lindy Zhai
![alt text](https://github.com/RobertRen1122/daisy2022/blob/834d6bc601402a9f614fe2ed7d3a85a03959da68/README.md)

## Goal
We would like to have a "note-beautifier". Essentially, this GAN based algorithm will take user's handing writing as input (likely in the form of an image, such as jpeg, png, etc). Then each alphabet will be "beautified" individually. This step involves segmenting alphabet out from image while recognizing it.  

## Tasks
### Pre-req
1. ~(DONE) GAN style-transfer example (Robert)~

### Preprocessing
1. ~(DONE) Segment each alphabet from a word, know which alphabet it is. (MVP) (Mark & Lindy)~
    * ~Get the coordinate of each alphabet with respect to each text.~
    * ~Standardize the size of each bouding box to a square/rectangle.~
2. ~(DONE) Transfer the image to black and white scale.~
3. ~(OPTIONAL) Replace the 'beautified' text on to the original image. (MVP)~
4. Process EMNIST Dataset **(Mark & Lindy)**
    * By class, 0-9, a-z, A-Z.
    * Write a function to convert data from csv to images (for training)

### Training
1. Go through cGAN.
2. Apply cGAN to preprocessed data.

### Product
1. Take in image of any size and produce an image (of the same size) with 'beautified' text. (MVP)
2. Compare generated text with ideal font.
3. Replace the original text with generated text.

### Note
* MVP - Minimum Viable Product
* Assumption: The person writes in straight line
