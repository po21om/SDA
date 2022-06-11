test_slow = {"a":1, "b":2, "c":3}
print(test_slow["a"])
print(test_slow.get("a"))

print(test_slow.get("d"))
print(test_slow.get("d", 4))
print(test_slow)