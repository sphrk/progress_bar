from time import sleep
import colorama

def progress(g, color=colorama.Fore.YELLOW):
    '''
        g : python generator
    '''
    total = len(g)

    def print_bar(percent, i, total, color=color):
        CHAR = '\u2588' # '█'
        percent_int = int(percent)
        bar = CHAR * percent_int + '-' * (100 - percent_int)
        
        i += 1
        # if i == total:
        #     color = colorama.Fore.GREEN
        # print(color + f"|{bar}| {percent:0.2f}% | ( {i}/{total} )", end='\r')
        
        # without color
        print(f"\r|{bar}| {percent:0.2f}% | ({i}/{total})", end='\r')
        

    print_bar(0, 0, total)    
    for i, value in enumerate(g):
        percent = 100 * ((i + 1) / total)
        print_bar(percent, i, total)
        # print('#', i, value, percent)
        yield value

if __name__ == '__main__':
    for i in progress(range(10)):
        sleep(.1)
