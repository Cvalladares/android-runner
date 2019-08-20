import subprocess


def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print(device.id)
    print(device.current_activity())
    # print("Running trace: /home/christian/Desktop/AndroidRunner/android-runner/examples/NAPPA/Scripts/Hillfair_culebra_test.py")
    # subprocess.call("/home/christian/Desktop/AndroidRunner/android-runner/examples/NAPPA/Scripts/Hillfair_culebra_test.py")
