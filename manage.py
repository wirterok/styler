import sys

# from typing import Any
# import inspect

# from db.scripts import init_db
# from scripts import *

# from utils.utils import start_loop

# class Management:
#     def __call__(self, command, *args, **kwargs) -> Any:
#         for name, call in globals().items():
#             if name == command:
#                 if not inspect.iscoroutinefunction(call):
#                     return call(*args, **kwargs)
#                 with start_loop() as loop:
#                     loop.run_until_complete(call(*args))

from fastapi_management.management.executors import Executor


if __name__ == "__main__":
    executor = Executor(sys.argv[1:])
    executor.execute()
    # Management()(*sys.argv[1:])