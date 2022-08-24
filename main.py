import os
import config


def get_words( file_path ):
    with open( file_path, 'r' ) as f:
        text = f.readlines()[0]
        words = text.split()
    return words


def send_message( phone_number, message ):
    os.system('osascript send.scpt {} "{}"'.format( phone_number, message ) )


"""
TEXT_FILE.TXT -> message to send passed in through format: file_name.txt
TARGET_PHONE  -> phone number being targeted by the applescript send.scpt
                 can be set in the config.py file.
"""
if __name__ == '__main__':
    words = get_words( config.MESSAGE_TO_SEND )
    for word in words:
        send_message( config.TARGET_PHONE, word )