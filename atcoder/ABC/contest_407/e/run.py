import os
import time


def get_files():
    files = []
    for root, dirs, filenames in os.walk('./tests'):
        for filename in filenames:
            if filename.endswith('.txt'):
                files.append(os.path.join(root, filename))
    return files

if __name__ == '__main__':
    files = get_files()
    total_time = 0
    for file in files:
        print(f'Running test: {file}')
        start_time = time.time()
        os.system(f'cat {file} | python main.py')
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time
        print(f'Execution time: {execution_time:.3f} seconds')
        print('-----------------------------------')
        print()
    
    print(f'Total execution time: {total_time:.3f} seconds')
    print(f'Average execution time: {total_time/len(files):.3f} seconds')