from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import textwrap
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import random
import os
import after_response
from .models import *
# Create your views here

@after_response.enable
def upload_insta(content, fontInt):
    fontNum = int(fontInt)
    text = content
    captions = "If you think this post is inappropriate, please comment '!report' (5 reports will automatically take down this post)"
    current = Current.objects.all()[0]
    current.num = current.num + 1
    number = str(current.num)
    current.save()

    fileName = "post " + str(number)

    colorInt = random.randint(1, 4)
    fontInt  = random.randint(1, 4)

    if colorInt == 1:
        color = "#F18D7E"
    if colorInt == 2:
        color = "#bc83d4"
    if colorInt == 3:
        color = "#3897F0"
    if colorInt == 4:
        color = "#57cf75"

    #F18D7E #bc83d4 #80d7ff #57cf75 #3897F0
    img = Image.new('RGB', (500, 500), color = color)

    fontLogo = ImageFont.truetype('Quicksand-Regular.ttf', 25, encoding='unic')

    d = ImageDraw.Draw(img)
    d.text((20, 20), "@voiceofws - #" + str(number), font=fontLogo, fill="#FFF", embedded_color=True)

    margin = 20
    offset = 60
    lineAmount = 30

    if fontNum == 1:
        font = ImageFont.truetype('Raleway-Regular.ttf', 25, encoding='unic')
    if fontNum == 2:
        font = ImageFont.truetype('Aveny T WEB.ttf', 32, encoding='unic')
        text = text.upper()
    if fontNum == 3:
        font = ImageFont.truetype('Roboto-BlackItalic.ttf', 29, encoding='unic')
    if fontNum == 4:
        font = ImageFont.truetype('AmaticSC-Regular.ttf', 35, encoding='unic')
    if fontNum == 5:
        font = ImageFont.truetype('SpecialElite-Regular.ttf', 25, encoding='unic')
    if fontNum == 6:
        font = ImageFont.truetype('GreatVibes-Regular.ttf', 35, encoding='unic')
        lineAmount = 32

    for line in textwrap.wrap(text, width=35):
        d.text((margin, offset), line, font=font, fill="#FFF")
        offset += lineAmount

    img.save(fileName+".jpg", format='JPEG', subsampling=0, quality=100)

    new_post = Post(name=fileName, content=content)
    new_post.save()

    bot = Bot()
    bot.login(username = "voiceofws", password = "Kim042800*", is_threaded=True)
    bot.upload_photo(fileName+".jpg", caption = captions)
    os.remove(fileName+".jpg.REMOVE_ME")

def index(request):
    if request.method == 'POST':
        try:
            content = request.POST['content']
            fontInt = request.POST['fontInt']
            if not content:
                return render(request, "voice/index.html", {"message": "Please write something"})
            upload_insta.after_response(content, fontInt)

            return render(request, "voice/index.html")
        except:
            return render(request, "voice/index.html", {"message": "Something went wrong. Please try again."})
    else:
        return render(request, "voice/index.html")
