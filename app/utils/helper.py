import random  
 
def csv_to_dict(file):
    d = {}
    for str in file.readlines()[1:len(file.readlines())-1]:
        line = str.split(',')
        #if there are commas in the job class
        if len(line) > 2:
            the_key = ",".join(line[:len(line) - 1])
            d[the_key] = ",".join(line[len(line) - 1:])
        else:
            d[line[0]] = line[1]
    return d