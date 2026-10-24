
"""Tests for the redactor."""

from redactor import mask, redact


def test_mask_replaces_every_letter():
    assert mask("dog") == "###"

def test_redact_handles_mixed_case_and_punctuation(): 
    assert redact("FOX, Fox and fox! and fox!!", ["fox"]) == "###, ### and ###! and ###!!"

def test_redacted_words_within_words_stay(): 
    assert redact("Thank You Andy!", ["and"]) == "Thank You Andy!"

def test_redact_words_at_start_and_end(): 
    assert redact("dog bites dog", ["dog"]) == "### bites ###"

def test_redact_with_repeat_separators(): 
    assert redact("fox,,  fox", ["fox"]) == "###,,  ###"

def test_redact_empty_string(): 
    assert redact("", ["fox"]) == ""

def test_empty_banned_list(): 
    assert redact("fox", []) == "fox"

def test_num_and_line_breaks(): 
    assert redact("fox 123\nfox", ["fox"]) == "### 123\n###"