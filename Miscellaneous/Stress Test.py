import random

def generate():
    "generate random test case here"

passed = 0
while passed <= 1000:
    test_case = generate()
    with open('input.txt', mode='w') as f:
        print(test_case, file=f)
    p1 = subprocess.run(
        'python brute.py < input.txt',
        check=True, shell=True, capture_output=True, text=True
    )
    p2 = subprocess.run(
        'solve.exe < input.txt',
        check=True, shell=True, capture_output=True, text=True
    )
    if p1.stdout != p2.stdout:
        print('Failed!')
        print('Expected:', p1.stdout)
        print('Output:', p2.stdout)  
        print("Test Case:\n" + test_case)
        break

    passed += 1
    print(f'{passed} cases passed')
