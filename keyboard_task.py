import keyboard, time
def KeyPressSample(startkey='tab', endkey='esc'):
    while True:  # making a inifinte loop
        try:
            # Wait for the next event.
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
                print('space was pressed')
        except KeyboardInterrupt:
            print('\nDone Reading input. Keyboard Interupt.')
            break
        except Exception as e:
            print(e)
            break

KeyPressSample()