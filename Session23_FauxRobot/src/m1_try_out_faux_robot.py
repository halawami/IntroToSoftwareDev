"""
For trying out the faux (fake) robot.
"""

import rosebot.faux_rosebot as rb  # Using the FAUX robot.
import time

def main():
    """ Make a robot.  Connect.  Try making it do some things. """
    robot = rb.RoseBot()  # Makes a robot

    # TODO: Play around with a faux (fake) robot.
    #       Use the DOT trick to find out what you can do!
    #       Start by CONNECTING to the robot.
    #       Throughtout, for arguments provide fake data
    #          (whatever you want).

    robot.buzzer.play_tone(146)
    time.sleep(2.5)
    robot.buzzer.stop()

    robot.sensor_reader.front_proximity_sensor.read()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
