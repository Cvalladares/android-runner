from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
# import os
import time
from com.xhaus.jyson import JysonCodec as json


def run_input(action, newdevice, test):
    action_complete = True
    if action['type'] == 'touch':
        if 'x' in action and 'y' in action and 'duration' in action and 'pause' in action:
            duration = action['duration']
            print 'touch at (' + str(action['x']) + ", " + str(action['y']) + ") for " + str(action['duration']) + \
                  " seconds, with a pause of " + str(action['pause']) + "after."
            if str(action['x']).isdigit() and str(action['y']).isdigit():
                if duration == 0:
                    newdevice.touch(action['x'], action['y'], 'DOWN_AND_UP')
                else:
                    newdevice.touch(action['x'], action['y'], 'DOWN')
                    MonkeyRunner.sleep(duration)
                    newdevice.touch(action['x'], action['y'], 'UP')
            else:
                action_complete = False
        else:
            action_complete = False

    elif action['type'] == 'drag':
        duration = action['duration']
        pause = action['pause']
        str_tuple = (action['points'][0]['x'], action['points'][0]['y'])
        end_tuple = (action['points'][1]['x'], action['points'][1]['y'])
        print 'Drag with duration of ' + str(action['duration']) + " seconds, with a pause of " + str(action['pause']) \
              + "after."

        newdevice.drag(str_tuple, end_tuple, duration, 10)
        MonkeyRunner.sleep(pause)

    elif action['type'] == 'press':
        duration = float(action['duration'])
        times = len(action['keys'])
        # print str(times) + 'keys to press'
        if test:
            for i in range(times):
                print 'pressed %s key for %d' % (action['keys'][i]['key'], duration)
        else:
            for i in range(times):
                newdevice.press(action['keys'][i]['key'], MonkeyDevice.DOWN)
                MonkeyRunner.sleep(duration)
                newdevice.press(action['keys'][i]['key'], MonkeyDevice.UP)

    elif action['type'] == 'nop':
        duration = float(action['pause'])
        print 'pause for %d seconds' % duration
        MonkeyRunner.sleep(duration)

    else:
        action_complete = False
    return action_complete


def get_time_pause(curr_line, prev_line):
    if "'" not in curr_line and "'" not in prev_line:
        curr_event = json.loads(curr_line)
        prev_event = json.loads(prev_line)
        pause = prev_event['pause']
        return pause
    else:
        return 0


def run_jblock(filename, newdevice):
    f = open(filename, 'r')
    '''
    except IOError: 
        print 'problem reading:' + filename
    '''
    print "opened file"
    total_completed = 0
    total_actions = 0
    current_line = 1
    '''
    if not os.path.exists('./images'):
        os.mkdir('./images')
    newdevice.wake()
    pathName = os.path.abspath('./images')
    #print pathName
    startShot = os.path.join(pathName, 'start.png')
    screenshot = newdevice.takeSnapshot()
    screenshot.writeToFile(startShot)
    '''
    prev_line = None
    for line in f:
        print str(current_line) +" - ",
        current_line += 1
        if prev_line is not None:
            pause = get_time_pause(line, prev_line)
            time.sleep(pause)

        prev_line = line
        total_actions += 1
        single_quotes = line.find("\'")
        if single_quotes == -1:
            device_input = json.loads(line)
            complete = run_input(device_input, newdevice, False)  # change to True to
            if complete:
                total_completed += 1
            else:
                action = str(device_input).replace(': u', ': ')
                print 'could not replay action ' + str(action)
        else:
            print 'could not replay action ' + line
    print str(total_completed) + '/' + str(total_actions) + ' actions completed'
    f.close()
    '''
    time.sleep(5)
    screenshotFinal = newdevice.takeSnapshot()
    finishShot = os.path.join(pathName, 'finish.png')
    screenshotFinal.writeToFile(finishShot)
    same = screenshot.sameAs(screenshotFinal, 0.999)
    print 'The images are the same: ' + str(same)
    '''


def main():
    if len(sys.argv) == 1:
        filename = 'testLogicLog.txt'
    else:
        filename = sys.argv[1]
    newdevice = MonkeyRunner.waitForConnection(7.0)
    run_jblock(filename, newdevice)
    print 'done'


# optparse
if __name__ == '__main__':
    main()
