import fuzzy.storage.fcl.Reader
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("fuzzy_data")
 
# preallocate input and output values
my_input = {
        "Distance" : 0.0,
        }
my_output = {
        "Speed_Correction" : 0.0
        }
 
i = 400
# if you need only one calculation you do not need the while
while i > 0:
        # set input values
        my_input["Distance"] = i
 
        # calculate
        system.calculate(my_input, my_output)
 
        # now use outputs
        print "X = ", my_output["Speed_Correction"], "i = ", i
	if i > 10:
		i = i - 10
	else:
		i = i - 1