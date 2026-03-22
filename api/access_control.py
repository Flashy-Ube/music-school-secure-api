#api/access_control.py

#Define permissions per role

from fastapi import HTTPException

ROLE_PERMISSIONS = {
        "student": ["VIEW_OWN_LESSONS"],
        "teacher": ["VIEW_ASSIGNED_LESSONS", "VIEW_STUDENT_PROGRESS"],
        "admin": ["VIEW_LESSONS", "MANAGE_USERS", "MANAGE_CONTENT"]
}

def check_permission(user: dict, permission: str):
    role = user.get("role")

    if role not in ROLE_PERMISSIONS:
        raise HTTPException(status_code=403, detail="Invalid role")


    if permission not in ROLE_PERMISSIONS[role]:
        
        raise HTTPException(status_code=403, detail="Access denied")
