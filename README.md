Simple Python Redactor. Takes a string and a list of banned words and outputs the string with those banned words redacted. 

## How to run

Run the example:

```
python3 redactor.py
```

Run the tests (requires pytest):

```
pip install pytest
pytest
```

## Design decisions

The program goes through the text one character at a time. Letters are collected into the current word, and any non-letter (a space, punctuation, a number) marks the end of that word. This keeps all spacing and punctuation exactly as it was, so only banned words change.

The output is built in a list and joined at the end, rather than adding to a string each time. Python strings can't be changed, so every `+=` on a string creates a whole new copy, while appending to a list doesn't.