def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    list_phrase = phrase.lower().split(' ')
    
    titled = [word.capitalize() for word in list_phrase]

    return ' '.join(titled)