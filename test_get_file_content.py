from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_get_file_content():
   
    t1 = get_file_content("calculator", "lorem.txt")
    print(len(t1))
    print(t1[MAX_CHARS:])

    t2 = get_file_content("calculator", "main.py")
    print(t2)

    t3 = get_file_content("calculator", "pkg/calculator.py")
    print(t3)

    t4 = get_file_content("calculator", "/bin/cat") #(this should return an error string)
    print(t4)

    t5 = get_file_content("calculator", "pkg/does_not_exist.py") #(this should return an error string)
    print(t5)

test_get_file_content()