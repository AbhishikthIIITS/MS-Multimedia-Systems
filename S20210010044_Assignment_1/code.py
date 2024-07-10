import numpy as np

from PIL import Image, ImageDraw, ImageFont
GreetingImage=Image.open("Background_img.jpg")

img_drawer = ImageDraw.Draw(GreetingImage)

greeting_font_1 = ImageFont.truetype(r'fabfeltscript.bold.ttf', 48)

greeting_font_2=ImageFont.truetype(r'DancingScript-Bold.ttf',18)


greeting_font_4=ImageFont.truetype(r'Diphylleia-Regular.ttf',17)

greeting_font_3=ImageFont.truetype(r'Diphylleia-Regular.ttf',18)

img_drawer.text((208, 90), "Happy", font = greeting_font_1, fill =(20,86,87,255))
img_drawer.text((210, 145), "Anniversary", font = greeting_font_1, fill =(20,86,87,255))

img_drawer.text((255, 205),"Congratulations on another", font = greeting_font_2, fill =(105,56,41,255))
img_drawer.text((270, 222),"year of love and laughter.", font = greeting_font_2, fill =(105,56,41,255))

img_drawer.text((268, 243),"Wishing you endless joy and ", font = greeting_font_2, fill =(105,56,41,255))
img_drawer.text((306, 261),"countless adventures ", font = greeting_font_2, fill =(105,56,41,255))
img_drawer.text((314, 278)," in the years ahead.", font = greeting_font_2, fill =(105,56,41,255))

img_drawer.text((314, 315),"\u00A9 ", font = greeting_font_3, fill =(7,46,49,255))
img_drawer.text((330, 315),"Abhishikth Boda", font = greeting_font_4, fill =(7,46,49,255))


GreetingImage.show()

GreetingImage.save('S20210010044_greeting-card.jpg')