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



try: # put code that needs to executed and could have some error that needs to be caught so that
    # program doesnt stop executing
    print x
except: # If there is an error then the code within the except block is executed
    print "Print this if something went wrong"
else: # if there is no error in the try block and code runs smoothly then after that block is executed
    #code with in the else block is executed
    print "Print this if nothing went wrong"
finally: # Irrespective of weather there is an error or not the code block within finally is executed.
    print "Print this no matter what.."

