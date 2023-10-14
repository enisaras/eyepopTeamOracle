import requests
import os
from dotenv import load_dotenv

# Hide Auth key used across app
load_dotenv()
API_KEY = os.getenv('API_KEY')


# header information
headers_get = {
    'Authorization': 'Bearer '+API_KEY,
    'Content-Type': 'application/json',
}

# Variables used across calls to AI server
def getConfig(url):
    response = requests.get(url, headers=headers_get).json()
    print(response)
    return response['url'], response['pipeline_id']

# Send image link for analysis, source is an OCI Bucket
def setSource(imageURL, pipelineURL, pipelineID):
    headers = {
        'content-type': "application/json"
    }
    data = \
    """
    {
        "source": {
            "sourceType": "URL",
            "url": "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idessoelsq5l/b/EyePopAIHackathon/o/peopleportrait-smiling-young-friends-walking-260nw-1392193913.jpg"
        }
    }
    """
    target = f"{pipelineURL}/pipelines/{pipelineID}/source?mode=queue&processing=sync"
    response = requests.patch(target, headers=headers, data=data)
    print(response.text)

pipeline_url, pipeline_id = getConfig('https://api.eyepop.ai/api/v1/user/pops/92/config')

test_image_link = "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idessoelsq5l/b/EyePopAIHackathon/o/tomato.jpeg"
setSource(test_image_link, pipeline_url, pipeline_id)