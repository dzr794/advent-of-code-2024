import os
import pdb
import re


input_file = os.path.join("./inputs/input_day_3.txt")


def get_input():
    with open(input_file, "r") as file:
        content = file.read()
        return content

input = get_input()

regex_part1 = r"(?:mul[\(]{1}([0-9]{1,3}),{1}([0-9]{1,3})[\)]{1})"
regex_part2 = r"(?P<mul>mul\({1}([0-9]{1,3}),{1}([0-9]{1,3})\){1})|(?P<do>do\(\))|(?P<dont>don't\(\))"

matches_part1 = re.finditer(regex_part1, input, re.MULTILINE)
matches_part2 = re.finditer(regex_part2, input, re.MULTILINE)

total = 0
add_mult = True
for matchNum, match in enumerate(matches_part2, start=1):
    actual_match = match.group()

    if actual_match == "do()":
      add_mult = True
      print("\ndo()")
    elif actual_match == "don't()":
        add_mult = False
        print("\ndon't()")
    else:
        print(f"\tmul_match: {actual_match} / add_mult: {add_mult}")
        if add_mult:
            total += int(match.groups()[1]) * int(match.groups()[2])

print(f"\t\ttotal: {total}")

# do\(\).*?(?:mul[\(]{1}([0-9]{1,3}),{1}([0-9]{1,3})[\)]{1})+