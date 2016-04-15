from PIL import ImageFilter,Image
im = Image.open('../file/account/CheckCode.gif')
imgry = im.covert('L')
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
