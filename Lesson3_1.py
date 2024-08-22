calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len (string), string.upper(), string.lower())
def is_contain(string, da_prostit_menya_Bog):
    string_info.upper()
    
print (string_info('DINNER'))
print (string_info('GIRL HELL 1999'))
print (is_contain('Katamari', ['Katamari', 'amar', 'maramaarmaam']))
print (is_contain('S33KH3LP', ['S33KH3LP', 'SEEKHELP', 'S33K HELP']))
print (calls)