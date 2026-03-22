# Threat Model

## Identified Threats

### 1. Token Forgery  
- Risk: Attackers generate fake JWT tokens
- Mitigation: 
    - Secure secret key (env variable)
    - assmebly signature verification

---

### 2. Privilege Escalation  
- Risk: Users gain unauthorized roles
- Mitigation: 
    - Role-Based Access Control (RBAC)

---

### 3. SQL Injection  
- Risk: Malicious database queries
- Mitigation: 
    - Parameterized queries

---

### 4. Tokenn Replay  
- Risk: Reuse of stolen tokens
- Mitigation: 
    -Token expiration (`exp` field)

---

### 5. Weak secret Management
- Risk: Hardcoded secrets exposed
- Mitigation: 
    - Environment Variables
