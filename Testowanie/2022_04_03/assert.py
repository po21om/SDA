
x = "abcdefg"

def letter_in_text(text, letter):
    assert letter in text.lower()

letter_in_text(x, "d")
letter_in_text(x, "h")