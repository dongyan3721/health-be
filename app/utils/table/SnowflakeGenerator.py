"""
@author David Antilles
@description 雪花算法id生成器
@timeSnapshot 2024/1/29-20:27:44
"""
import time


class Snowflake:
    def __init__(self, machine_id: int):
        """
        生成雪花算法ID
        :param machine_id: 机器ID
        """
        self.machine_id: int = machine_id
        self.sequence: int = 0
        self.last_timestamp: int = -1

    @staticmethod
    def _wait_next_millis(last_timestamp) -> int:
        timestamp = int(time.time() * 1000)
        while timestamp <= last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp

    @property
    def generate_id(self) -> int:
        timestamp = int(time.time() * 1000)
        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards")
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & 4095
            if self.sequence == 0:
                timestamp = self._wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0
        self.last_timestamp = timestamp
        return ((timestamp - 1288834974657) << 22) | (self.machine_id << 12) | self.sequence


class SnowflakeIDGenerator:
    def __init__(self, model):
        self.model = model

    @staticmethod
    async def generate_id():
        snowflake = Snowflake(0xac85ee4901)
        return snowflake.generate_id
