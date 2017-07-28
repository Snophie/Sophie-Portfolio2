from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("parrot.jpg")
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



darkBlue= input("What color would you like your red to be replaced with? example: (x, y, zss) ")
red= input("What color would you like your green to be replaced with? ")
lightBlue= input("What color would you like your blue to be replaced with? ")
yellow= input("What would you like your extra color to be? ")

for pxl in image_list:
    sum = pxl[0] + pxl[1] + pxl[2]
    if sum <= 182:
        recolored.append(darkBlue)
    elif sum <= 364:
        recolored.append(red)
    elif sum <= 546:
        recolored.append(lightBlue)
    elif sum >= 546:
        recolored.append(yellow)

#if pix <== 182

#        if (x % 5 == 0) or (x % 3 == 0):
#            z = z + x



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recoloredTEDparrot.jpg", "jpeg") #save the new image as "recolored.jpg"
