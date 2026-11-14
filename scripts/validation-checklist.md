# Validation checklist

Use this checklist when reviewing the live AWS environment. Mark an item complete only after collecting current evidence.

- [ ] Confirm region and account.
- [ ] Confirm VPC CIDR and subnet CIDRs.
- [ ] Confirm public ALB listener and target group port.
- [ ] Confirm target health and `/health` response.
- [ ] Confirm EC2 has no public IPv4 address and is SSM managed.
- [ ] Confirm app security group only permits the intended ALB-to-app path.
- [ ] Confirm RDS is private and reachable only from the application tier.
- [ ] Confirm application role can retrieve only the intended application secret.
- [ ] Confirm database application user permissions.
- [ ] Confirm RDS encryption and KMS key.
- [ ] Confirm CloudTrail is logging and verify actual non-empty S3 log objects.
- [ ] Confirm S3 Block Public Access and encryption.
- [ ] Record GuardDuty and Security Hub status accurately.
- [ ] Confirm whether EventBridge/Lambda automation is deployed and tested.
- [ ] Review current billing and remove unused lab resources.
