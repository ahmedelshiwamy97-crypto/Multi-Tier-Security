# Application component

The AWS lab runs a Flask application behind an Application Load Balancer using Gunicorn on TCP port `5000`.

Observed endpoints during validation:
- `GET /health` — health-check endpoint.
- `GET /api/accounts` — returns three demo account records.

The application source was not present in the GitHub repository snapshot used to prepare this package. This folder documents the deployed component without inventing or fabricating application source code.

Do not add credentials, `.env` files, database passwords, secret ARNs, or real customer data to this repository.
