class Image_editing:

    def __init__(self, fin):
        self.filename = fin
    
        fin = open(fin) # opens the file fo reading
        self.image = fin.read() #reads the image file 

        #calls the next function and defines variable as what the 
        # function returns, so a list of all the RGB values as integers
        self.pixel_int = self.obtaining_key_values(self.image)


    def obtaining_key_values(self, image_text):
        image_text_list = []
        
        for num in image_text.split(): #splits the file content by spaces into a list of strings
            image_text_list.append(num)

        #gets the special image numbers using their specific indexes
        self.magic_number = image_text_list[0]
        self.width = int(image_text_list[1])
        self.length = int(image_text_list[2])
        self.max_colour_val = int(image_text_list[3])
    
        colour_value_list = image_text_list[4:] #cuts out the special numbers out of the list
        
        pixel_int = []

        for index in colour_value_list:  #converts the string pixels into integers
            pixel_int.append(int(index))

        return pixel_int

    def hold_pix(self):  #takes the integer list and turns it into a 3D list(grid)
        self.grid = []

        while len(self.grid) < self.length:
            row_list = []

            while len(row_list) < self.width:
                row_list.append(self.pixel_int[0:3]) # take the RGB values as one list and add them into row
                self.pixel_int = self.pixel_int[3:] #remove these used values

            self.grid.append(row_list) #adds the row into the grid

        return self.grid
    
    def negate_red(self):
        for row in self.grid:
            for pixel in row:
                pixel[0] = self.max_colour_val - pixel[0] #subtract red val from max val
        return self.grid

    def flip_horizontal(self):
        new_grid= []
        for row in self.grid:
            fliped_row=[]
            for pixel in row[::-1]:      # reverses each row
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

    def row_to_string(self, rowlist):  # Converts a row of pixels to a string 
        nums = []

        for pixel in rowlist:
            pixel = [str(num) for num in pixel] # Convert each RGB value to string
            nums.append( " ".join(pixel))   # Join RGB values
        
        return " ".join(nums)     # Join all pixels in the row

    def save(self, filename):   # Saves the edited image to a new file
        lines = []
        lines.append(self.magic_number)
        lines.append(str(self.width) + " " + str(self.length))
        lines.append(str(self.max_colour_val))

        for row in self.grid:    # Add each row of pixel data
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