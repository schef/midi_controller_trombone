import digitalio
import analogio
from board import *
import time
import usb_midi

LED_PIN = GP25
BUTTON_SELECT = [GP0, GP1, GP2, GP3, GP4, GP5]
BUTTON_DATA = [GP28, GP27, GP26, GP22, GP21, GP20, GP19]

def get_millis():
    return int(time.monotonic_ns() / 1000 / 1000)

def millis_passed(timestamp):
    return get_millis() - timestamp

def create_output(pin):
    gpio_out = digitalio.DigitalInOut(pin)
    gpio_out.direction = digitalio.Direction.OUTPUT
    return gpio_out

def create_input(pin):
    gpio_in = digitalio.DigitalInOut(pin)
    gpio_in.direction = digitalio.Direction.INPUT
    gpio_in.pull = digitalio.Pull.DOWN
    return gpio_in

def test_peripherals():
    buttons_select = []
    buttons_data = []
    buttons_state = {}
    for pin in BUTTON_SELECT:
        buttons_select.append(create_output(pin))
        buttons_select[-1].value = False
    for pin in BUTTON_DATA:
        buttons_data.append(create_input(pin))
    for select_index, select in enumerate(buttons_select):
        for data_index, data in enumerate(buttons_data):
            buttons_state[(select_index, data_index)] = -1

    while True:
        for select_index, select in enumerate(buttons_select):
            select.value = True
            for data_index, data in enumerate(buttons_data):
                state = data.value
                if state != buttons_state[(select_index, data_index)]:
                    print("button changed[%d:%d] = %d" %
                          (select_index, data_index, state))
                    buttons_state[(select_index, data_index)] = state
            select.value = False

def send_usb_midi_message(data):
    usb_midi.ports[1].write(bytearray(data))

# def send_raw_midi_message(data):
#    uart.write(bytearray(data))
