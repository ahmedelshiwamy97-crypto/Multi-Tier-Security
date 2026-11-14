"""Reference-only Lambda sketch. This function was not deployed in the AWS lab."""
import json
import os

import boto3

sns = boto3.client("sns")
TOPIC_ARN = os.environ.get("ALERT_TOPIC_ARN")


def lambda_handler(event, context):
    """Forward a sanitized EventBridge security finding to an SNS topic.

    Deployment requires an SNS topic, environment configuration, IAM permissions,
    EventBridge rules, and end-to-end testing. This repository file alone does not
    create or activate any of those resources.
    """
    detail = event.get("detail", {})
    finding_id = detail.get("id", "unknown")
    finding_type = detail.get("type", event.get("detail-type", "Security event"))
    severity = detail.get("severity", {}).get("label", "UNKNOWN")
    message = {
        "finding_id": finding_id,
        "finding_type": finding_type,
        "severity": severity,
        "region": event.get("region", "unknown"),
        "account": event.get("account", "unknown"),
    }

    if not TOPIC_ARN:
        return {
            "statusCode": 200,
            "body": json.dumps({"status": "reference-only", "finding": message}),
        }

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="AWS security finding",
        Message=json.dumps(message),
    )
    return {
        "statusCode": 200,
        "body": json.dumps({"status": "notification-sent", "finding_id": finding_id}),
    }
