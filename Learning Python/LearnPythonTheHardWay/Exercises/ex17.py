#More files

#===============================================================================
# from sys import argv
# 2 from os.path import exists
# 3
# 4 script, from_file, to_file = argv
# 5
# 6 print "Copying from %s to %s" % (from_file, to_file)
# 7
# 8 # we could do these two on one line too, how?
# 9 in_file = open(from_file)
# 10 indata = in_file.read()
# 11
# 12 print "The input file is %d bytes long" % len(indata)
# 13
# 14 print "Does the output file exist? %r" % exists(to_file)
# 15 print "Ready, hit RETURN to continue, CTRL- C to abort."
# 16 raw_input()
# 17
# 18 out_file = open(to_file, 'w')
# 19 out_file.write(indata)
# 20
# 21 print "Alright, all done."
# 22
# 23 out_file.close()
# 24 in_file.close()
#===============================================================================