import argparse
import os
import shutil
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    args = parser.parse_args()

    contest = f"contest_{args.target}"
    base = os.path.join("..", contest)
    template = "../contest_template"

    if not os.path.isdir(base):
        print(f"[ERROR] not found: {base}")
        return

    for prob in sorted(os.listdir(base)):
        prob_dir = os.path.join(base, prob)
        if not os.path.isdir(prob_dir) or not re.match(r"^[a-z]$", prob):
            continue

        old_dir = os.path.join(prob_dir, "old")
        os.makedirs(old_dir, exist_ok=True)

        nums = [int(d) for d in os.listdir(old_dir) if d.isdigit()]
        n = max(nums) + 1 if nums else 1
        dst_old = os.path.join(old_dir, str(n))
        os.makedirs(dst_old)

        for f in os.listdir(prob_dir):
            if re.match(r"^(Main|main)\.", f):
                shutil.move(
                    os.path.join(prob_dir, f),
                    os.path.join(dst_old, f),
                )

        tpl_dir = os.path.join(template, prob)
        if os.path.isdir(tpl_dir):
            for f in os.listdir(tpl_dir):
                if re.match(r"^(Main|main)\.", f):
                    shutil.copy(
                        os.path.join(tpl_dir, f),
                        os.path.join(prob_dir, f),
                    )


if __name__ == "__main__":
    main()
