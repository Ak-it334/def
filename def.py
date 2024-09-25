
calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(*args):
    string = str(input())
    s = (len(string), string.upper(), string.lower())
    print(tuple(s))
    count_calls()
def is_contains(*args):
    string = str(input())
    list_search = list(input())
    count_calls()
    if string in list_search:
       print(True)
    else:
       print(False)

string_info()
string_info()
string_info()
is_contains()
print(calls)
