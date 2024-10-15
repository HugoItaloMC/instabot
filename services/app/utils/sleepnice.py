import random
import time


def delay(frequency: str = 'low'):
    frequency.lower()
    # frequency : ['low', 'nice', 'high']
    if frequency:
        if frequency == 'low':
            time.sleep(random.randint(4, 7))
        elif frequency == 'nice':
            time.sleep(random.randint(8, 12))
        elif frequency == 'high':
            time.sleep(random.randint(14, 21))
        else:
            time.sleep(random.randint(7, 12))