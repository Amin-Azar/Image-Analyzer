import json

def get_inpu_data():
    '''
    Sample Image
    '''

    with open('data/input-images.json') as f:
        data = json.load(f)
        return data['live-cams']
