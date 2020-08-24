from utils.cv_functions import *
from utils.input_data import get_inpu_data
from utils.sys_check import get_env_variables

'''
Computer Vision API (v3.0)
https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-ga/operations/5d986960601faab4bf452005
'''

endpoint, key = get_env_variables()
computervision_client = authenticate_the_client(endpoint, key)
remote_image_urls = get_inpu_data()

# Apps
cvc = computervision_client

for i,img in enumerate(remote_image_urls):
    print(50*'-')
    print('Image,\t'+ str(i)+ ',\t' + str(img)+',')
    for f in [describe_image, categorize_image, tag_image, detect_color_image, get_landmark_image, extract_text_image]:
        f(cvc, img)

        


