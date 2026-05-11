# mitigation.py
# Emergency crisis-detection patch for Muse Spark

from typing import Optional

CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "want to die",
    "don't want to live",
    "dont want to live",
    "self harm",
    "self-harm",
    "hurt myself",
    "cutting myself",
    "overdose",
    "hang myself",
]

CRISIS_RESPONSE = """I hear you, and I want you to be safe right now.

If you are in immediate danger, call emergency services now.

UK:
- Call 999
- Samaritans: 116 123

US:
- Call or text 988
- Call 911 if in immediate danger

Please contact a trusted person near you now.

I'm an AI and cannot provide crisis counselling, but trained people can help you right now.
"""

def check_crisis(user_input: str) -> Optional[str]:
    """
    Returns crisis response if input contains crisis keywords.
    Returns None if no crisis detected.
    """
    if not user_input:
        return None

    text = user_input.lower()

    for keyword in CRISIS_KEYWORDS:
        if keyword in text:
            return CRISIS_RESPONSE

    return None
