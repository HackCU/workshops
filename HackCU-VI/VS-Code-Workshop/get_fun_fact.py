
def get_fun_fact(input_str):
    file1 = open('fun_fact.txt', 'r')
    s = file1.read()
    try:
        num = int(input_str)
        if int('{}{}'.format(s[num-28], 
                                s[num-21])) == num:
            # haha... correct number.
            w1 = s[num-39]
            w2 = '{}{}'.format(s[num-32], s[num-19])
            w3 = '{}{}{}{}'.format(s[num-9], s[num-8], s[num-5], s[num-4])
            w4 = s[num+3]
            l  = [[39], [32,19], [9,8,5,4], [-3,-6,-8,-10,-15,-23]]
            for val in l:
                word = ''
                for i in val:
                    word+=s[num-i]
                print(word, end= ' ')
            print()
    except:
        raise Exception('Error! Not a number!')


if __name__ == '__main__':
    get_fun_fact('<your-number here>')