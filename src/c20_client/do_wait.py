import time

# WAITING_TIME_FOR_EACH_CALL = (60 mins * 60 seconds)/1000 = 3.6
# 0.06s additional time for buffering

WAITING_TIME_FOR_EACH_CALL = 3.66


def get_wait_time():
    sleep_time = WAITING_TIME_FOR_EACH_CALL
    return sleep_time


def wait():
    time.sleep(get_wait_time())


def wait_between_jobs():
    get_wait_time()
    wait()
