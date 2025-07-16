import os
import subprocess
import argparse
import time

def get_files():
    files = []
    for root, dirs, filenames in os.walk('./tests'):
        for filename in filenames:
            if filename.endswith('.txt'):
                files.append(os.path.join(root, filename))
    files.sort()
    return files

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--skip", type=bool, default=False)
    mode = parser.parse_args().skip
    files = get_files()

    for file in files:
        print(f'Running test: {file}')
        try:
            with open(file, 'r') as f:
                start = time.perf_counter()
                result = subprocess.run(
                    ['python', 'main.py'],
                    stdin=f,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                end = time.perf_counter()
                elapsed_ms = (end - start) * 1000
            print(result.stdout)
            print(f'Execution time: {elapsed_ms:.2f} ms')
            if result.stderr:
                print('[stderr]')
                print(result.stderr)
        except subprocess.TimeoutExpired:
            print('Error: Execution timed out')
        except Exception as e:
            print(f'Error running test: {e}')
        print('-----------------------------------\n')

if __name__ == '__main__':
    main()
