def reverse(text):
    reverse = ""
    for i in range(0, len(text)):
        reverse = reverse + text[len(text) - 1 - i]
    return reverse
