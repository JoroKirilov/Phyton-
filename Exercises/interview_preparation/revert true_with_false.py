# def tab_turn_on_button(turn_on_off):
#     return not turn_on_off
#
#
# button = False
# button = tab_turn_on_button(button)
# print(button)
# button = tab_turn_on_button(button)
# print(button)


from itertools import cycle

button_mode = cycle(("On", "Off"))
print(next(button_mode))
print(next(button_mode))
print(next(button_mode))
