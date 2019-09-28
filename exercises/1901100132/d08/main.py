from mymodule import stats_word
import traceback
import logging

logger = logging.getLogger(__name__)

def test_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test_traceback =>', e)
        print(traceback.format_exc())

def text_logger():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        #print('test_logger =>', e)
        logger.exception(e)

if __name__ == "__main__":
    test_traceback()
    text_logger()
    