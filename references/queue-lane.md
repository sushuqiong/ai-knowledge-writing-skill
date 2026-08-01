# Queue Lane

Use this lane when the request contains several tasks, needs prioritization, or requires inserting an urgent item into an existing plan.

## Trigger

- multiple files or outputs are requested
- the user asks for "step by step" execution
- one task depends on another
- the user wants queueing, priority, or handoff rules

## What to do

- split the work into clear steps
- mark the current step, the next step, and anything blocked
- keep dependencies explicit
- insert urgent tasks without losing already completed work
- avoid parallel work when one step must finish first

## Default output

- ordered queue
- status for each item
- what is blocked and why
- what can be done immediately

## Common mistakes

- mixing plan updates with final output
- hiding dependency order
- skipping a small urgent fix because it is not "part of the main task"
- restarting the whole queue when only one lane changed

## Privacy boundary

When queueing public work, keep task labels generic and avoid embedding private repository names, machine paths, or unpublished personal details.
