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
    """a is set of following. b is set of followers. return list of followings not in followers
    
    can be reused for a as non_mutuals, b as exceptions. return list of non_mutuals without the exceptions
    """
    return [name for name in a if name not in b]

# set of non-mutual exceptions who shouldn't be included in the non_mutuals set
non_mutuals_exceptions = ('codatoronto', 'rebels.shuffleacad', 'holypriest', 'levity.music', 'aadja', 'bardemto', 'khivamusic', 'followthefishtv', 'amelie_lens', 'johnsummit', 'airod_music', 'kinetic.to', 'dimension', 'alleykaydj', 'nicomoreno_music', 'mojie_music', 'shambhala_mf', 'vadimkhan', 'alesso', 'torontosymphony', 'zedsdead', 'todotoronto', 'excision', 'kamaruclothing', 'embryonevents', 'andyc_ramagram', 'rebelindustry', 'nomadtorontoofficial_', 'cerakhin', 'subtronics', 'outcastclothing', 'ihatemodels1', 'marshmello', 'blankemusic', 'djacslater', 'saralandrydj', 'veldmusicfestival', 'sammyvirji', 'emorfik', 'usamastandsup', 'd.n.r.productions', 'rebelzsyndicate', 'midnightrunnerstoronto', 'dtaalai', 'shufflerebellion', 'basswell', 'edc_thailand', 'picjerphoto', 'miscmondays', 'dirtmonkeymusic', 'zzzorza', 'carolina_callush', 'supermkttoronto', 'biia__________', 'arcaneghosts', 'zingaramusic', 'talesxoxo', 'spotted.toronto', 'electricislandto', 'dommazzetti', 'charlottedewittemusic', 'meduzamusic', 'ninaxbender', 'secreteventss', 'teedeejayyy', 'radiatetheworld', 'levels.ent', 'the.kimchi.club', 'chaseandstatus', 'paintedladyossington', 'contentday.ca', 'format.toronto', 'maup', 'svddendeath', 'besidethebookshelves', 'imomnom', 'secretsocietyto', 'torontohousecommunityy', 'bennybenassi', 'lastcallcocktailclub', 'sojourn_festival', 'barelyalive', 'alleycvt', 'officialrezz', 'lostlandsfestival')

followers = extract_names("followers.txt")
following = extract_names("following.txt")

non_mutuals = create_a_not_in_b_list(following, followers)

non_mutuals_without_exceptions = create_a_not_in_b_list(non_mutuals, non_mutuals_exceptions)

# Example usage:
print(f"followers: {len(followers)}")
print(f"following: {len(following)}")
# print(followers)
# print(following)

print(f"Non-mutuals: {non_mutuals}")


