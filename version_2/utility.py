from re import compile
def clean(text):
    ansi_escape = compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)