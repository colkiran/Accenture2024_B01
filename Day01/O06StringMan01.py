
st = "Hello World"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing - using their indexes
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:] :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
st = "malayalam"
print(f"Palindrome - {st}" if st == st[::-1] else f"Not a Palindrome - {st}")

print("-" * 60)
st = "hello"

# st is an object of string class
print(f"upper case :{st.upper()}")
print(f"title case :{st.title()}")
print(f"capitalize :{st.capitalize()}")

print("-" * 60)
# strings are immutable
st = "hello world"
print(f"st :{st}")
# st[0] = 'H'

print("-" * 60)
# index, count
st = "hello world"
print(f"st :{st}")

res = st.index('w')
print(f"res :{res}")

res = st.index("l")
print(f"res :{res}")

res = st.index("l", st.index("l") + 1)
print(f"res :{res}")

res = st.index("l", st.index("l", st.index('l') + 1) + 1)
print(f"res :{res}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.count("o")
print(f"res :{res}")
# how many times each character is repeating

from collections import Counter

res = Counter(st)
print(res)

