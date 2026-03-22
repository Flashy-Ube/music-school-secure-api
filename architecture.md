# Architecture

## Flow

1. CLient sends login request
2. Server verifies credentials
3. JWT toke is generated
4. Client send token in Authorization Header
5. Assembly Module verfies otken signature
6. Fast API Validates payload
7. RBAC checks user role
8. Access granted or denied

---

## Components

- FastAPI backend
- JWT Authentication layer
- assmebly verification module
- Database layer


Client
   |
OAuth2 Authentication
   |
API Server (Fast API)
   | 
Assembly Token Validator
   | 
RBAC Access Control
   |
PostgreSQL Control

