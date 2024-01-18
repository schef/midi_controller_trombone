import peripherals
import midi_player
import common

FIRST_CHANNEL = 1

# s:d #######################
# 0:0 0:1 0:2 0:3 0:4 0:5 0:6
# 1:0 1:1 1:2 1:3 1:4 1:5 1:6
# 2:0 2:1 2:2 2:3 2:4 2:5 2:6
# 3:0 3:1 3:2 3:3 3:4 3:5 3:6
# 4:0 4:1 4:2 4:3 4:4 4:5 4:6
# 5:0 5:1 5:2 5:3 5:4 5:5 5:6

#BASE_TONE = 48 - 2
BASE_TONE = 60 - 2 - 6

def get_button_midi_num(select_index, data_index):
    midi_index = -1
    if select_index == 5:
        midi_index = BASE_TONE + data_index
    elif select_index == 4:
        midi_index = BASE_TONE + 7 + data_index
    elif select_index == 3:
        midi_index = BASE_TONE + 12 + data_index
    elif select_index == 2:
        midi_index = BASE_TONE + 12 + 4 + data_index
    elif select_index == 1:
        midi_index = BASE_TONE + 12 + 7 + data_index
    elif select_index == 0:
        midi_index = BASE_TONE + 24 + data_index
    return midi_index

def on_button_change(select_index, data_index, state):
    midi_index = get_button_midi_num(select_index, data_index)
    if midi_index != -1:
        if state:
            midi_player.note_on(FIRST_CHANNEL, midi_index, 100)
        else:
            midi_player.note_off(FIRST_CHANNEL, midi_index)

def init():
    peripherals.register_on_button_change_cb(on_button_change)

def loop():
    pass
