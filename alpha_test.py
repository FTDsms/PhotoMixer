from PIL import Image

path = "C:\\Users\\Administrator\\Pictures\\Overwatch\\005PP7rUly8fdvpx7k7b0j302s02s0sn.jpg"

image = Image.open(path)
width, height = image.size

print(image.size, width, height)
print(image.format, image.format_description)

im = image.resize((2275, 2275))
im.putalpha(75)

im.save("mask.png")
im.show()
