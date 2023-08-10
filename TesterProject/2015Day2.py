#pt 1
txt_file = open("2015Day2.txt")
#edit_file = txt_file.split("x")
str_txt = ""
for line in txt_file:
    str_txt += line

edit_txt = str_txt.split("\n")
paper_sum = 0
for present in edit_txt:
    if(present != ""):
        dims = present.split("x")
        dims[0] = int(dims[0])
        dims[1] = int(dims[1])
        dims[2] = int(dims[2])
        paper_sum += 2 * dims[0] * dims[1]
        paper_sum += 2 * dims[0] * dims[2]
        paper_sum += 2 * dims[1] * dims[2]
        if (dims[0] * dims[1]) <= (dims[0] * dims[2]) and (dims[0] * dims[1]) <= (dims[1] * dims[2]):
            paper_sum += dims[0] * dims[1]
        elif (dims[0] * dims[2]) <= (dims[0] * dims[1]) and (dims[0] * dims[2]) <= (dims[1] * dims[2]):
            paper_sum += dims[0] * dims[2]
        else:
            paper_sum += dims[1] * dims[2]
print("The total amount of Wrapping paper required: " + str(paper_sum) + " square feet.")
#answer: 1586300(Correct)

#pt 2
ribbon_sum = 0
for present in edit_txt:
    if(present != ""):
        dims = present.split("x")
        dims[0] = int(dims[0])
        dims[1] = int(dims[1])
        dims[2] = int(dims[2])
        ribbon_sum += (dims[0] * dims[1] * dims[2])
        if dims[0] >= dims[1] and dims[0] >= dims[2]:
            ribbon_sum += 2 * (dims[1] + dims[2])
        elif dims[1] >= dims[0] and dims[1] >= dims[2]:
            ribbon_sum += 2 * (dims[0] + dims[2])
        else:
            ribbon_sum += 2 *(dims[0] + dims[1])
print("The length of ribbon needed: {} feet".format(ribbon_sum))
#answer: 3737498 feet(correct)