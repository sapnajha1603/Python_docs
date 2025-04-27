import requests

# Make a GET request to a URL
response = requests.get('https://www.google.com')

# Print the response text (the content of the requested file)
print(response.text)  # Response content

# Print the status code (200 means OK)
print(f" the response is : {response.status_code}")
