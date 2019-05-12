import logging
import time

# Create Logger
logging.basicConfig(filename=r'/Users/xxxxxxxxxxxxx/PracticeLogger.csv', level=logging.DEBUG)
logger = logging.getLogger()


def read_file(path):
    """Returns the content of the file at 'path' and measure the time required"""
    start_time = time.time()
    try:
        f = open(path, mode="r")
        data = f.read()
        return data
    except FileNotFoundError as e:
        logger.error(e)
        raise
    except Exception as e:
        logger.error(e)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        time_taken = stop_time-start_time
        logger.info("Time required for {file} reading is {time}".format(file=path, time=time_taken))


data = read_file(r"/xxxxxxxxxxx/xxxxxxx.csv")
print(data)
