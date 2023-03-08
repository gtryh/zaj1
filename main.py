from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt


im = Image.open('baby_yoda.jpg')
print("tryb obrazu", im.mode)


def filtruj(obraz, kernel, scale):
    im1 = obraz.copy()
    w, h = im1.size
    pixele = im1.load()
    pixele2 = obraz.load()


#Zad 3
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 20,  (-1, 0, 1, -2, 0, 2, -1, 0, 1))
print(ImageFilter.EMBOSS.filterargs)

im = Image.open('baby_yoda.jpg')
im_c = im.convert('L')
im2 = im_c.filter(ImageFilter.EMBOSS)
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im3 = im_c.filter(ImageFilter.EMBOSS)

plt.subplot(1, 2, 1)
plt.imshow(im2)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(im3)
plt.axis('off')
plt.show()

#Zad3
im_2 = im.filter(ImageFilter.DETAIL)
im_4 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im_6 = im.filter(ImageFilter.SHARPEN)
im_8 = im.filter(ImageFilter.SMOOTH_MORE)

plt.figure(figsize=(5, 8))
plt.subplot(4, 2, 1)
plt.imshow(im)
plt.axis('off')

plt.subplot(4, 2, 2)
plt.title("DETAIL")
plt.imshow(im_2)
plt.axis('off')

plt.subplot(4, 2, 3)
plt.imshow(im)
plt.axis('off')

plt.subplot(4, 2, 4)
plt.title("EDGE_ENHANCE_MORE")
plt.imshow(im_4)
plt.axis('off')

plt.subplot(4, 2, 5)
plt.imshow(im)
plt.axis('off')

plt.subplot(4, 2, 6)
plt.title("SHARPEN")
plt.imshow(im_6)
plt.axis('off')

plt.subplot(4, 2, 7)
plt.imshow(im)
plt.axis('off')

plt.subplot(4, 2, 8)
plt.title("SMOOTH_MORE")
plt.imshow(im_8)
plt.axis('off')
plt.show()

#Zad4
im_copy1=im.copy()
im_copy2=im.copy()
im_copy3=im.copy()
im_copy4=im.copy()
im_copy5=im.copy()
ImageFilter.GaussianBlur.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im12 = im_copy1.filter(ImageFilter.GaussianBlur)
ImageFilter.UnsharpMask.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im13 = im_copy2.filter(ImageFilter.UnsharpMask)
ImageFilter.MedianFilter.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im16 = im_copy3.filter(ImageFilter.MedianFilter)
ImageFilter.MinFilter.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im17 = im_copy4.filter(ImageFilter.MinFilter)
ImageFilter.MaxFilter.filterargs = ((3, 3), 1, 20,  (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im18 = im_copy5.filter(ImageFilter.MaxFilter)

plt.figure(figsize=(5, 8))

plt.subplot(5, 2, 1)
plt.imshow(im)
plt.axis('off')

plt.subplot(5, 2, 2)
plt.title("GaussianBlur")
plt.imshow(im12)
plt.axis('off')

plt.subplot(5, 2, 3)
plt.imshow(im)
plt.axis('off')

plt.subplot(5, 2, 4)
plt.title("UnsharpMask")
plt.imshow(im13)
plt.axis('off')

plt.subplot(5, 2, 5)
plt.imshow(im)
plt.axis('off')

plt.subplot(5, 2, 6)
plt.title("MedianFilter")
plt.imshow(im16)
plt.axis('off')

plt.subplot(5, 2, 7)
plt.imshow(im)
plt.axis('off')

plt.subplot(5, 2, 8)
plt.title("MinFilter")
plt.imshow(im17)
plt.axis('off')

plt.subplot(5, 2, 9)
plt.imshow(im)
plt.axis('off')

plt.subplot(5, 2, 10)
plt.title("MaxFilter")
plt.imshow(im18)
plt.axis('off')
plt.show()
