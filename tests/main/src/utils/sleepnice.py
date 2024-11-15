import random
import time
__all__ = ['delay']

def delay(frequency: str = ''):
    frequency.lower()
    # frequency : ['low', 'nice', 'high']
    if frequency:
        timein: int = 0
        if frequency == 'low':
            timein = time.sleep(random.randint(6, 11))
        elif frequency == 'nice':
            timein = time.sleep(random.randint(9, 14))
        elif frequency == 'high':
            timein = time.sleep(random.randint(12, 17))
        else:
            timein = time.sleep(random.randint(2, 4))
        return timein