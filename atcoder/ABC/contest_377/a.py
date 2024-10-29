# https://atcoder.jp/contests/abc377/tasks/abc377_a

alpha = input()
count_dict = {'A': 0, 'B': 0, 'C': 0}
if alpha[0] in count_dict:
    count_dict[alpha[0]] += 1
if alpha[1] in count_dict:
    count_dict[alpha[1]] += 1
if alpha[2] in count_dict:
    count_dict[alpha[2]] += 1
if count_dict['A']== 1 and count_dict['B']== 1 and count_dict['C']== 1:
	print("Yes")
else:
    print("No")