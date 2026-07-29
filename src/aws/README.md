# AWS Services

This folder has all the AWS infrastructure code and config files for SentinelGraph.

## Folder layout

```
aws/
├── lambda/      - Lambda function handlers
├── s3/          - S3 bucket policies
├── ec2/         - EC2 setup scripts
├── iam/         - IAM roles and policies (no credentials here ever)
└── cloudwatch/  - CloudWatch dashboards and alarms
```

## Services we are using

| Service | What it does in our project |
|---------|----------------------------|
| EC2 | tenant simulation + web dashboard |
| S3 | store logs, graphs, model files |
| CloudTrail | captures IAM/API activity for identity edges in graph |
| VPC Flow Logs | captures network traffic for resource-abuse edges in graph |
| CloudWatch | resource metrics for mitigation controller, pipeline monitoring |
| Lambda | ETL, graph building, risk scoring, pipeline glue |
| SageMaker | train and serve the GNN |
| Step Functions | orchestrate the mitigation workflow |
| RDS | graph metadata, risk scores, history |
| IAM | access control, also provides the role/permission structure the graph models |
| Cognito | auth for dashboard users |
| SNS / SES | abuse alerts |
| QuickSight | dashboards |

**Important: never commit AWS keys, .pem files, or credentials to this repo.**
