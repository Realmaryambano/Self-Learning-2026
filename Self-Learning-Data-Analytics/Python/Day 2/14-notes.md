.strip() is used to remove spaces (and a few related characters).

Specifically, it removes:
- Leading spaces (at the start)
- Trailing spaces (at the end)

Example:
```python
word = "   hello   "
print(word.strip())
```

Output:
hello

Important points (simple):
- " hello".strip() → "hello"
- "hello ".strip() → "hello"
- " hello ".strip() → "hello"
- "he llo".strip() → "he llo" ❌ (spaces in the middle are NOT removed)

Related methods:
- .lstrip() → removes spaces from the left only
- .rstrip() → removes spaces from the right only

So yes, when used .strip() in your code, you were cleaning the user input by removing extra spaces at the beginning and end.
