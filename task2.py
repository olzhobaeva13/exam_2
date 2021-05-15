#задание 2
file_ = open('exam_2.txt', 'r') 
text = file_.read()

def count_s_and_t():
    lst_of_letters = list(text)
    count_s = 0
    count_t = 0
    for i in lst_of_letters:
        if i=='s':
            count_s += 1
        elif i=='t':
            count_t += 1
    print(f's - {count_s}, t - {count_t}')
count_s_and_t()
