# AWS cleanup guide

> **Warning:** Deleting resources is irreversible and may remove data. Save screenshots, logs, and any required evidence first. Confirm the account and region (`us-east-1`) before cleanup.

1. Delete the RDS DB instance `secure-banking-db`. Decide whether to retain a final snapshot; retained snapshots may continue to incur charges.
2. Delete the Application Load Balancer `Secure-Banking-ALB` and target group `Secure-Banking-TG`.
3. Terminate the private EC2 instance. Remove its instance profile/role only after confirming it is not shared.
4. Delete the NAT Gateway. After deletion completes, release its Elastic IP if it is no longer needed.
5. Stop/delete the CloudTrail trail as appropriate. Retain required audit evidence; only then empty and delete its S3 bucket.
6. Delete the application secret and RDS-managed secret when no longer required.
7. Schedule deletion of the customer-managed KMS key only after confirming no retained encrypted resources depend on it. KMS key deletion has a waiting period.
8. Remove security groups, route tables, subnets, Internet Gateway, and VPC after dependencies are removed.
9. Check EC2, RDS, VPC, S3, CloudTrail, Secrets Manager, and KMS billing/console pages for remaining resources.

Do not delete the KMS key or audit logs before deciding whether evidence must be retained. Verify all resources are in `us-east-1`.
