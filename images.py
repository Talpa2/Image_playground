from PIL import Image, ImageFilter

img = Image.open('./image/3.jpg')
new_img = img.resize((300, 300))
new_img.save('minipicaci.jpg')