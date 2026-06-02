# Project context for Claude

## What this is
A growing collection of LeetCode solutions in Python. Lowest-priority repo of the four-project portfolio — its job is to demonstrate steady DSA practice over time, not headline thinking.

## Layout
Flat. No folders. Every solution sits at the repo root.

```
<repo>/
├── 0001_two_sum.py
├── 0002_<next>.py
├── ...
├── README.md           (index table, one row per problem)
├── LICENSE
└── .gitignore
```

## Naming
`<4-digit-problem-number>_<snake_case_title>.py`

Examples:
- `0001_two_sum.py`
- `0020_valid_parentheses.py`
- `0121_best_time_to_buy_and_sell_stock.py`

Four-digit padding so files sort numerically.

## File template
Every solution file follows the same shape:

```python
"""
<number>. <Title>  (<Difficulty>)

Problem summary in your own words (1-3 sentences).
Approach explained.

Time:  O(...)
Space: O(...)
"""
from typing import List  # if needed


class Solution:
    def <leetcodeMethodName>(self, ...) -> ...:
        ...


if __name__ == "__main__":
    assert Solution().<method>(<input>) == <expected>
    # a couple more cases
    print("ok")
```

## Conventions
- One `class Solution` per file with the LeetCode-style method name (camelCase, matches the LeetCode signature exactly).
- Smoke test at the bottom — running `python <file>.py` should print `ok`.
- When adding a new problem, also add a row to the table in `README.md`.
- **Commit messages**: `add <###>. <title>` for new problems, `refactor <###>: <change>` for revisions.
- **No Claude co-author trailer**.
- Per-repo git identity: `user.name=abdullah5111`, `user.email=abdullahsajjad489@gmail.com`.

## Status
Local only. One solution: `0001_two_sum.py`. Not yet `git init`-ed or pushed.

## What's next
See [NEXT_STEPS.md](./NEXT_STEPS.md).
