#opens and reads the file
fin = open("image. ppm")
image = fin.read()
#print(self.image)

class image_editing:

    def __init__(self):
        pass
    
    def obtaining_key_values(self, image_text):
        image_text_list = []
        for num in image_text.split():
            image_text_list.append(num)
        self.magic_number = image_text_list[0]
        self.width = int(image_text_list[1])
        self.length = int(image_text_list[2])
        self.max_colour_val = image_text_list[3]
        self.each_pixel_image_text = image_text_list[4:-1]
        return self.each_pixel_image_text

    def hold_pix(self):
        grid = []
        while len(grid) < self.length:
            row_list = []
            while len(row_list) < self.width:
                row_list.append(self.each_pixel_image_text[0:3])
                self.each_pixel_image_text = self.each_pixel_image_text[3:]
            grid.append(row_list)
        return grid

bot = image_editing()
bot.obtaining_key_values(image)
print(bot.hold_pix())