import os
import pdb
import re

input_file = os.path.join("./inputs/input_day_4.txt")
# input_file = os.path.join("./inputs/mini_input_day_4.txt")


def get_input():
    input = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = [x.replace("\n", "") for x in lines[i]]
            if line[-1] == "":
                del line[-1]
            input.append(line)

    return input

def add_xmas(found:str):
    global total_xmas
    if found.lower() == 'xmas':
        total_xmas += 1


def search_xmas_right(input,x,y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if x + 3 >= len(input[y]):
        print("search LEFT: invalid, skipping")
        return
    
    search = input[y][x] + input[y][x + 1] + input[y][x + 2] + input[y][x+3]
    print(f"search LEFT: {search}")
    add_xmas(search)

def search_xmas_left(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if x - 3 < 0:
        print("search RIGHT: invalid, skipping")
        return

    search = input[y][x] + input[y][x - 1] + input[y][x - 2] + input[y][x - 3]
    print(f"search RIGHT: {search}")
    add_xmas(search)

def search_xmas_up(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if y - 3 < 0:
        print("search UP: invalid, skipping")
        return

    search = input[y][x] + input[y - 1][x] + input[y - 2][x] + input[y - 3][x]
    print(f"search UP: {search}")
    add_xmas(search)

def search_xmas_down(input, x, y):
    print(f"input[{x}][{y}]: {input[y][x]}")
    print(f"len(input): {len(input)}")
    if y + 3 >= len(input):
        print("search DOWN: invalid, skipping")
        return

    search = input[y][x] + input[y + 1][x] + input[y + 2][x] + input[y + 3][x]
    print(f"search DOWN: {search}")
    add_xmas(search)

def search_xmas_diag_up_left(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if (y - 3 < 0) or (x - 3 < 0):
        print("search UP_LEFT: invalid, skipping")
        return

    search = input[y][x] + input[y - 1][x - 1] + input[y - 2][x - 2] + input[y - 3][x - 3]
    print(f"search UP_LEFT: {search}")
    add_xmas(search)

def search_xmas_diag_up_right(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if (y - 3 < 0) or (x + 3 >= len(input[y])):
        print("search UP_RIGHT: invalid, skipping")
        return

    search = input[y][x] + input[y - 1][x + 1] + input[y - 2][x + 2] + input[y - 3][x + 3]
    print(f"search UP_RIGHT: {search}")
    add_xmas(search)

def search_xmas_diag_down_left(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if (y + 3 >= len(input)) or (x - 3 < 0):
        print("search DOWN_LEFT: invalid, skipping")
        return

    search = input[y][x] + input[y + 1][x - 1] + input[y + 2][x - 2] + input[y + 3][x - 3]
    print(f"search DOWN_LEFT: {search}")
    add_xmas(search)


def search_xmas_diag_down_right(input, x, y):
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if (y + 3 >= len(input)) or (x + 3 >= len(input[y])):
        print("search DOWN_RIGHT: invalid, skipping")
        return

    search = input[y][x] + input[y + 1][x + 1] + input[y + 2][x + 2] + input[y + 3][x + 3]
    
    print(f"search DOWN_RIGHT: {search}")
    add_xmas(search)

def search_2x_diag_mas(input, x, y):
    global total_xmas
    # print(f"input[{x}][{y}]: {input[y][x]}")
    if (y + 1 >= len(input)) or (y - 1 < 0) or (x + 1 >= len(input[y])) or (x - 1 < 0):
        # print("search X-mas: invalid, skipping")
        return

    diag_1 = input[y - 1][x - 1] + input[y][x] + input[y + 1][x + 1]
    diag_2 = input[y + 1][x - 1] + input[y][x] + input[y - 1][x + 1]
    

    # print(f"search X-mas: {diag_1} , {diag_2}")
    if (
        (diag_1.lower() == "mas" or diag_1.lower() == "sam")
        and (diag_2.lower() == "mas" or diag_2.lower() == "sam")
    ):
        # print(f"x-mas at: {y},{x}")
        total_xmas += 1

total_xmas = 0
input = get_input()

print(f"input size: {len(input[0])} x {len(input)}")

def find_xmas():
  for y, line in enumerate(input):
      print(f"line: {line}")
      for x, char in enumerate(line):
        

        search_xmas_left(input, x, y)
        search_xmas_right(input, x, y)
        search_xmas_up(input, x, y)
        search_xmas_down(input, x, y)
        search_xmas_diag_up_left(input, x, y)
        search_xmas_diag_up_right(input, x, y)
        search_xmas_diag_down_left(input, x, y)
        search_xmas_diag_down_right(input, x, y)
      
def find_2xmas():
    for y, line in enumerate(input):
        # print(f"line: {line}")
        for x, char in enumerate(line):
            search_2x_diag_mas(input, x, y)
            # pdb.set_trace()

find_2xmas()
print(f"total_xmas: {total_xmas}")