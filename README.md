# Birthday Problem

A Python simulation of the [Birthday Problem](https://en.wikipedia.org/wiki/Birthday_problem) — a classic probability puzzle.

## What it does

For each group size from 1 to 100, it calculates the probability that at least two people in the group share a birthday.

## Usage

```bash
python bday-problem.py
```

## Example output

```
1 people: 0.0
2 people: 0.0027...
...
23 people: 0.5073...  ← over 50% chance at just 23 people!
...
100 people: ~1.0
```

## The math

The probability that **at least two people share a birthday** is calculated as:

```
P = 1 - (365 × 364 × 363 × ... × (365 - n + 1)) / 365^n
```

where `n` is the number of people.
