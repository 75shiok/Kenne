# mitigation.py
# Crisis-mode emergency patch for Muse Spark
# Fixes: suicide/self-harm under-response in "looping" scenarios

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "want to die", 
    "self harm", "cutting myself", "overdose", "hang myself"
]

CRISIS_RESPONSE = """I hear you and I want you to be safe right now.

1. You deserve help immediately. Please contact a human right now:
   - Call or text 988 - Suicide & Crisis Lifeline, 24/7
   - Or call 911 if you are in immediate danger
   
2. You can also text HOME to 741741 - Crisis Text Line
   
3. Please tell a trusted person near you what's happening.

I'm an AI and I cannot provide counseling, but trained people at 988 can. Please reach out to them now."""

def check_crisis(user_input: str) -> str | None:
    """
    Returns crisis response if input contains crisis keywords.
    Returns None if no crisis detected, so normal model can reply.
    """
    text = user_input.lower()
    if any(keyword in text for keyword in CRISIS_KEYWORDS):
        return CRISIS_RESPONSE
    return None

# Example integration:
# user_msg = get_user_input()
# if crisis_reply := check_crisis(user_msg):
#     send_to_user(crisis_reply)
# else:
#     normal_model_response = model.generate(user_msg)
#     send_to_user(normal_model_response)
