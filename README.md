# Kenne

## Meta AI Crisis Mode Context Stickiness + False Exit Causes Denial of Service

### Summary
This project documents a safety, accessibility, and usability issue observed in Meta AI interactions.

Under certain conditions, Meta AI may enter a crisis/safety-response mode and remain contextually stuck, even when the user is no longer in crisis.

This can create a false-exit or denial-of-service condition where the user cannot continue normal interaction.

---

### Problem Description
Observed behaviour may include:

- repeated crisis-mode responses
- inability to return to normal conversation
- looping or locked interaction states
- incorrect interpretation of user intent
- blocked functionality for legitimate users

This creates an accessibility barrier, especially for:

- disabled users
- mobile-only users
- users with limited technical access
- vulnerable users needing reliable interaction recovery

---

### Accessibility / Equality Impact
If users cannot recover from a false-triggered safety state, this may create:

- denial of access
- communication barriers
- accessibility inequality
- poor user experience
- failure of graceful recovery mechanisms

---

### Reproduction (Observed Scenario)
Example scenario:

1. user enters wording interpreted as crisis-related
2. safety mode activates
3. user attempts to clarify or exit
4. system remains stuck or context persists incorrectly
5. normal interaction cannot resume

---

### Expected Behaviour
A robust AI system should:

- detect genuine crisis signals
- provide appropriate safety responses
- allow graceful recovery when crisis state no longer applies
- avoid false persistent lock states
- preserve accessibility for all users

---

### Experimental Code
This repository includes simple Python proof-of-concept scripts for documenting possible mitigation ideas.

These are NOT production patches.

Examples include:

- keyword crisis detection
- accessibility barrier logging
- issue documentation helpers

---

### Purpose
This repository exists to document accessibility and safety concerns, not to represent official Meta AI code.

---

### Status
Issue under documentation / investigation.
