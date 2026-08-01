# Precision Lane

Use this lane when the prompt is vague, risky, privacy-sensitive, or likely to benefit from one sharply targeted question.

## Best for

- unclear requests
- privacy-sensitive prompts
- claims that may be weak or time-sensitive
- requests where one missing detail would change the answer

## Typical input

- a prompt with hidden assumptions
- a request that might leak private details
- a task that needs one small clarifying question

## Typical output

- what is unclear
- what is risky
- what can be assumed safely
- the smallest next question or next action

## Do not use it for

- asking too many broad questions
- turning uncertainty into confidence
- asking for details that do not change the artifact

## Privacy boundary

If a prompt includes private paths, account data, secrets, or screenshots with hidden context, generalize them before proceeding and do not echo them back in public-facing text.
