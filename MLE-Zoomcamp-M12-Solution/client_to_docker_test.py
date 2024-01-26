import requests

# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
url = 'http://localhost:9000/2015-03-31/functions/function/invocations'

# Create the event with the URL of the image
event = {
    "inputs": {
    "question": "That is a happy person",
    "answers" : [
        "That is a happy dog",
        "That is a very happy person",
        "Today is a sunny day"
        ]
    },
}

# Send POST request using requests module
response = requests.post(url, json=event)
# Print the response
print(response.text)
