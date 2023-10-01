targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)

while shoot != "End":
    shoot = int(shoot)
    if 0 <= shoot < targets_len:
      target = targets[shoot]
      targets[shoot] = -1

      for element in range(targets_len):
          if targets[element] == -1:
              continue
          if targets[element] > target:
              targets[element] -= target
          else:
              targets[element] += target

    shoot = input()
count_targets = targets.count(-1)


print(f"Shot targets: {count_targets} ->", *targets)



