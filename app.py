#!/usr/bin/env python3
import re

# files: followers.txt, following.txt
# Extract names from: alt="<profile_name>'s profile picture"

pattern = re.compile(r'alt="([^"]+?)\'s profile picture"')

def extract_names(path):
    names = set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for m in pattern.finditer(line):
                names.add(m.group(1))
    return names

followers = extract_names("followers.txt")
following = extract_names("following.txt")

# Example usage:
print(f"followers: {len(followers)}")
print(f"following: {len(following)}")
# print(followers)
# print(following)
