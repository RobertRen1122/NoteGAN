# Daisy Intelligence Hackathon 2022
Group Members: Robert Ren, Mark Zhao, Lindy Zhai

![alt text](https://github.com/RobertRen1122/daisy2022/blob/909424d4ef86f9603cdddcd1aeceb3a77bb73e68/endpage.png)

## Goal
We would like to have a "note-beautifier". Essentially, this GAN based algorithm will take user's hand writing as input (likely in the form of an image, such as jpeg, png, etc). Then each alphabet will be "beautified" individually. This step involves segmenting alphabet out from image while recognizing it, then the segmented letter is being inputted to the GAN algorithms. After retreiving the output from GAN, this output in the form of an image will be resized to fit in the original document.

## Background
As students, all of our team members agree that notetaking is not our strengths. This consensus comes from our not-so-good handwriting, as well as our gradual lost of patience once we found good electronic substitute for pen and paper. However, recognizing that keeping notes is an important part of academic learning, we would like to work on a ML project that could improve our inefficient learning and handwriting habits.

Plus, we thought it would be so much fun to work on a GAN project :)


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
2. Compare generated text with ideal font using similarity measurements.
3. Replace the original text with generated text.

* Note that we have complete codes for every part of the product, but due to tight time constraints, we have not yet linked all py files together. However, feel still feel free to check out the functionality of the different parts of our design

### Note
* MVP - Minimum Viable Product
* Assumption: The person writes in straight line
