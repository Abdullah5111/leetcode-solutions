# Next steps

## Get it on GitHub
- [ ] `python 0001_two_sum.py` prints `ok`
- [ ] Init git, commit, push (see d:\Github\PORTFOLIO.md for the command sequence)

## Steady cadence — the *only* feature this repo needs
This repo's value to clients is **showing consistent DSA practice over time**. The single best thing you can do here is add one problem per session (or per few days) as you actually solve them. Quality > quantity.

For each new problem:
1. Create `<4-digit-number>_<snake_case_title>.py` at the repo root following the file template in [CLAUDE.md](./CLAUDE.md).
2. Add a smoke test at the bottom.
3. Run it: `python <file>` should print `ok`.
4. Add a row to the table in `README.md`.
5. Commit: `add <###>. <title>`.

## Suggested next problems (Easy → Medium ramp)

- [ ] 9. Palindrome Number (Easy)
- [ ] 13. Roman to Integer (Easy)
- [ ] 14. Longest Common Prefix (Easy)
- [ ] 20. Valid Parentheses (Easy)
- [ ] 21. Merge Two Sorted Lists (Easy)
- [ ] 26. Remove Duplicates from Sorted Array (Easy)
- [ ] 53. Maximum Subarray (Medium — Kadane's)
- [ ] 70. Climbing Stairs (Easy — Fibonacci DP)
- [ ] 121. Best Time to Buy and Sell Stock (Easy)
- [ ] 125. Valid Palindrome (Easy)
- [ ] 136. Single Number (Easy — XOR trick)
- [ ] 141. Linked List Cycle (Easy — Floyd's)
- [ ] 217. Contains Duplicate (Easy)
- [ ] 226. Invert Binary Tree (Easy)
- [ ] 242. Valid Anagram (Easy)

Don't grind them all in one sitting — the point is the cadence on your contribution graph.

## Quality improvements (later, optional)
- [ ] Add a `.github/workflows/test.yml` that runs every solution file (or a discoverer script that finds all `*.py` and runs them) so you get a green checkmark per push
- [ ] Group the README index by topic once you have ~20 problems
- [ ] Optionally add a second language for the strongest problems (C++ or Go)
