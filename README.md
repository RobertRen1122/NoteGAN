# Daisy Intelligence Hackathon 2022
Group Members: Robert Ren, Mark Zhao, Lindy Zhai

## Goal
We would like to have a "note-beautifier"

## Tasks
### Pre-req
1. (DONE) GAN style-transfer example (Robert)

### Preprocessing
1. (DONE) Segment each alphabet from a word, know which alphabet it is. (MVP) (Mark and Lindy)
    * Get the coordinate of each alphabet with respect to each text.
    * Standardize the size of each bouding box to a square/rectangle.
2. (DONE) Transfer the image to black and white scale.
3. (OPTIONAL) Replace the 'beautified' text on to the original image. (MVP)
4. Process EMNIST Dataset
    * By class, 0-9, a-z, A-Z.
    * Write a function to convert data from csv to images (for training)

### Training
1. Apply style transfer. (MVP)
    * Input and output should be of the same size.
    * Style transfer should be **ONE-TO-ONE**.
2. Go through cGAN.
3. Apply cGAN to preprocessed data.

### Product
1. Take in image of any size and produce an image (of the same size) with 'beautified' text. (MVP)
2. Compare generated text with ideal font.
3. Replace the original text with generated text.

### Note
* MVP - Minimum Viable Product
* Assumption: The person writes in straight line
