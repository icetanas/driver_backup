import odrive
from odrive.enums import *
import time

odrv0 = odrive.find_any()
print(odrv0)

odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.controller.input_vel=2

for i in range(50):
	print("Encoder Position:",odrv0.axis1.encoder.pos_estimate)
	print("Encoder Velocity:",odrv0.axis1.encoder.vel_estimate)
	time.sleep(0.5)

odrv0.axis1.controller.input_vel=0
odrv0.axis1.requested_state = AXIS_STATE_IDLE
	
