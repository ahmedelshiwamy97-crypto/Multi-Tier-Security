# Implementation and validation

## 1. Deployed architecture

- VPC `10.0.0.0/16` across two Availability Zones.
- Public subnets `10.0.1.0/24`, `10.0.2.0/24`.
- Private application subnets `10.0.11.0/24`, `10.0.12.0/24`.
- Private database subnets `10.0.21.0/24`, `10.0.22.0/24`.
- Internet Gateway and public routing.
- One NAT Gateway for private application outbound access (lab cost-saving choice).
- Public Application Load Balancer receives HTTP :80 and forwards to the private EC2 target on TCP :5000. Health endpoint: `/health`.
- Private EC2 runs Flask/Gunicorn and is managed through AWS Systems Manager.
- Private Amazon RDS for MySQL 8.4, database `banking_db`, TCP :3306.
- Secrets Manager stores application DB credentials. The EC2 role is scoped to `GetSecretValue` for the application secret only.
- The database application user has SELECT-only access to the `accounts` table.
- RDS storage encryption uses a customer-managed AWS KMS key.
- CloudTrail is configured as a multi-region trail with log file validation and delivery to a private S3 bucket with Block Public Access and SSE-S3 encryption.

## 2. Validation performed

| Test | Observed result |
|---|---|
| Application `/health` | Responded successfully |
| Application `/api/accounts` | Returned three demo account records |
| Application secret access from EC2 role | Allowed |
| Master RDS secret access from EC2 role | Denied with `AccessDeniedException` |
| CloudTrail trail status | `IsLogging: true` |
| Non-empty CloudTrail log delivery | Not independently confirmed at validation time |

## 3. Security services not completed

- **GuardDuty:** detector creation failed because the AWS account required a service subscription. It is not enabled in this environment.
- **Security Hub:** status was not verified.
- **EventBridge and Lambda:** incident-response automation was not deployed. `lambda/incident_response.py` is reference-only.
- **CloudWatch retention:** setup was not completed because the target log group did not exist.

## 4. Known limitations

- HTTP only; TLS/HTTPS is not configured.
- No end-user authentication or authorization.
- Demo account data only.
- One NAT Gateway (single point of failure for outbound egress).
- RDS is Single-AZ in this cost-conscious lab.
- CloudTrail logging was enabled, but successful delivery of non-empty log files was not independently confirmed at the time of validation.

Do not describe this implementation as production-ready or as a fully deployed security monitoring/SOC solution.
