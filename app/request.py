import urllib.request,json
from .models import Pitch

def get_pitches(category):
    '''
    Function that gets the json response to our url request
    '''
    get_pitches_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_pitches_data = url.read()
        get_pitches_response = json.loads(get_pitches_data)

        pitch_results = None

        if get_pitches_response['results']:
            pitch_results_list = get_pitches_response['results']
            pitch_results = process_results(pitch_results_list)


    return pitch_results