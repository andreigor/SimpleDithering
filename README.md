
# Simple Dithering

Apply a simple Dithering technique to a multi-band colored image.
The Dithering technique reduces the collor pallete of an image, while trying to maintain a good visual
perception by the user.

Several Dithering masks have been proposed by the literature. In this project, we implemented the following:
- a) Floyd and Steinberg
- b) Stevenson and Acre
- c) Burkes
- d) Sierra
- e) Stucki
- f) Jarvis, Judice and Ninke

## How to use

1. run ```cd``` in shell into directory ```src```
2. run ```python input_image.png dithering_mask output_image.png```

##

The output image will be saved in the ```outputs``` directory. A few sample images are availabel in the ```images``` directory

