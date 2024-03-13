# ---------------------------------------------------------------------------- #
#                                 Spell Checker                                #
# ---------------------------------------------------------------------------- #

# By Armurier & jjkay03 - Started on 13/02/2024

from .logger import log

from textblob import TextBlob


def spell_checker(text):
    """
    Function taking a string as input and returning the same string without any spelling mistakes

    Args:
        text (str): The text to check
    """

    log("Entered spell checking text", debug=False)
    
    spell_checked_text = TextBlob(text).correct()

    log("Spell checked text and exiting the function", debug=False)


    """
    This version kind of works, however it is not perfect. It is not able to correct the following sentence:
    "I hate peple who kan't spel." ---> does not correct "kan't" to "can't" but "kan" to "an't".

    We also need to check if we can change the language of the spell checker to French, or let the choice to the user.
    """
    return spell_checked_text