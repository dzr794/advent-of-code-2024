import os
import pdb

input_file = os.path.join("./inputs/input_day_2.txt")

not_safe_reports = []

def get_reports():
    reports = []
    safe_reports = 0
    with open(input_file, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = [ int(x.replace("\n", "")) for x in  lines[i].split(" ")]
            
            # col1, col2 = line.split("   ")
            reports.append(line)

    return reports

def exclude_index(lst, index):
    return [x for i, x in enumerate(lst) if i != index]

def isSafe(line):
    goodValuesNegative = [-1, -2, -3]
    goodValuesPositive = [1, 2, 3]
    usedValues = None

    for i in range(len(line) - 1):
        dif = line[i] - line[i + 1]
        
        if dif == 0 or abs(dif) > 3:
            # print(f"\t\tWarn: {dif} invalid value")
            # print("\t\tNOT SAFE")
            return False
        
        if usedValues is None:
            if dif < 0:
                usedValues = goodValuesNegative
            else:
                usedValues = goodValuesPositive
        # print(f"\tusedValue: {usedValues}")
        # print(f"\t{line[i]} - {line[i + 1]} dif: {dif}")
        if dif not in usedValues:
            # print(f"\t\tWarn: {dif} not in {usedValues}")
            # print("\t\tNOT SAFE")
            return False
    
    # print("\t\tIS SAFE")
    return True

def isSafeDampener(line):
    goodValuesNegative = [-1, -2, -3]
    goodValuesPositive = [1, 2, 3]
    usedValues = None
    errorCount = 0
    
    remove_index = None

    for i in range(len(line) - 1):
        dif = line[i] - line[i + 1]

        # if dif == 0 or abs(dif) > 3:
        #     print(f"\t\tError: {dif} invalid value")
        #     print("\t\tNOT SAFE")
        #     return False

        if usedValues is None:
            if dif < 0:
                usedValues = goodValuesNegative
            else:
                usedValues = goodValuesPositive

        print(f"\t{line[i]} - {line[i + 1]} dif: {dif} // usedValue: {usedValues}")
        if dif not in usedValues and errorCount == 0 and remove_index is None:
            print(f"\t\tWarn: {dif} not in {usedValues}")
            
            # test if can test with next index
            print(f"i+2: {i+2} < len(line)-1: {len(line)-1}")
            if i+2 < len(line)-1:
                print(f"line[i]: {line[i]} - line[i+2]: {line[i + 2]}")
                dif = line[i] - line[i + 2]
                if dif not in usedValues:
                    remove_index = i
                else:
                    remove_index = int(i + 1)      
            else:
              remove_index = int(i+1)
            
            print(f"\t\tREMOVING index {remove_index} ({line[remove_index]})")
            errorCount += 1


    print(f"\t\tWarns: {errorCount}")
    if remove_index is None:
        print("\t\tIS SAFE")
        return True
    
    line_with_excluded = exclude_index(line, remove_index)
    # del line[remove_index]

    print(f"\t\t\t NEW LINE: {line_with_excluded}")
    # if second try is needed
    for i in range(len(line_with_excluded) - 1):
        dif = line_with_excluded[i] - line_with_excluded[i + 1]

        if dif == 0 or abs(dif) > 3:
            print(f"\t\t\t\tError: {dif} invalid value")
            print("\t\t\t\tNOT SAFE")
            return False

        print(f"\t\t\t{line_with_excluded[i]} - {line_with_excluded[i + 1]} dif: {dif} // usedValue: {usedValues}")
        if dif not in usedValues:
            print("\t\t\t\tNOT SAFE")
            return False

    print("\t\t\t\tIS SAFE")
    return True


reports = get_reports()

safe_reports = 0
for index,report in enumerate(reports):
    print(f"ACTUAL INDEX: {index}")
    print(f"{report}")
    isSafeLine = isSafeDampener(report)
    if isSafeLine:
        safe_reports += 1
    else:
        not_safe_reports.append(report)
    
    # pdb.set_trace()
    print(f"{report} is safe: {isSafeLine} / safe reports: {safe_reports}\n")

print(f"Safe reports: {safe_reports}")
print(f"NOT Safe reports: \n{not_safe_reports}")