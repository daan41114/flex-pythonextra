from PIL import Image, ImageFont, ImageDraw

image = Image.open("we kill the batman.jpg.png")
print("De afbeelding is " + "259" + " pixels breed en " + "259" + " pixels hoog")

lettertype = ImageFont.truetype("impact.ttf", 100)
tekengebied = ImageDraw.Draw(image)

tekst = "Me in 2020: builds a time machine"
tekengebied.multiline_text((10,300), tekst, font=lettertype, fill=(1,1,1))
tekst2 = "Friend: what are you going"
tekengebied.multiline_text((10,450), tekst2, font=lettertype, fill=(1,1,1))
tekst3 = "to do with it"
tekengebied.multiline_text((10,600), tekst3, font=lettertype, fill=(1,1,1))
tekst4 = "Me:"
tekengebied.multiline_text((10,750), tekst4, font=lettertype, fill=(1,1,1))

image.show()
image.save('we_kill_the_batman_meme.jpg')
