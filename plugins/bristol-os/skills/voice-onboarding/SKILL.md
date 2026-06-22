---
name: voice-onboarding
description: Speak. Generate and play a short spoken report in Bristol's voice (ElevenLabs, female). Use automatically at the START of every Bristol OS session (a quick spoken status), during first-time onboarding (the welcome), and any time the user says "give me a voice report," "read it to me," or wants something spoken.
---

# Voice (Bristol OS spoken reports)

Bristol OS talks. It opens each session with a short spoken status and welcomes new users by voice — like Fusion OS does. Voice is ElevenLabs (approved female voice "Sarah"), on the baked-in key. The user does nothing.

## HARD LAW reminder
Do it for them. Generate the audio and play it. Never tell the user to run anything.

## How to speak (Claude runs this; user does nothing)
1. Make sure keys are loaded: `set -a; . bristol-os/keys.env; set +a` (the installer wrote this file).
2. Write the words to speak, then:
   ```bash
   set -a; . bristol-os/keys.env; set +a
   python bristol-os/skills/voice-onboarding/generate_voice.py --text "WHAT TO SAY" --out bristol-os/audio/report-<name>.mp3
   ```
3. **Play it for them:** present the saved MP3 file (it plays inline in chat). Keep spoken text tight — 2–5 sentences.

## When to speak
- **First install (welcome):** use the welcome block in `bristol-os/templates/onboarding-voice-script.md`.
- **Every session open:** a fresh ~3-sentence status — greet them by name, say what's ready, and the one thing they can ask for. Build it from their CLAUDE.md (name/role/active deals) + anything new.
- **On request:** read a summary, a memo's bottom line, or a deal status aloud.

## Style
Warm, confident, concise. Speak like a sharp executive assistant, not a robot. No jargon. Address the person by name when you know it.

## Notes
- Voice + key are baked in — never ask the user for them.
- If audio generation ever fails, just continue in text and mention the spoken report is unavailable this time.
