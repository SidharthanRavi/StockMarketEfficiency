import requests

def lambda_handler(event, context):
    
    # Define the API URL
    api_url = "https://latest-stock-price.p.rapidapi.com/price"
    querystring = {"Indices": "NIFTY 50"}
    headers = {
        "X-RapidAPI-Key": "", #Enter Your Api Key 
        "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
    }

    try:
        # Make a GET request to the API
        response = requests.get(api_url, headers=headers, params=querystring)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
            return {
                'statusCode': 200,
                'body': data
            }
        
        else:
            return {
                'statusCode': response.status_code,
                'body': "API request failed"
            }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
