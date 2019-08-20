# from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
from com.xhaus.jyson import JysonCodec as json


def run_input(action):
    # newdevice.touch(action['x'], action['y'], DOWN)
    # counter = action['up'] - action['down']
    # time.sleep(counter)
    # newdevice.touch(action['x'], action['y'], UP)

    if str(action['type']) is 'touch':
        print 'touch at (' + str(action['x']) + ", " + str(action['y']) + ") for " + str(action['duration']) + \
              " seconds, with a pause of " + str(action['pause']) + "after."
    elif str(action['type']) is 'drag':
        print 'Drag with duration of ' + str(action['pause']) + " seconds, with a pause of " + str(action['pause']) \
              + "after."
    elif str(action['type']) is 'pause':
        print 'Pause of duration ' + str(action['pause'])


def run_jblock(filename):
    f = open(filename, 'r')
    for line in f:
        device_input = json.loads(line)
        run_input(device_input)


def main():
    if len(sys.argv) != 2:
        print 'usage: ./replay.py file'
        sys.exit(1)
    filename = sys.argv[1]
    # newdevice = MonkeyRunner.waitForConnection()
    # deviceAC = build_jblock(filename)
    run_jblock(filename)


if __name__ == '__main__':
    main()
