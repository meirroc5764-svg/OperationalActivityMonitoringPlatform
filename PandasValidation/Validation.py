import math as m
import logging
from logger import logger
from ModelAnomaly import Anomaly
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)



class PandasServers:
    def __init__(self):
        self.WINDOW_SIZE = 20
        self.Z_THRESHOLD = 3.5
        self.CRITICAL_THRESHOLD = 4.5
        self.window = []

    def calculation(self,message):
        if self._validation(message) == None:
            return None


        if len(self.window < self.WINDOW_SIZE):#check if window have enouj value

            self.window.append(int(message["value"]))

            logger.info(f"the window only {len(self.window)}")
            return

        window = pd.Series(self.window)

        mean = window.mean()
        std = window.std()

        value = message["value"]

        z = (value - mean) / std

        if abs(z) >= 3:
            classification = "Critical"
        elif abs(z) >= 2:
            classification = "Warning"
        else:
            classification = "Normal"


        anomaly = Anomaly(
        event_id=message["event_id"],
        source_id=message["source_id"],
        timestamp=message["timestamp"],
        value=message["value"],
        mean=mean,
        standard_deviation=std,
        z_score=z,
        severity=classification,
        detected_at= datetime.now()
        )
        

        return anomaly


            



    def _change_window(self,num):
        for i in range(len(self.window) -1):
            self.window[i] = self.window[i + 1]

            count += 1
        self.window[-1] = num

        


    def _validation(self,message):
        df = pd.DataFrame(message)

        if df.empty:
            logger.info("the message is empty")
            return None

        if df.isnull().values.any():
            logger.info("you have nullbul in data")
            return None

        if not isinstance(df["timestamp"].iloc[0], datetime):
            logger.info("not valid date time")
            return None

        if not isinstance(df["value"].iloc[0], int) or (int(df["value"] > 0)):
            logger.info("in message value name valiue invalid")
            return None

        return message

