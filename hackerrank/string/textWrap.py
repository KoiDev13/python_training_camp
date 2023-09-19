import textwrap

def wrap(string:str, max_width:int)->list:
    """This function is used for wraping text."""
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.fill(text=string)
    return word_list

if __name__ == '__main__':
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)