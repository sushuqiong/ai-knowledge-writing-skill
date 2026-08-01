# Precision Lane

Use this lane when the prompt is vague, risky, privacy-sensitive, or likely to benefit from one sharply targeted question.

## Trigger

- the request could mean more than one thing
- a hidden assumption would change the output
- the task might leak private details
- the claim is weak, speculative, or time-sensitive

## What to do

- identify the one missing detail that matters most
- ask the minimum number of questions needed to move forward
- state safe assumptions when a full question is not necessary
- separate facts, inference, and uncertainty
- stop unsupported claims from slipping into the output

## Default output

- what is unclear
- what is risky
- what can be assumed safely
- the smallest next question or next action

## Common mistakes

- asking too many broad questions
- turning uncertainty into confidence
- asking for details that do not change the artifact
- overlooking privacy risk because the request sounds simple

## Privacy boundary

If a prompt includes private paths, account data, secrets, or screenshots with hidden context, generalize them before proceeding and do not echo them back in public-facing text.
