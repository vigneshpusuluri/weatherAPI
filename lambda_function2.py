import json
import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    dynamodb_client = boto3.client('dynamodb')
    content_object = s3.Object('dgapi', 'datafile.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    data = json.loads(file_content)
 
    dynamodb_client.put_item(TableName='apidata',
    Item={
        "datetime":{"S":data['list'][0]["dt_txt"]},
        "weather_description":{"S":data['list'][0]['weather'][0]['description']},
        "temp":{"S":str(data['list'][0]['main']['temp'])},
        "temp_min":{"S":str(data['list'][0]['main']['temp_min'])},
        "temp_max":{"S":str(data['list'][0]['main']['temp_max'])},
        "pressure":{"S":str(data['list'][0]['main']['pressure'])},
        "humidity":{"S":str(data['list'][0]['main']['humidity'])},
        "visibility":{"S":str(data['list'][0]['visibility'])},
        "wind_speed":{"S":str(data['list'][0]['wind']['speed'])},
        "wind_deg":{"S":str(data['list'][0]['wind']['deg'])},
        "cloud":{"S":str(data['list'][0]['clouds']['all'])},
        "sunrise":{"S":str(data['city']['sunrise'])},
        "sunset":{"S":str(data['city']['sunset'])}
        }
    )