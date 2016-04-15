from PIL import Image,ImageFilter

kitten = Image.open('../file/img/10/1.jpg')
blurry = kitten.filter(ImageFilter.GaussianBlur)
blurry.save("../file/account/asdas.jpg")
blurry.show()