lines = open("squeue.log", 'r').readlines()[1:]
output = open("Running.log", 'w')


for line in lines:
        if (line.split()[4] != "PD"):
            output.write(line)
output.seek(0)
output.close    
#######################################
output2 = open("Running.log", 'r')
AllActiveNodes=0
ActiveCommNodes=0
ActiveUniqueNodes=0
max=0
for line2 in output2:
    num6 = int(line2.split()[6])
    AllActiveNodes += num6
    if num6 >=4:
        if num6>max:
            max=num6
        ActiveCommNodes += num6
output.seek(0)
output.close   
#######################################
output3 = open("Running.log", 'r')
commnodeslist = open("commnodeslist.log", 'w')
for line3 in output3:
        value=int(line3.split()[6])
        if value != 1:
            commnodeslist.write(line3.split()[7])
            commnodeslist.write('\n')
commnodeslist.seek(0)
commnodeslist.close
output3.close  


words_set = set()
duplicate_set = set()

with open('commnodeslist.log') as input_file:
    file_content = input_file.readlines()

for lines in file_content:
    words = lines.split(",")
    for word in words:
        if word in words_set:
            duplicate_set.add(word)
        else:
            words_set.add(word)

for word in duplicate_set:
    print(word)

      
print("AllActiveNodes (Running status)= " , AllActiveNodes)
print("ActiveCommNodes (involving >2 nodes)= " , ActiveCommNodes)
print("Maximum nodes running= " , max)
print("Overall Background traffic= ", (ActiveCommNodes/AllActiveNodes) * (ActiveCommNodes/980))