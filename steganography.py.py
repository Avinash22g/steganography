from PIL import Image

def genData(data):
    newd = []
    for char in data:
        newd.append(format(ord(char), '08b'))
    return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):
        pix = [value for value in next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3]]
        for j in range(8):
            if datalist[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1
            elif datalist[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

# Example usage:
original_image = Image.open("C:\Users\ACER\Pictures\R15.jpeg")
message_to_hide = "Hello, this is a hidden message!"
encoded_image = Image.new("RGB", original_image.size)
encoded_image.putdata(list(modPix(original_image.getdata(), message_to_hide)))
encoded_image.save("encoded_image.png")
