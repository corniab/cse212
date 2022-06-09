def do_somthing_5_times(callback_function, i=0):
    if i < 5:
        callback_function()
        do_somthing_5_times(callback_function, i+1)

def print_ben():
    print("ben")

do_somthing_5_times(print_ben)
