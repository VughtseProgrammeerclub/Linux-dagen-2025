import time
import sys
width = 30
for i in range(width + 1):
    filled = "#" * i
    empty = "." * (width - i)
    sys.stdout.write("\r[" + filled + empty + "]")
    sys.stdout.flush()
    time.sleep(0.1)
print("\nKlaar!")