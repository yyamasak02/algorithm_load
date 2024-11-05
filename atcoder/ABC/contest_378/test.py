import sys
import os
import re
import subprocess
import time
import difflib
import json


check_mark: str = "\u2705"
failed_mark: str = "\u274C"

def check_existence(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Error: file {file_path} does not exist.")
        return False
    return True

def get_case_numbers(file_path: str) -> list:
    files: list = os.listdir(file_path)
    pattern: any = r"case(\d+)\.txt"
    case_files: list = []

    for file in files:
        match = re.match(pattern, file)
        if match:
            number = match.group(1)
            case_files.append(number)
    return case_files

def cal_diff(expected: str, actual: str) -> str:
    difer: str = ""
    diff = difflib.unified_diff(
        expected.splitlines(), actual.splitlines(), lineterm='', fromfile='expected', tofile='actual'
    )
    for line in diff:
        difer += line
        difer += "\n"
    return difer

def	check_result(case_path: str, expected_path: str, script_path: str, case_numbers: list) -> dict:
	result_log: dict = {}
	ans: str = ""
	is_all_passed: bool = True
	for number in case_numbers:
		result_log[number] = None
		infile_name: str = f"{case_path}/case{number}.txt"
		expect_name: str = f"{expected_path}/expect{number}.txt"
		try:
			with open(infile_name, 'r') as input_file:
				input_data = input_file.read()
			start_time: time = time.perf_counter()
			result = subprocess.run(['python3', f"{script_path}"], input=input_data, text=True, capture_output=True)
			actual_output: str = result.stdout.strip()
			end_time: time = time.perf_counter()
			execution_time: time = end_time - start_time
			if os.path.exists(expect_name):
				with open(expect_name, 'r') as expected_file:
					expected_output = expected_file.read()
				if actual_output == expected_output:
					ans = f"Test case {number}: PASSED: {check_mark}, time: {execution_time:.6f} seconds"
				else:
					ans = f"Test case {number}: FAILED: {failed_mark}, time: {execution_time:.6f} seconds" + "\n" + "expected: \n"+ expected_output + "\n" + "actual: \n" + actual_output
					is_all_passed = False
			else:
				ans = f"Test case {number}: Expected output not found. Output: {actual_output} time: {execution_time:.6f} seconds"
		except Exception as e:
			ans = f"testing failed: {e}"
		finally:
			print(ans)
			result_log[number] = ans
	if is_all_passed:
		print("All cases passed!! Congratulations.")
	return result_log


def run_test(test_case: str) -> any:
	try:
		case_path: str = f"case/{test_case}"
		expected_path: str = f"expect/{test_case}"
		script_name = f"problem/{test_case}.py"
		if not check_existence(case_path) or not check_existence(expected_path) or not check_existence(script_name):
			return False
		case_numbers: list = get_case_numbers(case_path)
		case_numbers.sort()
		result_log: dict = check_result(case_path=case_path, expected_path=expected_path, script_path=script_name, case_numbers=case_numbers)
		with open(f"result_{test_case}.json", 'w', encoding='utf-8') as json_file:
			json.dump(result_log, json_file, ensure_ascii=False, indent=4)
	except Exception as e:
		print(f"Error ocuured: {e}")


def main():
    # when missing parameter
    if len(sys.argv) != 2:
        print("Usage: python3 test_script.py [a|b|c|d|e|f|g]")
        return
    
    test_case = sys.argv[1]
    # when wrong parameter
    if test_case not in 'abcdefg':
        print("Error: Test case must be one of 'a' to 'g'.")
        return
    
    # run test
    run_test(test_case)
    
if __name__ == "__main__":
    main()
