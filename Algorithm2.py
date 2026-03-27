#names: 
people = [3, 5, 3, 4, 2, 2, 1, 4, 1]
limit = 5
boats = 0
lp = 0
rp = len(people) -1
people.sort() #timsort has time complexity nlogn according to google
while lp <= rp: #loop till pointers meet
    if people[lp] + people[rp] <= limit: #if heavier and lighter can be paired, "pair them" by moving pointers
        lp += 1
        rp -= 1
    else:   #else requires a person to have their own boat, move over only one pointer to see if they pair
        rp -=1
    boats += 1
print(boats)
