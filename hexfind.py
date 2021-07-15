import re
a=0
matchyy = []
regex_pattern = r"[#](?:[a-fA-F0-9]{6}|[a-fA-F0-9]{3})"
for i in range(int(input())):
    line = input()
    if "}" in line:
        #print("end")
        a -= 1
    if a>=1:
        #print("checking")
        matchy = re.findall(regex_pattern, line)
        for i in matchy:
            print(i)
            #matchyy.append(i[:-1])
    if "{" in line:
        #print("enter")
        a+=1
    else:
        pass

#print(matchyy)
