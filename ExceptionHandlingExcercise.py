# EXCEPTION HANDLING
# Any statement or function that might throw error is enclosed in try,except ,finally methods

# try --> put the code that might throw an error inside try: (with a : at the end)
try :
    print x
# except --> in case an error occurs then put the statement or code that will have to executed instead inside except
except:
    print "An error occured"

# finally --> put the statement or code that will have to be executed irrespective of the error
finally:
    print "This sentece will defenitely be printed"


try:
    #print x
    print 2/0
except NameError: # This except block will be executed only when there is NameError type of error
    print "This is undefined variable"
except: # As no type of error is specified here for all the other type of error this block is executed
    print "Someother kind of error"
finally: # Irrespective of any error this block is executed
    print "finally print this anyway..."


