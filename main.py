def on_button_pressed_a():
    radio.set_group(1)
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)
