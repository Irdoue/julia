import boto3
import botocore.exceptions
import json
from lib import make_plan, save_pic, make_julia_step, file_to_plan, plan_to_file;

def lambda_handler(event, context):
    
    #Format s3
    constants = [0.25+0.5j, -0.5251993, 0.285 + 0.01j, -0.7269 + 0.1889j, 0.7885, 0.28+0.008j, 0.3 + 0.5j, -1.417022285618 + 0.0099534j, 0.285 + 0.013j, 0.8 + 0.2j, 1, -0.8 + 0,156j]
    c = constants[int(event['queryStringParameters']['set_ID'])]
    user_ID = event['queryStringParameters']['user_ID']
    dec = int(event['queryStringParameters']['resolution']) + 1
    s3 = boto3.resource('s3')
    bucket_name = 'lecompartimentdeirdoue'
    
    #Importing plan
    key = user_ID + '.plan'
    try:
        s3.Bucket(bucket_name).download_file(key, '/tmp/' + key)
        plan = file_to_plan(user_ID)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
           plan =  make_plan(dec)
           
    #Making new plan and picture
    pic_file_path = '/tmp/' + user_ID + '.png'
    plan = make_julia_step(plan, c)
    save_pic(plan, pic_file_path)
    
    s3 = boto3.client('s3')
    
    #Uploading new picture
    filename = '/tmp/' + user_ID + '.png'
    key = user_ID + '.png'
    s3.upload_file(filename, bucket_name, key)
    
    #Saving new plan
    plan_to_file(plan, user_ID)
    filename = '/tmp/' + user_ID + '.plan'
    key = user_ID + '.plan'
    s3.upload_file(filename, bucket_name, key)
    

    
    return {
        'statusCode': 200,
    }