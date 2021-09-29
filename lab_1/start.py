"""
Language detection starter
"""

import os


PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEXTS_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'texts')

if __name__ == '__main__':

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'en.txt'), 'r', encoding='utf-8') as file_to_read:
        en_text = file_to_read.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'de.txt'), 'r', encoding='utf-8') as file_to_read:
        de_text = file_to_read.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'unknown.txt'), 'r', encoding='utf-8') as \
            file_to_read:
        unknown_text = file_to_read.read()

    import main

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'la.txt'), 'r', encoding='utf-8') as file_to_read:
        la_text = file_to_read.read()

    english = main.create_language_profile('en', en_text, [])
    german = main.create_language_profile('de', de_text, [])
    latin = main.create_language_profile('la', la_text, [])
    unknown = main.create_language_profile('unknown', unknown_text, [])

    languages_complete = [english, german, latin]

    top_n = 4

    EXPECTED = 'en'
    RESULT = main.detect_language(unknown, english, german, top_n)
    RESULT_advanced = main.detect_language_advanced(unknown, languages_complete, [latin, german], top_n)
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Detection not working'
