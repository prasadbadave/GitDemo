import logging
def test_loggingDemo():
    fileHandler=logging.fileHandler('logfile.log')
    formater=logging.Formatter("%(asctime)s : %(leveltime)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formater)
    logger=logging.getLogger(__name__)
    logger.addHandler(fileHandler)
    logger.setLevel("logging.INFO")
    logger.debug("THis is debug statement")
    logger.info("THis is informaiton statement")
    logger.warning("This is warning")
    logger.error("A major errro has occured")
    logger.critical("this is criticle issue")
