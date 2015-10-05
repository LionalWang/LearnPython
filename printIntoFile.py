import sys
print >> sys.stderr, 'Fatal error: invalid input!'
logfile = open('/tmp/mylog.txt', 'a')
print >> logfile, 'Fatal error: invalid input!'
logfile.close
