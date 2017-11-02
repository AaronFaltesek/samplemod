# from radioScrape import StateCheck
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='radioScrape.log',
                    filemode='w',
                    format='%(asctime)s : %(name)s :'
                    )


if __name__ == '__main__':
    print("Was up")
