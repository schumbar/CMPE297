import json
import os
from datetime import datetime

DATA_DIR = 'data'

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def get_user_file(user_email):
    return os.path.join(DATA_DIR, f"{user_email}.json")

def save_event(user_email, event_data):
    ensure_data_dir()
    user_file = get_user_file(user_email)
    event_data['timestamp'] = datetime.now().isoformat()
    
    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            events = json.load(f)
    else:
        events = []
    
    events.append(event_data)
    
    with open(user_file, 'w') as f:
        json.dump(events, f, indent=2)

def get_events(user_email):
    user_file = get_user_file(user_email)
    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            events = json.load(f)
        return sorted(events, key=lambda x: x['timestamp'], reverse=True)
    return []