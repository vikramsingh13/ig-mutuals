#!/usr/bin/env python3
import re

# files: followers.txt, following.txt
# Extract names from: alt="<profile_name>'s profile picture"

pattern = re.compile(r'alt="([^"]+?)\'s profile picture"')

def extract_names(path):
    # using sets for faster comparison later on
    names = set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for m in pattern.finditer(line):
                names.add(m.group(1))
    return names

def create_a_not_in_b_list(a, b):
    """a is set of following. b is set of followers. return list of followings not in followers"""
    return [name for name in a if name not in b]

followers = extract_names("followers.txt")
following = extract_names("following.txt")

non_mutuals = create_a_not_in_b_list(following, followers)

# Example usage:
print(f"followers: {len(followers)}")
print(f"following: {len(following)}")
# print(followers)
# print(following)

print(f"Non-mutuals: {non_mutuals}")


