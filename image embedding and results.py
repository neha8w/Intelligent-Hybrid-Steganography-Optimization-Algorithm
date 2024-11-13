from PIL import Image
import diamondEncodingandDecode1 as DE
import cv2
import matplotlib.pyplot as plt
import math
from tkinter import filedialog
from skimage import io, img_as_float
from skimage.filters import gaussian
import numpy as np  # Import numpy for array operations


### performance parameters
### mse
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    img1 = Image.open(imageA, 'r').convert("L") 
    test1 = Image.Image.getdata(img1)  
    pixels_A=[]
    #print(len(test))
    for i in range(0,len(test1)-1):
        pixels_A.append(test1[i])
    
    img2 = Image.open(imageB, 'r').convert("L") 
    test2 = Image.Image.getdata(img2)  
    pixels_B=[]
    #print(len(test))
    for j in range(0,len(test2)-1):
        pixels_B.append(test2[j])
    sum=0
    for k in range(0,len(pixels_B)-1):
        err = (abs(pixels_A[k] - pixels_B[k]) ** 2)
        sum+=err
    error=sum/len(test2)
    return error
### end of MSE

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, sigma):
    noisy_image = image + np.random.normal(0, sigma, image.shape)
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def select_image_file():
    global input_path
    input_path = filedialog.askopenfilename(title="Select Image File")
    return input_path

img=select_image_file()

# Load the cover image
cover_img = Image.open(img, 'r').convert("L")
cover_array = np.array(cover_img)

# Add Gaussian noise to the cover image
sigma = 30  # Adjust sigma value as needed
noisy_cover_array = add_gaussian_noise(cover_array, sigma)
noisy_cover_img = Image.fromarray(noisy_cover_array)

# Display message about the noisy image being created
print("Noisy image created.")

# Display the noisy cover image
plt.imshow(noisy_cover_img, cmap='gray')
plt.title("Noisy Cover Image")
plt.axis('off')
plt.show()

    

cover_img = Image.open(img, 'r').convert("L") 
test = Image.Image.getdata(cover_img)  
cover_pixels=[]
#print(len(test))
for i in range(0,len(test)-1,2):
    cover_pixels.append([test[i],test[i+1]])
#print(cover_pixels)
print("Image has been converted to pixels ")

txt=input("Enter secret message: ")
res = ''.join(format(ord(i), '08b') for i in txt)
 
# printing result 
#print("The string after binary conversion : " + str(res))
    
sd=res
new_pixels=[]
#z=embedding parameter
#lw= (2*z*z + 2*z + 9)
#print("Lw is: ",lw)
for i in range(0,len(sd)):
    #print("Secret data to be embedded is: ",int(sd[i]))
    new_pixels.append(DE.diamond_encoding_new(cover_pixels[i][0],cover_pixels[i][1],int(sd[i])))


stego_pixels=new_pixels+cover_pixels[len(sd):]
#print("Stego pixels are: ", stego_pixels)

pixels_out = []
for row in stego_pixels:
    for tup in row:
        pixels_out.append(tup)
        
image_out = Image.new(cover_img.mode,cover_img.size)
image_out.putdata(pixels_out)

stego_name=input("Enter name for stego image with extension:")
image_out.save(stego_name)
print("Stego image has been created")


re_img = Image.open(stego_name, 'r').convert("L") 
test_d = Image.Image.getdata(re_img)  
re_pixels=[]
#print(len(test_d))
for i in range(0,len(test_d)-1,2):
    re_pixels.append([test_d[i],test_d[i+1]])
#print(cover_pixels)
final_bstr=''


for i in range(0,len(sd)):
    final_bstr+=DE.diamondDecode(re_pixels[i][0],re_pixels[i][1])

print()
#print("Final answer is: ",final_bstr)
print()

bin_data=final_bstr

def BinaryToDecimal(binary): 
		
	decimal, i=0,0
	while(binary != 0): 
		dec = binary % 10
		decimal = decimal + dec * pow(2, i) 
		binary = binary//10
		i += 1
	return (decimal) 


str_data =' '


for i in range(0, len(bin_data), 8):
	temp_data = int(bin_data[i:i + 8])
	decimal_data = BinaryToDecimal(temp_data)
	str_data = str_data + chr(decimal_data) 

# printing the result
print("Recovered Data is is:", str_data)

mse_value=mse(img, stego_name)
print("MSE VALUE IS: ", round(mse_value,2))
#calculate psnr
psnr= 10*(math.log10((255**2)/mse_value))
print("PSNR VALUE is: ",round(psnr,2))


def Coverdraw_histogram(image_filename):
    image = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure()
    plt.title('Histogram of Cover Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.plot(histogram, color='black')
    plt.xlim([0, 256])
    plt.show()
    print("Histogram of Coverimage created")
    
def stegodraw_histogram(image_filename):
    image = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.figure()
    plt.title('Histogram of Stego Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.plot(histogram, color='black')
    plt.xlim([0, 256])
    plt.show()
    print("Histogram of Stegoimage created")

# Draw histogram
Coverdraw_histogram(img)
stegodraw_histogram(stego_name)