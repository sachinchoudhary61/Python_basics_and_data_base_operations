# A safer way of reading various from a dictionary
data = {'France': 'Paris','Italy':'Rome'}
#capiatal = data['Germany'] # error
capital = data.get('Germany') # ok
# but it returns 'None'
print(capital)

capital = data.get('Germany','??')
print(capital)# paris "??"

# all description
# When Working with dictionaries,make sure you are trying to read an existing key.
# Otherwise ,either use a "try" block or call the "get" method.
# if the key is missing, it returns "none". In the the second parameter, you
# can pass a default value that will be returned if there's no key.
