# let's debug this code!!
# it's broken btw
#andy was here

if __name__ == '__main__':
    # we need some hackers!
    hackcu_list = ['a', 'b', 'c', 'd', 'e', 'f', 'z',
                    'm', 'A', 'r']
    another_list = [0] * 26
    for ind, val in enumerate(hackcu_list):
        another_list[ord(val)-97] = 0