# Let us simplify the code
# by using the "with" Keyword.
# write to a text file

with open('t.txt','w') as  f :
    f.write('HEllo World ! ')
    f.close()

# It will be Closed automaticallly
# f = open('t.txt', mode =  'w')
# w = create and write
# r = read(default)
# a = append
# x = create if not exist
# with = with satement is used tp wrap the execution of a block of code
#           within  methods defined by a context manger
