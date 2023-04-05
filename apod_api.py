'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import sys
import requests

dev_key = 'iAqY4P2RxYRWc6KsvVmWUzf0l3WSVxDofzxelxvj'


def main():
    
    apod_info = get_apod_info('2018-12-31')
    print(apod_info)
    
    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    payload = {'api_key': dev_key, 'date': apod_date.isoformat()}
    
    req = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    
    if req.status_code == 200:
        return req.json()
    
    return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    
    if apod_info_dict['media_type'] == 'image':
        return apod_info_dict['hdurl']
    elif apod_info_dict['media_type'] == 'video':
        print("This apod date features a video, cannot download !!!")
        sys.exit(1)
     
    return None

if __name__ == '__main__':
    main()