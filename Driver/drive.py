import odrive
from odrive.enums import *
odrv0 = odrive.find_any()
odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.controller.input_vel=0
