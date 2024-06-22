import locale
locale.setlocale(locale.LC_ALL, '')

def format_datetime(value, fmt='%m월 %d일 %p %I:%M'):
    return value.strftime(fmt)