import json
import boto3
import urllib3
def lambda_handler(event, context):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://api.openweathermap.org/data/2.5/forecast?id=1277333&appid=2c74f19547a0ea66b0346134f1dc94e5')
    print(r.data)
    print(r.status)
    client = boto3.client('s3')
    client.put_object(Body=r.data, Bucket='dgapi', Key='datafile.json')
