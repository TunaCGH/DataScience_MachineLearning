from loguru import logger

def add(x, y):
    if __name__ == "__main__":
        logger.info("This module is being run directly")
    else:
        logger.info("This module is being imported")
    print(f"{x} + {y} = {x + y}")
    return x + y

def subtract(x, y):
    if __name__ == "__main__":
        logger.info("This module is being run directly")
    else:
        logger.info("This module is being imported")
    print(f"{x} - {y} = {x - y}")
    return x - y


_ = add(5, 3) # Assign to _ to avoid printing output in the console
# | INFO     | __main__:add:3 - This module is being run directly
# 5 + 3 = 8

_ = subtract(10, 4)
# | INFO     | __main__:subtract:3 - This module is being run directly
# 10 - 4 = 6