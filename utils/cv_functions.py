from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time


def authenticate_the_client(endpoint, key):
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    return client

def describe_image(client, image_url):
    '''
    Describe images with human-readable language with the confidence score.
    '''
    res = client.describe_image(image_url)
    
    print("des,\t-1,\t{}".format(res.request_id))
    cnt =0
    for caption in res.captions:
        if caption.confidence > 0.7:
            cnt +=1
            print("des,\t{:d},\t{:20s},\t{:.2f}%".format(cnt, caption.text, caption.confidence * 100))

def categorize_image(client, image_url):
    '''
    Categorize an Image with a confidence score.
    https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/concept-categorizing-images
    '''
    res = client.analyze_image(image_url , ["categories"])

    print("cat,\t-1,\t{},".format(res.request_id))
    cnt=0
    for category in res.categories:
        if category.score > 0.7:
            cnt +=1
            print("cat,\t{:d},\t{:20s},\t{:.2f}%".format(cnt, category.name, category.score * 100))

def detect_color_image(client, image_url):
    '''
    Detects the different aspects of its color scheme in a remote image.
    '''
    res = client.analyze_image(image_url, ["color"])

    print("clr,\t-1,\t{}".format(res.request_id))
    print("clr,\t{:d},\t{:20b},\t{}".format(1, res.color.is_bw_img, 'Is black and white'))
    print("clr,\t{:d},\t{:20s},\t{}".format(2, res.color.accent_color, 'Accent color'))
    print("clr,\t{:d},\t{:20s},\t{}".format(3, res.color.dominant_color_background, 'Dominant background color'))
    print("clr,\t{:d},\t{:20s},\t{}".format(4, res.color.dominant_color_foreground, 'Dominant foreground color'))
    cnt = 4
    for dom_color in res.color.dominant_colors:
        cnt +=1
        print("clr,\t{:d},\t{:20s},\t{}".format(cnt, dom_color, 'Dominant colors'))

def get_landmark_image(client,image_url):
    res = client.analyze_image_by_domain("landmarks", image_url)
    
    print("lnd,\t-1,\t{},".format(res.request_id))
    cnt=0
    for landmark in res.result["landmarks"]:
        
        if landmark.confidence > 0.7:
            cnt +=1
            print("tag,\t{:d},\t{:20s},\t{:.2f}%".format(cnt, landmark.name, landmark.confidence * 100))


def tag_image(client, image_url):
    '''
    Tag an Image for each thing in the image.
    '''
    res = client.tag_image(image_url)

    print("tag,\t-1,\t{},".format(res.request_id))
    cnt=0
    for tag in res.tags:
        if tag.confidence > 0.7:
            cnt +=1
            print("tag,\t{:d},\t{:20s},\t{:.2f}%".format(cnt, tag.name, tag.confidence * 100))

def extract_text_image(client, image_url):
    '''
    Extract handwritten text in an image
    from Microsoft's tutorial
    '''
    res = client.read(image_url,  raw=True)

    print("txt,\t-1,\t,")

    # Grab the ID from the URL
    operation_id = res.headers["Operation-Location"].split("/")[-1]

    # Call the "GET" API every 1 second and wait for it to retrieve the results 
    while True:
        get_handw_text_results = client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    cnt =0
    # Print the detected text, line by line
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
                cnt +=1
                print("txt,\t{:d},\t{:20s},".format(cnt, line.text ))
                #print(line.bounding_box)



