import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = ''  # сюди складатимемо результат
    inside_tag = False  # прапорець: чи ми зараз "всередині" тегу <...>

    for symbol in html:
        if symbol == '<':
            # почався тег - вмикаємо прапорець і сам символ не додаємо
            inside_tag = True
        elif symbol == '>':
            # тег закінчився - вимикаємо прапорець і сам символ не додаємо
            inside_tag = False
        elif not inside_tag:
            # звичайний символ поза тегом - додаємо його в результат
            clean_text += symbol

