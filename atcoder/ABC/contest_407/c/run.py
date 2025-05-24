import os


def get_files():
    files = []
    for root, dirs, filenames in os.walk('./tests'):
        for filename in filenames:
            if filename.endswith('.txt'):
                files.append(os.path.join(root, filename))
    return files

if __name__ == '__main__':
    files = get_files()
    for file in files:
        # call python main.py with the file as argument
        print(f'Running test: {file}')
        os.system(f'cat {file} | python3 main.py')
        print('-----------------------------------')
        print()