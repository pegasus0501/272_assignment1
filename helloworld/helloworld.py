import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    try:
        # Attempt to get responses from the microservices
        hello_response = requests.get("http://34.134.245.100/hello")
        hello_response.raise_for_status()  # Raises an HTTPError if the response was an error
    except requests.exceptions.RequestException as e:
        # Handle any errors that occurred during the request to the hello service
        return Response(f"Error contacting hello service: {e}", status=500)

    try:
        world_response = requests.get("http://34.29.141.164/world")
        world_response.raise_for_status()  # Raises an HTTPError if the response was an error
    except requests.exceptions.RequestException as e:
        # Handle any errors that occurred during the request to the world service
        return Response(f"Error contacting world service: {e}", status=500)

    # Combine the results
    result = hello_response.text + " " + world_response.text
    return result

if __name__ == "__main__":
    app.run(port=5006)