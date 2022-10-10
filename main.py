import time
from time import sleep
from typing import Iterable, Dict, List
from threading import Thread

import pydirectinput


# import pyautogui
# CONTINUE = "Continue"
# STOP = "Stop"

def press_key_worker(type_seq: Iterable, interval: float):
    while True:
        before = time.perf_counter()
        pydirectinput.typewrite(type_seq, interval)
        after = time.perf_counter()
        print(f"{type_seq} sec: {after - before}")


def get_thread_handle(type_seq: Iterable, interval: float) -> Thread:
    handle = Thread(target=press_key_worker, args=(type_seq, interval))
    return handle


def run(list_skills: Dict[str, float]):
    handles: List[Thread] = list()
    for key, item in list_skills.items():
        handle = get_thread_handle(key, item)
        handle.start()
        handles.append(handle)

    for handle in handles:
        handle.join()


if __name__ == '__main__':
    sleep(2)

    skills = {
        "5": 19.5,
        "2": 12.5,
    }

    run(skills)
