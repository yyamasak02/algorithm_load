import os
import subprocess
import argparse
import time


def get_files(folder: str) -> list:
    files = []
    for root, dirs, filenames in os.walk(f"{folder}/tests"):
        for filename in filenames:
            if filename.endswith(".txt"):
                files.append(os.path.join(root, filename))
    files.sort()
    return files


def run_tests(files: list, folder: str) -> None:
    for file in files:
        print(f"Running test: {file}")
        try:
            with open(file, "r") as f:
                start = time.perf_counter()
                result = subprocess.run(
                    ["python", f"{folder}/main.py"],
                    stdin=f,
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                end = time.perf_counter()
                elapsed_ms = (end - start) * 1000
            print(result.stdout)
            print(f"Execution time: {elapsed_ms:.2f} ms")
            if result.stderr:
                print("[stderr]")
                print(result.stderr)
        except subprocess.TimeoutExpired:
            print("Error: Execution timed out")
        except Exception as e:
            print(f"Error running test: {e}")
        print("-----------------------------------\n")


def main():
    DEFAULT_FOLDERS = ["a", "b", "c", "d", "e", "f"]
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, default=None)
    args = parser.parse_args()

    folders: list = None
    if args.dir is None or not os.path.exists(args.dir):
        print(f"[INFO] running default folders: {DEFAULT_FOLDERS}")
        folders = DEFAULT_FOLDERS
    else:
        folders = [args.dir]

    for folder in folders:
        files = get_files(folder=folder)
        print(f"[INFO] Running {folder} Problems")
        run_tests(files=files, folder=folder)


if __name__ == "__main__":
    main()
