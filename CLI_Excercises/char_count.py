import sys

if len(sys.argv[1]) < 2:
    print(f"Use like this: python char_count.py <tekst>")


print(f"Length is {len(sys.argv[1])} characters")