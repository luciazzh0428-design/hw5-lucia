# Presentation Order Picker Skill

## What

This skill generates a random presentation order for a group of participants.

## Why

In many team projects, deciding a fair speaking order can be difficult. A random selection ensures fairness and avoids bias. This task requires code because randomness cannot be reliably produced by a language model alone.

## How to use

Provide a list of participant names, and the skill will return a randomized presentation order.

## Script

The Python script uses the `random.shuffle()` function to randomly reorder the list of names and generate a fair sequence.

## What worked well

The skill is simple, practical, and reusable for real-world scenarios such as team presentations, meetings, or interviews.

## Limitations

The output is purely random and does not consider constraints such as priority or scheduling preferences.

## Reflection

This assignment helped me understand the difference between prompts and skills. I learned that some tasks, such as randomness, require deterministic code rather than relying only on AI. Combining AI instructions with scripts makes the solution more reliable and reusable.

## Video
(https://youtu.be/x-I33uBN20Q)
