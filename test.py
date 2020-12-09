import textwrap
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import random

number = 2
fileName = "post " + str(number)

colorInt = random.randint(1, 4)

if colorInt == 1:
    color = "#F18D7E"
if colorInt == 2:
    color = "#bc83d4"
if colorInt == 3:
    color = "#80d7ff"
if colorInt == 4:
    color = "#57cf75"

#F18D7E #bc83d4 #80d7ff #57cf75
img = Image.new('RGB', (500, 500), color = color)

font = ImageFont.truetype('Raleway-Regular.ttf', 25)
d = ImageDraw.Draw(img)
d.text((20, 20), "@voiceofws - #" + str(number), font=font, fill="#FFF")

margin = 20
offset = 60
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras finibus mi purus, suscipit maximus lorem ullamcorper ac. Pellentesque dignissim vestibulum lacus, vel hendrerit enim. Duis vestibulum magna eu ultricies commodo. Suspendisse tempus sollicitudin tellus sed malesuada. Donec ac commodo dolor. Nulla id velit pulvinar nibh laoreet euismod. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean justo leo, viverra quis congue tincidunt, dictum sed lacus. Suspendisse hendrerit lorem ipsum, porttitor tincidunt libero vehicula nec. Nullam tempus tempor urna, vitae tristique ligula tempus et. Nullam dolor velit, consequat a sem sit amet, porta sodales libero. Proin maximus sollicitudin enim quis feugiat."

for line in textwrap.wrap(text, width=35):
    d.text((margin, offset), line, font=font, fill="#FFF")
    offset += 30

img.save(fileName+".jpg")

#bot = Bot()
#bot.login(username = "voiceofws", password = "Kim042800*")
#bot.upload_photo(fileName+".jpg", caption = fileName)
