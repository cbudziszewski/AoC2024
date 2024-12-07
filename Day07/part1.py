#!/usr/bin/env python3
calibrations = list()
targets = list()
with open('input.txt') as file:
    for line in file:
        k, v = line.rstrip().split(":")
        targets.append(k)
        calibrations.append(list(map(int,v.split())))
        print(targets)
        print(calibrations)

operators = list()
operators.append(lambda a, b: a*b)
operators.append(lambda a, b: a+b)

print('########')

def is_calibration_correct(target, running, remaining):
    if len(remaining) == 1:
        result = [op(running, remaining[0]) for op in operators]
        print(f"result: {[int(r) == int(target) for r in result]}")
        return any([r == target for r in result])
    else:
        return any([ is_calibration_correct(target, op(running, remaining[0]), remaining[1:]) for op in operators ])

## liste umkehren und rekursiv bearbeiten
## das liest sich aber wie ein endrekursives problem

# Zero can be returned by any wrong calc
total_calibration_result = 0
for i, v in enumerate(calibrations):
    print(f"cal {i}: {v} tgt {targets[i]}")
    correct = is_calibration_correct(int(targets[i]), v[0], v[1:])
    total_calibration_result = total_calibration_result + int(targets[i]) if correct else total_calibration_result
    print(f"total: {total_calibration_result}")

print(f"total: {total_calibration_result}")




