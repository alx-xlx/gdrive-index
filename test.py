from time import sleep
from IPython.display import clear_output, display

for f in range(10000):
    clear_output(wait=True)
    print(f)  # use display(f) if you encounter performance issues
    # sleep(1)