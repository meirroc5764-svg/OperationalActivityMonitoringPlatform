import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)

formater = logging.Formatter( 
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

consoleHendler = logging.StreamHandler()
fileHendler = logging.FileHandler("app.log", encoding="utf-8")

consoleHendler.setFormatter(formater)
fileHendler.setFormatter(formater)

logger.addHandler(consoleHendler)
logger.addHandler(fileHendler)