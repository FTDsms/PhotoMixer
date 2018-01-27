from PIL import Image

img1 = Image.open("merged.png")
img2 = Image.open("mask.png")

img3 = Image.alpha_composite(img1, img2)
img3.save("test.png")
