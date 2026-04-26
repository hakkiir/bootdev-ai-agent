from functions.write_file import write_file

def test_write_file():

    t1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    t2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    t3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    print(t1)
    print(t2)
    print(t3)

test_write_file()