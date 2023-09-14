import random
from modules.Console import console
from modules.Inputs import PressButton, WaitFrames, ReleaseInputs
from modules.Memory import GetTrainer, GetTask


def ModeSpin():
    try:
        # TODO home position, FollowPath() if trainer walks off
        ReleaseInputs()
        directions = ['Up', 'Right', 'Down', 'Left']
        directions.remove(GetTrainer()['facing'])  # Remove currently facing direction from possible inputs
        PressButton([random.choice(directions)])
        WaitFrames(5)

    except:
        console.print_exception(show_locals=True)


def ModeFishing():
    PressButton(['Select'], 3)
    task = GetTask('TASK_FISHING')
    while task != {} and task['isActive']:
        # Check if in `Fishing_WaitForA` or `Fishing_StartEncounter` or `Fishing_EndNoMon`
        if task['data'][0] == 7 or task['data'][0] == 10 or \
                task['data'][0] == 15:
            PressButton(["A"])
        task = GetTask('TASK_FISHING')