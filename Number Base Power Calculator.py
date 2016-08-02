#!/usr/bin/python
import os,time

def log(results):
	file =  open('Result.txt',"a")
	file.write(results)
	file.close

def fast_power(a,n):
    start_time = time.time()
    result = 1
    value = a
    power = n
    loop = 0
    while power > 0:
    	loop = loop + 1
        print "\nLoop Attempt [%d]" % loop
        print "-------------------------------------------------------------------------------"
        if power % 2 == 1:
            result = result * value
    	    print "Result: Logged"
        value = value * value
    	print "Value: Logged"
        power = power//2
    	print "Power: ",power
        if power == 0:
			print "Final Result:\n%d" % (result)
        print "-------------------------------------------------------------------------------"
        results = "\n\nLoop Attempt [%d]\n-------------------------------------------------------------------------------\nPower: %d\nValue:\n%d\nResult:\n%d\n-------------------------------------------------------------------------------"% (loop,power,value,result)
        log(results)
        timeused = "Time Used: %.2f\n" % (time.time() - start_time)
        print  timeused
        log("\n%s"%timeused)
    raw_input("Input anything to continue...")

def main():
	try:
		os.system("cls")
		print "-------------------------------------------------------------------------------"
		print "			Number Base Power Calculator"
		print "-------------------------------------------------------------------------------"
		print "Insert 0 to Exit\nLargest Prime Number found: 2^74,207,281"
		a = int(input("Insert Base Value? : "))
		if (a == 0 ):
			exit()
		n = int(input("Insert [%d] Power of? : " % a))
		statement = "Statement: %d^%d" % (a,n)
		log(statement)
		fast_power(a,n)
	except Exception as ex:
		print ""
		print "-------------------------------------------------------------------------------"
		print "				Something Wrong"
		print "-------------------------------------------------------------------------------"
		print "Error Code\t: ",ex
		raw_input("Input anything to continue...")

try:
	file =  open('Result.txt',"w")
	file.write("")
	file.close
	main()
except KeyboardInterrupt:
	print "				Something Wrong"
	print "-------------------------------------------------------------------------------"
	print "Error Code\t: Keyboard Interrupted (CTRL+C Detected)"
