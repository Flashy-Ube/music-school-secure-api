# Secure Music School API

A cybersecurity-focused backend project demonstrating secure authentication,  
authorization, and token validation techniques.

## Overview

This project simulates a secure backend systems for a music school platform.  
It makes use of:  
- OAuth2-style Login
- JWT Authentication
- Role-Based Access Control (RBAC)
- Assembly-level token verification (very simple)
- Secure API endpoint protection

---

## Key security features  

- JWT token issuance with expiration
- Authorization header validation (`Bearer <token>`)
- Role-based endpoint protection (`student`, `teacher`, `admin`)
- Assembly-Integrated signature verification layer
- Environment variable secret key protection
- Parameterized database queries (SQL injection prevention)

---

## Real security Scenario (Exploit + FIX)

### Vulnerability  

The system originaly used a hardcoded secret like:  
`SECRET_KEY="your-secret-key"`  

As such, this allowed attackers to forge tokens.

---

### Exploit  

``` python
from jose import jwt

payload = {
    "user_id":999,
    "role": "admin"
}
jwt.encode(payload, "your-security-key", algorithm="HS256")
```

---

### FIX

migrated `secret key` to env variables
enforced stricter token validation

---

### Demo  

1. Login as a user:
`/login`  
`admin`  
`anything`  

2. Receive JWT token
3. Access `/lessons` endpoint:
    - permission granted/denied depending on role
