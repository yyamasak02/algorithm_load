n,m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
tonari_sa = []
for i in range(n-1):
    tonari_sa.append((i, x[i+1]-x[i]))
tonari_sa.sort(key=lambda x: x[1], reverse=True)
cut_points = []
for i in range(m-1):
    cut_points.append(tonari_sa[i][0])
cut_points.sort()
groups = []
start = 0
for cut in cut_points:
    groups.append(x[start:cut+1])
    start = cut + 1
groups.append(x[start:])
total_power = 0
for i, group in enumerate(groups):
    if len(group) == 1:
        power = 0
    else:
        station_pos = (group[0] + group[-1]) / 2
        power = int((group[-1] - station_pos)*2)
    total_power += power

print(total_power)