import boto3
import json
import csv

#Create CloudFormation client
cf = boto3.client('cloudformation')


with open('./test-deploy.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for index, row in enumerate(reader, start=1): #TODO: Temporarily set to 1 for testing. Will remove index, enumerate, and start in final version.
        stack_name = row[0]
        cf.delete_stack