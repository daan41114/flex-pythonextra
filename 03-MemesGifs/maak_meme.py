from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("achtergrond.jpg")
print("De afbeelding is " + "259" + " pixels breed en " + "259" + " pixels hoog")

lettertype = ImageFont.truetype("impact.ttf", 21)
tekengebied = ImageDraw.Draw(achtergrond)

tekst = "Coding in Python easy!"
tekengebied.multiline_text((10,220), tekst, font=lettertype, fill=(225,255,255))

achtergrond.show()
achtergrond.save("meme_met_tekst.jpg")
