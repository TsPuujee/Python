
def reverse(s):
    if len(s) <= 1:
        return s[0]
    else:
        return reverse(s[1:]) + s[0]

print(reverse("Сайн уу?"))