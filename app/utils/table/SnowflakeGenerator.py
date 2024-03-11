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


class SnowFlakeSmall:
    def __init__(self, worker_id):
        # Bits allocation
        self.worker_id_bits = 5
        self.sequence_bits = 7

        # Max values
        self.max_worker_id = (1 << self.worker_id_bits) - 1
        self.max_sequence = (1 << self.sequence_bits) - 1

        # Shifts
        self.timestamp_shift = self.worker_id_bits + self.sequence_bits
        self.worker_id_shift = self.sequence_bits

        # Epoch and worker ID
        self.epoch = 1690373045764
        self.worker_id = worker_id

        # Internal state
        self.sequence = 0
        self.last_timestamp = -1

        # Validate worker ID
        if worker_id > self.max_worker_id or worker_id < 0:
            raise ValueError(f"Invalid worker ID, should be in the range [0, {self.max_worker_id}]")

    @property
    def next_id(self):
        curr_timestamp = self.timestamp_gen()

        if curr_timestamp < self.last_timestamp:
            raise ValueError(f"Server time moved backward {self.last_timestamp - curr_timestamp} milliseconds")

        if curr_timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.max_sequence
            if self.sequence == 0:
                curr_timestamp = self.wait_next_millis(curr_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = curr_timestamp

        return ((curr_timestamp - self.epoch) << self.timestamp_shift) | (
                    self.worker_id << self.worker_id_shift) | self.sequence

    def wait_next_millis(self, curr_timestamp):
        while curr_timestamp <= self.last_timestamp:
            curr_timestamp = self.timestamp_gen()
        return curr_timestamp

    def timestamp_gen(self):
        return int(time.time() * 1000)


class SnowflakeIDGenerator:
    def __init__(self, model):
        self.model = model

    @staticmethod
    async def generate_id():
        return SnowFlakeSmall(0xa).next_id
