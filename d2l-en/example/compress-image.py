import cv2
import numpy as np

def compress_image(image_path, quality=90):
    # Read the image
    img = cv2.imread(image_path)
        
        # Encode the image with JPEG compression
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)
        
        # Decode the compressed image
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    
    return decoded_img

compressed_img = compress_image('original_image.jpg', quality=50)
print(compressed_img)
