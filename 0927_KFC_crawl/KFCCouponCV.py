from PIL import Image
import matplotlib.pyplot as plt
from Convert_Img import convert_Image , change_Image_to_text

#圖片處理
img = Image.open('C:/Users/case-pc/Desktop/KFC/40081.jpg')
width = img.size[0]
height = img.size[1]

#剪裁圖片
img3 = img.crop((35,70,100,105))
img3 = convert_Image(img3)

print(change_Image_to_text(img3))

#畫出圖型img3
plt.figure("coupon")
plt.axis('off')
plt.imshow(img3)
plt.show()