if __name__ == "__main__":
    n,q = map(int, input().split())
    box_to_label = list(range(n))
    label_to_box = list(range(n))
    pigeon_to_box = list(range(n))
    for _ in range(q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            op[1] -= 1
            op[2] -= 1
            pigeon_to_box[op[1]] = label_to_box[op[2]]
        if op[0] == 2:
            op[1] -= 1
            op[2] -= 1
            tmp = label_to_box[op[1]]
            label_to_box[op[1]] = label_to_box[op[2]]
            label_to_box[op[2]] = tmp
            tmp = box_to_label[label_to_box[op[1]]]
            box_to_label[label_to_box[op[1]]] = box_to_label[label_to_box[op[2]]]
            box_to_label[label_to_box[op[2]]] = tmp
        if op[0] == 3:
            op[1] -= 1
            print(box_to_label[pigeon_to_box[op[1]]] + 1)