'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
  # must take in the 'word'
  find_th = word.find('th')
  # must see if and how many times it includes the letters "th" (case matters)
  if find_th == -1:
    # this means there were no "th"s, so return 0
    return 0
  # this means that if there are "th"s after the initial "th", to find them and add them up.
  return 1 + count_th(word[find_th+2:])
    