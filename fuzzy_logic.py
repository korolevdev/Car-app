import fuzzy.storage.fcl.Reader
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("fuzzy_data")
 
# preallocate input and output values
my_input = {
        "Distance" : 0.0,
        }
my_output = {
        "Speed_Correction" : 0.0
        }
 
def fuzzy_speed_calc(dist):
    my_input["Distance"] = int(dist)
    system.calculate(my_input, my_output)
    return my_output["Speed_Correction"]/100.0