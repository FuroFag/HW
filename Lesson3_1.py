calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len (string), string.upper(), string.lower())
def is_contain(string, list_to_search):
    return string.casefold() in [s.casefold for s in list_to_search]
print (string_info('DINNER'))
print (string_info('GIRL HELL 1999'))
print (is_contain('Katamari', ['KAtAmari', 'amar', 'maramaarmaam']))
print (is_contain('S33KH3LP', ['S33KH3LP', 'SEEKHELP', 'S33K HELP']))
print (calls)