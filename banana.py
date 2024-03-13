# ---------------------------------------------------------------------------- #
#                            Banana - Spell Checker                            #
# ---------------------------------------------------------------------------- #
# By jjkay03 & Armurier - Started on 13/02/2024

from modules import * # Import all custom modules in /modules dir
import keyboard

# ----------------------------------- Main ----------------------------------- #
log_create_file()
log("BANANA IS STARTING!")

# Hotkeys
keyboard.add_hotkey("alt+q", get_selected_text)
keyboard.wait()