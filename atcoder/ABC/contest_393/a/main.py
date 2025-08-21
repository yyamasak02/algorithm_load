s1, s2 = input().split()

s1_bool = True if s1 == "sick" else False
s2_bool = True if s2 == "sick" else False

if s1_bool == s2_bool:
    if s1_bool is True:
        print(1)
    else:
        print(4)
else:
    if s1_bool is True:
        print(2)
    else:
        print(3)
