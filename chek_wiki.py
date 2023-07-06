import wikipedia


def check_wiki(text: str, language: str = 'uz') -> dict:
    response = {
        'data': False,
        'word': False,
        'summary': None,
        'search': None
    }
    wikipedia.set_lang(language)
    if text == '':
        return response
    try:
        summary = wikipedia.summary(text)
    except:
        items = wikipedia.search(text)
        if items:
            response['search'] = items
            response['word'] = True
    else:
        response['summary'] = summary
        response['data'] = True
    return response


if __name__ == '__main__':
    print(check_wiki('Sunnat'))
