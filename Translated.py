import requests


def translator(language1, language2, text):
    """
    Translates text from one language to another using MyMemory API.

    :param language1: en(English)
    :param language2: it(Italian)
    :param text: Hello my dear friends
    :return: Ciao miei cari amici
    """
    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text,
        'langpair': f'{language1}|{language2}'}

    result_translation = requests.post(url, params=params).json()['responseData']['translatedText']
    print(f'Translated: {result_translation}')


def main():
    input('Welcome to my translator. Press enter to start!\n')
    print("Menu:")
    print('list - list of languages\ntranslate - translate from one language to another\n')

    while (action := input('What your action (q to quit): ').lower()) != 'q':
        match action:
            case 'list':
                lang_dict = {'en': '(English)', 'uk': '(Ukrainian)', 'fr': '(French)', 'es': '(Spanish)',
                             'de': '(German)', 'zh': '(Chinese)', 'ja': '(Japanese)', 'it': '(Italian)',
                             'pt': '(Portuguese)', 'ko': '(Korean)', 'ar': '(Arabic)', 'tr': '(Turkish)'}

                for lang, full_lang in lang_dict.items():
                    print(f'{lang}: {full_lang}')

            case 'translate':
                text = input('What text do you want to translate: ')
                lang1 = input('Enter the first language: ').lower()
                lang2 = input('Enter the language you want to translate into: ').lower()

                translator(lang1, lang2, text)

            case _:
                print('Invalid action. Try Again!')


if __name__ == '__main__':
    main()
