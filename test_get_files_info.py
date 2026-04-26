from functions.get_files_info import get_files_info

def test_get_files_info():
    
    t1 = get_files_info("calculator", ".")
    print(t1)

    t2 = get_files_info("calculator", "pkg")
    print(t2)

    t3 = get_files_info("calculator", "/bin")
    print(t3)

    t4 = get_files_info("calculator", "../")
    print(t4)


test_get_files_info()