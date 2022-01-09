# Daisy Intelligence Hackathon 2022 **2nd place !!!**
Group Members: Robert Ren, Mark Zhao, Lindy Zhai  
**Checkout the `daisy_sol_final.ipynb` for our work in only 24 hours!**

![alt text](https://github.com/RobertRen1122/daisy2022/blob/909424d4ef86f9603cdddcd1aeceb3a77bb73e68/endpage.png)

## Goal
We would like to have a "note-beautifier". Essentially, this GAN-based architecture will take in user's hand writing as input (likely in the form of an image, such as jpeg, png, etc). Then each alphabet will be "beautified" individually. This step involves segmenting alphabets out from the images and the recognize it. The segmented letter is inputted to the GAN architecture. After retreiving the generated 'beautified' fonts from GAN, this output in the form of an image will be resized to fit in the original document.

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
3. ~(OPTIONAL) Replace the 'beautified' text on to the original image.~
4. ~(DONE) Process EMNIST Dataset (Mark & Lindy)(MVP)~
    * ~By class, 0-9, a-z, A-Z.~
    * ~Write a function to convert data from csv to images (for training)~

### Training
1. ~(DONE)Go through cGAN. (Robert)~
2. ~Apply cGAN to preprocessed data.(Robert)~

### Product
1. ~(DONE)Take in image of any size and produce an image (of the same size) with 'beautified' text. (MVP) (Robert)~
2. ~(DONE)Compare generated text with ideal font using similarity measurements. (Mark)~
3. (OPTIONAL)Replace the original text with generated text.

* Note that we have complete codes for every part of the product, but due to tight time constraints, we have not yet linked all py files together. However, feel still feel free to check out the functionality of the different parts of our design

### Note
* MVP - Minimum Viable Product
* Assumption: The person writes in straight line
