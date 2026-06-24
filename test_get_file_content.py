from functions.get_file_content import get_file_content

def test_message(file_content: str) -> None:
    print('------------------------------------')
    print('------------------------------------')
    print('Printing file content')
    print(file_content)
    print('------------------------------------')
    print(f"Text length: {len(file_content)}")
    print(f"Truncated?: {'truncated' in file_content}")

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

first = get_file_content("calculator", "main.py")
second = get_file_content("calculator", "pkg/calculator.py")
third = get_file_content("calculator", "/bin/cat") 
fourth = get_file_content("calculator", "pkg/does_not_exist.py") 

test_message(first)
test_message(second)
test_message(third)
test_message(fourth)