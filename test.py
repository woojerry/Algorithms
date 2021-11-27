# for k in range(3, len(arr)):
#     sub_list.append(list(itertools.combinations(arr, k)))

# for subs in sub_list:
#     for sub in subs:
#         print(sub)
#         changed = False
#         for i in range(len(sub)-1):
#             if not changed:
#                 if sub[i] > sub[i+1]:
#                     changed = True
#                     print(changed)
#             else:
#                 if sub[i] > sub[i+1]:
#                     print(i)
#                     if i == len(sub) - 1:
#                         answer += 1
#                 elif sub[i] <= sub[i+1]:
#                     break
# for k in range(3, len(arr)):
#     sub_list.append(list(itertools.combinations(arr, k)))

# for subs in sub_list:
#     for sub in subs:
#         print(sub)
#         changed = False
#         for i in range(len(sub)-1):
#             if not changed:
#                 if sub[i] > sub[i+1]:
#                     changed = True
#                     print(changed)
#             else:
#                 if sub[i] > sub[i+1]:
#                     print(i)
#                     if i == len(sub) - 1:
#                         answer += 1
#                 elif sub[i] <= sub[i+1]:
#                     break
