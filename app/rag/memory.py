SESSION_MEMORY = {}

def get_contextual_question(session_id: str, question: str):
    if session_id in SESSION_MEMORY:
        return SESSION_MEMORY[session_id] + " " + question
    return question

def update_session(session_id: str, question: str):
    SESSION_MEMORY[session_id] = question
