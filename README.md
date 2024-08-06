# aws-pipeline-template
An example template that builds a full Code Pipeline stack in AWS and will link to a GitHub Repo.

NOTE: This repo is for example and PoC purposes, in order to use this for your testing you will need to modify fields such as <your-account-id> and provide AWS Paramater Store variables. You will also need GitHub repos to reference in order for this to build properly.

I use .csv files to deploy this in bulk with an SDK, but you can just use the template by itself in cloudformation if you want. 
