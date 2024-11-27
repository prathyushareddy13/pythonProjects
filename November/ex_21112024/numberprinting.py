
def num_print():
    result_str = ""
    rev_str=""
    for i in range(1,5):
        result_str += str(i)
        #print(result_str)
        for j in range(i, -1):
            rev_str += str(j)
        #print(space+reverse_string)
        #rev_str = result_str[:: -1]
        print(rev_str)

num_print()
