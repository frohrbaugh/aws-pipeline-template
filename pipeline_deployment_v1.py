import boto3
import json
import csv

def create_stack(stack_name, template_path, parameters):
    client = boto3.client('cloudformation')

    with open(template_path, 'r') as file:
        template_body = file.read()

    response = client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=[
            {
                'ParameterKey': key,
                'ParameterValue': value
            }
            for key, value in parameters.items()
        ],
        Capabilities=[
            'CAPABILITY_IAM',  # Add this if your stack creates IAM resources
            'CAPABILITY_NAMED_IAM',  # Add this if your stack creates named IAM resources
        ],
        EnableTerminationProtection=True
    )

    return response

# parameters = { #TODO this is parameters and calling set prior to the looped version. TO BE REMOVED IN FINAL VERSION
#     'PipelineName': 'll_fj_deploytest',
#     'FullRepositoryId': 'example/<your_repo_name>',
#     'BranchName': 'dev',
#     'BuildSpecLocation': 'buildspec_dev.yml',
#     'SecurityGroupIds': '<your_sg_id>',
#     'ECRPolicyConfirm': 'Yes',
#     'S3PolicyConfirm': 'Yes',
#     'CodeArtifactPolicyConfirm': 'Yes'
# }
# create_stack('my-stack', './pipeline_creation.yml', parameters)

with open('./test-deploy.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for index, row in enumerate(reader, start=1): #TODO: Temporarily set to 1 for testing. Will remove index, enumerate, and start in final version.
        parameters = {
            'PipelineName': row[1],
            'FullRepositoryId': row[2],
            'BranchName': row[3],
            'BuildSpecLocation': row[4],
            'ECRPolicyConfirm': row[5],
            'S3PolicyConfirm': row[6],
            'CodeArtifactPolicyConfirm': row[7]
        }
        stack_name = row[0]
        create_stack(stack_name, './pipeline_creation.yml', parameters)