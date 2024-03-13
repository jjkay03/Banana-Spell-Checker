# Cyberpulse logger module by jjkay03

import os
import datetime
import inspect


log_debug_mode = True
log_folder_path = "logs"
log_file_path = ""
log_folder_created = False


# Function: Create logs folder and log file
def log_create_file():
    global log_file_path, log_folder_created

    if not os.path.exists(log_folder_path): # Make a log folder
        os.mkdir(log_folder_path)
        log_folder_created = True

    log_file_path = os.path.join(log_folder_path, datetime.datetime.now().strftime("%Y-%m-%d - %H-%M-%S") + '.log')
    with open(log_file_path, 'w'): pass # Create log file

    log(f"Creating log file: {log_file_path}")


# Function: Log info, print log message + time
def log(message, debug=False):
    global log_file_path
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # If log debug mode is on and debug message log the debug
    if log_debug_mode==True and debug==True:
        # Get the filename of the calling module
        caller_frame = inspect.stack()[1]
        caller_module = inspect.getmodulename(caller_frame[1])
        log_message = f"[{current_time} DEBUG]: [{caller_module}.py] {message}"
    
    # If log debug mode is off and debug message ignore the debug
    elif log_debug_mode==False and debug==True:
        return
    
    # If normal log message log it
    else:
        log_message = f"[{current_time} INFO]: {message}"

    print(log_message)

    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message + '\n')
