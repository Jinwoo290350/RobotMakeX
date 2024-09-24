# codes make you happy
import novapi
from mbuild.encoder_motor import encoder_motor_class
from mbuild import power_expand_board
from mbuild import gamepad
from mbuild.smartservo import smartservo_class
from mbuild import power_manage_module

# initialize variables
speed = 0
speed1 = 0
speed2 = 0
speed3 = 0
Ball = 0
auto = 0

# new class
encoder_motor_M4 = encoder_motor_class("M4", "INDEX1")
encoder_motor_M2 = encoder_motor_class("M2", "INDEX1")
encoder_motor_M5 = encoder_motor_class("M5", "INDEX1")
encoder_motor_M6 = encoder_motor_class("M6", "INDEX1")
encoder_motor_M3 = encoder_motor_class("M3", "INDEX1")
smartservo_1 = smartservo_class("M1", "INDEX1")
smartservo_2 = smartservo_class("M3", "INDEX1")

def auto():
    global speed, speed1, speed2, speed3, Ball, auto
    while not (1 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99()

    stop_auto()
    while not (0.2 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(65)

    stop_auto()
    while not (0.45 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(65)

    stop_auto()
    while not (1 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(65)

    stop_auto()
    while not (0.37 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-50)
        encoder_motor_M2.set_power(-50)
        encoder_motor_M5.set_power(-50)
        encoder_motor_M6.set_power(-50)

    stop_auto()
    while not (2.7 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-40)
        encoder_motor_M2.set_power(40)
        encoder_motor_M5.set_power(-40)
        encoder_motor_M6.set_power(40)

    stop_auto()
    while not (0.7 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2()

    stop_auto()
    while not (1 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_A5_E0_B8_87()

    stop_auto()
    while not (0.2 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(65)

    stop()
    while not (0.7 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_AB_E0_B8_99_E0_B8_B5_E0_B8_9A()

    stop()
    while not (0.65 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(80)

    stop()
    while not (2 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99()

    stop_auto()
    while not (0.2 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.55 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(65)

    stop_auto()
    while not (0.7 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2()

    stop_auto()
    while not (0.3 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.4 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.8 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-55)
        encoder_motor_M2.set_power(55)
        encoder_motor_M5.set_power(-55)
        encoder_motor_M6.set_power(55)

    stop_auto()
    while not (1.1 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_A5_E0_B8_87()

    stop()
    while not (0.5 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-55)
        encoder_motor_M2.set_power(55)
        encoder_motor_M5.set_power(-55)
        encoder_motor_M6.set_power(55)

    stop_auto()
    while not (0.7 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_AB_E0_B8_99_E0_B8_B5_E0_B8_9A()

    stop()
    while not (2 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99()

    stop_auto()
    while not (0.265 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.55 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(65)

    stop_auto()
    while not (0.2 < novapi.timer()):
        time.sleep(0.001)
        reset()

    stop_auto()
    while not (0.5 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2()

    stop_auto()
    while not (0.55 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.45 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (1 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-55)
        encoder_motor_M2.set_power(55)
        encoder_motor_M5.set_power(-55)
        encoder_motor_M6.set_power(55)

    stop_auto()
    while not (1.1 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_A5_E0_B8_87()

    stop()
    while not (0.2 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-35)
        encoder_motor_M2.set_power(35)
        encoder_motor_M5.set_power(-35)
        encoder_motor_M6.set_power(35)

    stop_auto()
    while not (0.7 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_AB_E0_B8_99_E0_B8_B5_E0_B8_9A()

    stop()
    while not (2 < novapi.timer()):
        time.sleep(0.001)
        _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99()

    stop_auto()
    while not (0.25 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.5 < novapi.timer()):
        time.sleep(0.001)
        encoder_motor_M4.set_power(-65)
        encoder_motor_M2.set_power(-65)
        encoder_motor_M5.set_power(-65)
        encoder_motor_M6.set_power(-65)

    stop_auto()
    while not (0.45 < novapi.timer()):
        time.sleep(0.001)
        gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2()

    stop_auto()

def _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC4", -100)
    power_expand_board.set_power("DC6", 100)

def _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_A5_E0_B8_87():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC4", 70)
    power_expand_board.set_power("DC6", -70)

def gripper_stop():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.stop("DC2")

def gripper__E0_B8_AB_E0_B8_99_E0_B8_B5_E0_B8_9A():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC2", 45)
    power_expand_board.set_power("DC5", -35)

def gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC2", -45)
    power_expand_board.set_power("DC5", 35)

def flag_down():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC7", -40)

def only_suck():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC1", -75)

def manual():
    global speed, speed1, speed2, speed3, Ball, auto
    while True:
        time.sleep(0.001)
        if gamepad.is_key_pressed("Up"):
          _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_82_E0_B8_B6_E0_B9_89_E0_B8_99()

        else:
          if gamepad.is_key_pressed("Down"):
            _E0_B8_94_E0_B8_B6_E0_B8_87gripper_E0_B8_A5_E0_B8_87()

          else:
            if gamepad.get_joystick("Ly") < 0:
              forward()

            else:
              if gamepad.get_joystick("Ly") > 0:
                backward()

              else:
                if gamepad.get_joystick("Lx") > 0:
                  left_x()

                else:
                  if gamepad.get_joystick("Lx") < 0:
                    right_x()

                  else:
                    if gamepad.is_key_pressed("N2"):
                      reset()

                    else:
                      if gamepad.is_key_pressed("Right"):
                        gripper__E0_B8_9B_E0_B8_A5_E0_B9_88_E0_B8_AD_E0_B8_A2()

                      else:
                        if gamepad.is_key_pressed("Left"):
                          gripper__E0_B8_AB_E0_B8_99_E0_B8_B5_E0_B8_9A()

                        else:
                          if gamepad.is_key_pressed("R1"):
                            shoot()

                          else:
                            if gamepad.is_key_pressed("L2"):
                              _E0_B9_80_E0_B8_9B_E0_B9_89_E0_B8_B2_E0_B9_80_E0_B8_82_E0_B9_89_E0_B8_B2()

                            else:
                              if gamepad.is_key_pressed("+"):
                                _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_9A_E0_B8_AD_E0_B8_A5_E0_B8_AD_E0_B8_AD_E0_B8_81()

                              else:
                                if gamepad.is_key_pressed("N1"):
                                  _E0_B8_AB_E0_B8_A2_E0_B8_B8_E0_B8_94()

                                else:
                                  if gamepad.is_key_pressed("R2"):
                                    _E0_B9_80_E0_B8_9B_E0_B9_89_E0_B8_B2_E0_B8_AD_E0_B8_AD_E0_B8_81()

                                  else:
                                    if gamepad.get_joystick("Rx") > 0:
                                      right_turn()

                                    else:
                                      if gamepad.get_joystick("Rx") < 0:
                                        left_turn()

                                      else:
                                        if gamepad.is_key_pressed("N3"):
                                          _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_81_E0_B8_A5_E0_B8_B1_E0_B8_9A()

                                        else:
                                          if gamepad.is_key_pressed("L1"):
                                            flag_down()

                                          else:
                                            if gamepad.get_joystick("Ry") < 0:
                                              HAHU()

                                            else:
                                              if gamepad.get_joystick("Ry") > 0:
                                                HAHA()

                                              else:
                                                if gamepad.is_key_pressed("L_Thumb"):
                                                  speed = 1

                                                else:
                                                  if gamepad.is_key_pressed("R_Thumb"):
                                                    speed = 0

                                                  else:
                                                    if gamepad.is_key_pressed("N4"):
                                                      power_expand_board.stop("DC3")
                                                      power_expand_board.stop("DC1")
                                                      power_expand_board.stop("DC2")

                                                    else:
                                                      if gamepad.is_key_pressed("≡"):
                                                        _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_9A_E0_B8_AD_E0_B8_A5_E0_B9_80_E0_B8_82_E0_B9_89_E0_B8_B2()

                                                      else:
                                                        stop()

def flag():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC7", 40)

def shoot():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("BL1", 100)
    power_expand_board.set_power("BL2", 100)

def suck():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("BL1", 65)
    power_expand_board.set_power("BL2", 65)
    power_expand_board.set_power("DC1", -75)
    power_expand_board.set_power("DC2", 100)

def left_turn():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M4.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M5.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M2.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M6.set_power(speed2 * gamepad.get_joystick("Rx"))

def _E0_B8_AB_E0_B8_A2_E0_B8_B8_E0_B8_94():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.stop("BL1")
    power_expand_board.stop("BL2")

def right_turn():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M4.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M5.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M2.set_power(speed2 * gamepad.get_joystick("Rx"))
    encoder_motor_M6.set_power(speed2 * gamepad.get_joystick("Rx"))

def _E0_B9_80_E0_B8_9B_E0_B9_89_E0_B8_B2_E0_B9_80_E0_B8_82_E0_B9_89_E0_B8_B2():
    global speed, speed1, speed2, speed3, Ball, auto
    smartservo_1.set_power(5)

def _E0_B9_80_E0_B8_9B_E0_B9_89_E0_B8_B2_E0_B8_AD_E0_B8_AD_E0_B8_81():
    global speed, speed1, speed2, speed3, Ball, auto
    smartservo_1.set_power(-5)

def _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_9A_E0_B8_AD_E0_B8_A5_E0_B9_80_E0_B8_82_E0_B9_89_E0_B8_B2():
    global speed, speed1, speed2, speed3, Ball, auto
    smartservo_2.set_power(7)

def right_x_slow():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M5.set_power(65)
    encoder_motor_M2.set_power(-55)
    encoder_motor_M3.set_power(65)
    encoder_motor_M6.set_power(-55)

def stop():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M4.set_power(0)
    encoder_motor_M2.set_power(0)
    encoder_motor_M5.set_power(0)
    encoder_motor_M6.set_power(0)
    power_expand_board.stop("DC7")
    novapi.reset_timer()
    smartservo_1.set_power(0)
    power_expand_board.stop("DC6")
    power_expand_board.stop("DC4")
    smartservo_2.set_power(0)

def _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_9A_E0_B8_AD_E0_B8_A5_E0_B8_AD_E0_B8_AD_E0_B8_81():
    global speed, speed1, speed2, speed3, Ball, auto
    smartservo_2.set_power(-7)

def left_x_slow():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M3.set_power(-55)
    encoder_motor_M6.set_power(65)
    encoder_motor_M5.set_power(-55)
    encoder_motor_M2.set_power(65)

def reset():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC1", 85)
    power_expand_board.set_power("DC3", 85)

def stop_auto():
    global speed, speed1, speed2, speed3, Ball, auto
    encoder_motor_M4.set_power(0)
    encoder_motor_M2.set_power(0)
    encoder_motor_M5.set_power(0)
    encoder_motor_M6.set_power(0)
    power_expand_board.stop("DC7")
    novapi.reset_timer()
    smartservo_1.set_power(0)
    smartservo_2.set_power(0)

def _E0_B8_AB_E0_B8_A1_E0_B8_B8_E0_B8_99_E0_B8_81_E0_B8_A5_E0_B8_B1_E0_B8_9A():
    global speed, speed1, speed2, speed3, Ball, auto
    power_expand_board.set_power("DC1", -80)
    power_expand_board.set_power("DC3", -80)

def HAHU():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0:
      encoder_motor_M6.set_power(gamepad.get_joystick("Ry"))
      encoder_motor_M2.set_power(-1 * gamepad.get_joystick("Ry"))

    else:
      encoder_motor_M6.set_power(-1 * gamepad.get_joystick("Ry"))
      encoder_motor_M2.set_power(gamepad.get_joystick("Ry"))

def HAHA():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0 or speed == 1:
      encoder_motor_M2.set_power(gamepad.get_joystick("Ry"))
      encoder_motor_M4.set_power(-1 * gamepad.get_joystick("Ry"))

    else:
      encoder_motor_M5.set_power(-1 * gamepad.get_joystick("Ry"))
      encoder_motor_M4.set_power(gamepad.get_joystick("Ry"))

def forward():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0:
      encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Ly"))
      encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Ly"))
      encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Ly"))
      encoder_motor_M6.set_power(speed1 * gamepad.get_joystick("Ly"))

    else:
      if speed == 1:
        encoder_motor_M6.set_power(speed3 * gamepad.get_joystick("Ly"))
        encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Ly"))
        encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Ly"))
        encoder_motor_M4.set_power(speed1 * gamepad.get_joystick("Ly"))

def backward():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0:
      encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Ly"))
      encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Ly"))
      encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Ly"))
      encoder_motor_M6.set_power(speed1 * gamepad.get_joystick("Ly"))

    else:
      if speed == 1:
        encoder_motor_M6.set_power(speed3 * gamepad.get_joystick("Ly"))
        encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Ly"))
        encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Ly"))
        encoder_motor_M4.set_power(speed1 * gamepad.get_joystick("Ly"))

def right_x():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0:
      encoder_motor_M2.set_power(speed3 * gamepad.get_joystick("Lx"))
      encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Lx"))
      encoder_motor_M6.set_power(speed1 * gamepad.get_joystick("Lx"))
      encoder_motor_M5.set_power(speed1 * gamepad.get_joystick("Lx"))

    else:
      if speed == 1:
        encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Lx"))
        encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Lx"))
        encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Lx"))
        encoder_motor_M5.set_power(speed1 * gamepad.get_joystick("Lx"))

def left_x():
    global speed, speed1, speed2, speed3, Ball, auto
    if speed == 0:
      encoder_motor_M2.set_power(speed3 * gamepad.get_joystick("Lx"))
      encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Lx"))
      encoder_motor_M6.set_power(speed1 * gamepad.get_joystick("Lx"))
      encoder_motor_M5.set_power(speed1 * gamepad.get_joystick("Lx"))

    else:
      if speed == 1:
        encoder_motor_M5.set_power(speed3 * gamepad.get_joystick("Lx"))
        encoder_motor_M4.set_power(speed3 * gamepad.get_joystick("Lx"))
        encoder_motor_M6.set_power(speed1 * gamepad.get_joystick("Lx"))
        encoder_motor_M2.set_power(speed1 * gamepad.get_joystick("Lx"))

speed = 0
speed2 = -0.9
speed1 = 0.8
speed3 = -1 * speed1
Ball = 0
if power_manage_module.is_auto_mode():
  speed = 0
  auto()

else:
  while True:
      time.sleep(0.001)
      manual()

