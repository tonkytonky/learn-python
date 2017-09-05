def compare_strings(string1, string2):
    if string1 == string2:
        return 1
    else:
        if len(string1) > len(string2):
            return 2
        elif string2 == 'learn':
            return 3
        else:
            return 'Непредусмотренный случай'
