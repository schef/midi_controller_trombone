import common

buttons_select = []
buttons_data = []
buttons_state = {}

on_button_change_cb = None

def init():
    global buttons_select, buttons_data, buttons_state
    for pin in common.BUTTON_SELECT:
        buttons_select.append(common.create_output(pin))
        buttons_select[-1].value = False
    for pin in common.BUTTON_DATA:
        buttons_data.append(common.create_input(pin))
    for select_index, select in enumerate(buttons_select):
        for data_index, data in enumerate(buttons_data):
            buttons_state[(select_index, data_index)] = -1

def loop():
    global buttons_select, buttons_data, buttons_state
    global on_button_change_cb
    for select_index, select in enumerate(buttons_select):
        select.value = True
        for data_index, data in enumerate(buttons_data):
            state = data.value
            if state != buttons_state[(select_index, data_index)]:
                buttons_state[(select_index, data_index)] = state
                print("button changed[%d:%d] = %d" %
                      (select_index, data_index, state))
                if on_button_change_cb:
                    on_button_change_cb(select_index, data_index, state)
        select.value = False

def register_on_button_change_cb(cb):
    global on_button_change_cb
    on_button_change_cb = cb

def test_loop():
    init()
    while True:
        loop()
