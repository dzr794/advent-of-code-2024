import os

input_file = os.path.join("./inputs/input_day_1.txt")

def get_lists():
  list_1 = []
  list_2 = []

  with open(input_file, 'r') as file:
      lines = file.readlines()
      for i in range(len(lines)):
          line = lines[i]
          col1, col2 = line.split("   ")
          list_1.append( int(col1.replace("\n", "")) )
          
          list_2.append( int(col2.replace("\n", "")) )
  
  return list_1, list_2

def solve_part_1():
    list_1, list_2 = get_lists()

    sorted_1 = sorted(list_1)
    sorted_2 = sorted(list_2)

    dif_list = []

    for i in range(len(sorted_1)):
        dif_list.append( abs(sorted_1[i] - sorted_2[i]) )

    result = sum(dif_list)

    return result

print(solve_part_1())

def solve_part_2():
    list_1, list_2 = get_lists()

    simils = []

    for i in range(len(list_1)):
      actual = list_1[i]
      times_apear = list_2.count(actual)

      simils.append( actual * times_apear )

    result = sum(simils)
    return result

print(solve_part_2())


        


    
    