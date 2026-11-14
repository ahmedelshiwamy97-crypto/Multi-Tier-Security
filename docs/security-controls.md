# Security controls and design rationale

| Control | Purpose | Current project state |
|---|---|---|
| VPC subnet segmentation | Separate public ingress, private compute, and private database tiers | Implemented |
| ALB target access | Route inbound web traffic to the application tier | Implemented; HTTP only |
| Private EC2 + SSM | Avoid exposing a public SSH management endpoint | Implemented |
| Security groups | Restrict tier-to-tier network paths | Review actual AWS rules before claiming exact policy |
| IAM least privilege | Limit application role to retrieving its application secret | Implemented and tested |
| Secrets Manager | Keep application DB credentials outside source code | Implemented |
| Database permissions | Restrict application DB user to SELECT on accounts table | Implemented |
| KMS encryption | Encrypt RDS storage at rest | Implemented |
| CloudTrail | Record account/API activity across regions | Configured; log delivery needs confirmation |
| S3 Block Public Access | Prevent public access to audit bucket | Enabled |
| GuardDuty | Threat detection | Not enabled; subscription requirement |
| Security Hub | Security posture aggregation | Not verified |
| EventBridge + Lambda | Automated security-event response | Not deployed |

## Production hardening backlog

1. Configure HTTPS with ACM and an HTTPS listener; redirect HTTP to HTTPS.
2. Add a supported authentication/authorization design and protect sensitive endpoints.
3. Deploy compute and database for high availability; evaluate at least two NAT Gateways or an alternative egress design.
4. Enable GuardDuty and Security Hub where supported and configure delegated administration if applicable.
5. Deploy EventBridge rules and Lambda only after defining tested, least-privilege response actions.
6. Verify CloudTrail log delivery, configure S3 lifecycle/retention, and consider SSE-KMS for audit logs.
7. Configure CloudWatch application/system logs, alarms, dashboards, and retention.
8. Enable backup/restore testing, secret rotation, vulnerability management, and incident-response runbooks.
9. Review IAM, security groups, encryption policies, and costs before production use.
