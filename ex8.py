# -- coding: utf-8 --

formatter = "%s %s %r %r"

print formatter % ("叮噹", "大雄", "技安", "小夫")
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)
