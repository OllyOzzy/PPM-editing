#opens and reads the file

class Image_editing:

    def __init__(self, fin):
        self.filename = fin
    
        fin = open(fin)
        self.image = fin.read()

        self.pixel_int = self.obtaining_key_values(self.image)


    def obtaining_key_values(self, image_text):
        image_text_list = []
        for num in image_text.split():
            image_text_list.append(num)
        
        self.magic_number = image_text_list[0]
        self.width = int(image_text_list[1])
        self.length = int(image_text_list[2])
        self.max_colour_val = int(image_text_list[3])
    
        colour_value_list = image_text_list[4:]
        
        pixel_int = []

        for index in colour_value_list:
            pixel_int.append(int(index))

        return pixel_int

    def hold_pix(self):
        self.grid = []

        while len(self.grid) < self.length:
            row_list = []

            while len(row_list) < self.width:
                row_list.append(self.pixel_int[0:3])
                self.pixel_int = self.pixel_int[3:]

            self.grid.append(row_list)

        return self.grid
    
    def negate_red(self):
        for row in self.grid:
            for pixel in row:
                pixel[0] = self.max_colour_val - pixel[0]
        return self.grid

    def flip_horizontal(self):
        new_grid= []
        for row in self.grid:
            fliped_row=[]
            for pixel in row[::-1]:
                fliped_row.append(pixel)
            new_grid.append(fliped_row)
        self.grid = new_grid
        return self.grid


    def grey_scale(self):
        for row in self.grid:
            for pixel in row:
                col_avg = 0
                col_avg = (pixel[0] + pixel[1] + pixel[2]) // 3
                pixel [0] = col_avg
                pixel [1] = col_avg
                pixel [2] = col_avg
        return self.grid

    
    def flatten_red(self):
        for row in self.grid:
            for pixel in row:
                pixel[0]= 0
        return self.grid

    def row_to_string(self, rowlist):
        nums = []

        for pixel in rowlist:
            pixel = [str(num) for num in pixel]
            nums.append( " ".join(pixel))
        
        return " ".join(nums)

    def save(self, filename):
        lines = []
        lines.append(self.magic_number)
        lines.append(str(self.width) + " " + str(self.length))
        lines.append(str(self.max_colour_val))

        '''
        for each row in grid

            use row_to_string() to get string of row

            add to lines
        '''
        for row in self.grid:
            lines.append(self.row_to_string(row))

        fout = open(filename, "w")
        fout.write( "\n".join(lines))
        fout.close()


bot = Image_editing("image.ppm")

bot.hold_pix()
bot.negate_red()
bot.flip_horizontal()
bot.grey_scale()
bot.flatten_red()
bot.save("image_out.ppm")