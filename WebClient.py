'''
web client to visit mysite by script
'''
import sys, urllib2

def dump_info():
    print 'aa'
    req = urllib2.Request("http://127.0.0.1:8000/testJQuery/")
    print 'aa'
    fd = urllib2.urlopen("http://127.0.0.1:8000/testJQuery/")
    print "retrieved ", fd.geturl()
#     print fd
    info = fd.info();
    for key, value in info.items():
        print "%s = %s" % (key, value) 


if __name__ == "__main__":
    dump_info()