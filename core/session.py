from fastapi import Request
import time


session_store = {}

def get_or_create_session(request: Request):
    session_id = request.client.host  
    now = time.time()
    
    if session_id not in session_store:
        session_store[session_id] = {"count": 0, "last_active": now}
    else:
        session_store[session_id]["last_active"] = now
    
    session_store[session_id]["count"] += 1
    return session_id, session_store[session_id]