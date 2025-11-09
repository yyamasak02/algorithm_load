import os
import argparse
import time
import sys
import yaml
import subprocess


def init_config(path: str = "config.yml") -> dict:
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return {
        "default_folders": config.get("default_folders", []),
        "timeout": config.get("timeout", 3),
    }


def get_files(folder: str) -> list[str]:
    files = []
    for root, _, filenames in os.walk(f"{folder}/tests"):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(root, filename))
    return sorted(files)


def run_tests(files: list[str], folder: str, timeout: int, language: str) -> None:
    for file in files:
        print(f"Running test: {file}")
        d: dict[str, str] = {
            "python": f"python {folder}/main.py",
            "java": f"java {folder}/Main.java",
            "rust": f"rustc {folder}/main.rs -o {folder}/rust_main; {folder}/rust_main",
        }
        try:
            with open(file, "r") as f:
                old_stdin = sys.stdin
                sys.stdin = f
                output = None
                try:
                    start = time.perf_counter()
                    subprocess.run(
                        d[language], stdin=sys.stdin, stdout=output, shell=True
                    )
                finally:
                    sys.stdin = old_stdin
            if output is None:
                output = ""
            end = time.perf_counter()
            print(output)
            print(f"Execution time: {(end - start) * 1000:.2f} ms")
        except Exception as e:
            print(f"Error running test: {e}")
        print("-----------------------------------\n")


def main():
    config = init_config()
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pro", type=str, default="python")
    parser.add_argument("-d", "--dir", type=str, default=None)
    args = parser.parse_args()
    if args.pro not in ["python", "java", "rust"]:
        print(f"[ERROR] not support {args.pro}")
        return
    if args.dir is None or not os.path.exists(args.dir):
        print(f"[INFO] running default folders: {config['default_folders']}")
        folders = config["default_folders"]
    else:
        folders = [args.dir]
    for folder in folders:
        files = get_files(folder=folder)
        print(f"[INFO] Running {folder} Problems")
        run_tests(
            files=files, folder=folder, timeout=config["timeout"], language=args.pro
        )


if __name__ == "__main__":
    main()
