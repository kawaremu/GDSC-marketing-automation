import re


columns = "" #get the columns from the csv file
message = 'Hello (name), your age is (age)'


def repl(m,info=[]):
    val = m.group().strip('()')
    d = {'mimi':'name','23':'age'}
    flipped = dict(zip(d.values(), d.keys()))
    return '{}'.format(flipped.get(val,''))
      

# For each
result = re.sub(r'\([^()]+\)', repl, message)

print(result)

