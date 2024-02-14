# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

from lfsr import LFSR # import your LFSR class for use in ImageEncrypter  
from PIL import Image

class ImageEncrypter(LFSR):
    # initialize an ImageEncrypter object with an LFSR and image file name     
    def __init__(self, seed: str, tap: int, file_name: str):
        super().__init__(seed, tap) # inherit LFSR
        self.file_name = file_name
        ImageEncrypter.step(self) # generate first LFSR new_number
    
    # open the image specified by ‘file_name’ in your constructor     
    # # you will find the Image.open method useful here     
    def open_image(self):
        img = Image.open(self.file_name)
        return img


    # calls open_image()     
    # converts the image to a 2D array of R, G, B triples     
    # you will find the Image.load method useful here     
    def pixelate(self):
        img = ImageEncrypter.open_image(self)
        self.img_size = img.size # save img size for pixel xy
        pixels = img.load() #PixelAccess
        return img, pixels


    # encrypts the 2D pixelated “image” returned from pixelate()      
    # returns the encrypted 2D array     
    # you will find the binary XOR operator useful here         
    def encrypt(self):
        img, pixels = ImageEncrypter.pixelate(self)

        # loop through pixels
        for y in range(self.img_size[1]): 
            for x in range(self.img_size[0]): 
                tmp_pixel = [] # to modify tuple
                for nth in range(len(pixels[x, y])):
                    # assign new XORed int
                    tmp_pixel.append(pixels[x, y][nth] ^ int(self.new_num, 2))
                    ImageEncrypter.step(self) # generate next LFSR new_num
                pixels[x, y] = tuple(tmp_pixel) # assign encrypted value from list

        # save modified img object. change in PixelAccess will auto update image
        self.new_img = img        

    # converts the encrypted 2D pixelated image into an image      
    # # and names it <file_name>_transform.png     
    # # you will find the Image.save method useful here         
    def save_image(self):
        if '.png' in self.file_name:
            file_name = self.file_name.split('.')[0]
        else:
            file_name = self.file_name
        self.new_img.save(f'{file_name}_transform.png')


# your executable code that invokes ImageEncrypter and encrypts/decrypts an 
# # image and saves the result to a file 
def main():
    # initial params
    seed, tap = '10011010', 5
    file_name='football.png'
    obj = ImageEncrypter(seed, tap, file_name=file_name) # create obj
    obj.encrypt()
    obj.save_image()

    # print(obj.__dict__)

if __name__ == '__main__':
    main() 