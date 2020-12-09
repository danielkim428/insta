from django.shortcuts import render
import textwrap
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import random
import os
from .models import *
# Create your views here

def index(request):
    if request.method == 'POST':
        try:
            captions = "If you think this post is inappropriate, please comment '!report' (5 reports will automatically take down this post)"
            content = request.POST['content']
            if not content:
                return render(request, "voice/index.html", {"message": "Please write something"})
            current = Current.objects.all()[0]
            current.num = current.num + 1
            number = str(current.num)
            current.save()

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
            text = content

            for line in textwrap.wrap(text, width=35):
                d.text((margin, offset), line, font=font, fill="#FFF")
                offset += 30

            img.save(fileName+".jpg", format='JPEG', subsampling=0, quality=100)

            new_post = Post(name=fileName, content=content)
            new_post.save()

            bot = Bot()
            bot.login(username = "voiceofws", password = "Kim042800*", is_threaded=True)
            bot.upload_photo(fileName+".jpg", caption = captions)
            os.remove(fileName+".jpg.REMOVE_ME")
            
            return render(request, "voice/index.html")
        except:
            return render(request, "voice/index.html", {"message": "Something went wrong. Please try again."})
    else:
        return render(request, "voice/index.html")
