def is_left_side(sx, sy) -> bool:
    return ((sx % 2 == 1) and (sy % 2 == 0)) or ((sx % 2 == 0) and (sy % 2 == 1))


def main():
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    print(f"({sx}, {sy}) : {is_left_side(sx, sy)}")
    print(f"({tx}, {ty}) : {is_left_side(tx, ty)}")
    print(max(abs(sx - tx), abs(sy - ty)))
    return


if __name__ == "__main__":
    main()
