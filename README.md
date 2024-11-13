Project Title: Intelligent Hybrid Steganography Optimization Algorithm
-
Digital image steganography refers to the practice of hiding secret messages into digital images with the intention of secret communication.
Steganography process hides the encrypted data such that nobody can suspect that there exists secret data.
Normally, the steganography system includes three components such as cover-object, secret data, and stego-object.
It considers three parameters for the processing which means capacity, security, and image quality.
The project aims to implement encryption of secret data into cover image as well as decryption of secret data from cover image using diamond encoding method.

Technologies Used:
-
Python, PIL, Matplotlib, TensorFlow

Results and analysis:
-
-> maximum embedd-able secret data possible achieved till 500 words/ one page worth of text
->the algorithm can embedd in B&W as well as color images without causing severe distortion to the image.
->algorithm optimises implemention of Diamond Enconding technique by assessing the image pixels.
-> image compression achieved on embedding
-> attack-proof against Gaussian noise, salt & pepper attack.
-> MSE & PSNR values of original and embedded images compared.


The primary result of our project was the successful concealment and recovery of hidden data within a stego-image. This outcome showcases the robustness and reliability of the steganographic method and encoding function employed in this experiment. When the decoding algorithm was applied to the stego-image, it meticulously reversed the encoding process, extracting the secret test data with complete accuracy. The data recovery was achieved without any loss or distortion, reinforcing the notion that this steganographic technique is both reliable and effective. This successful recovery of hidden data has significant implications in various fields, including data security, privacy, and covert communication. 
However, it is important to recognize that the effectiveness of steganography can be influenced by factors such as the choice of cover image, the encoding function used, and the degree of data hiding.

