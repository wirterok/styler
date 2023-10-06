import asyncio

class start_loop(object):
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def __enter__(self):
        return self.loop

    def __exit__(self, type, value, traceback):
        self.loop.close()