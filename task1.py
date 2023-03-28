def gen_triangle(num):
    alt = 0
    for i in range(1,num+1):
        last_one = (str(num) + " ") * num
        middle = int((len(last_one)-1) / 2 - 1)
        num_of_space = middle - 1 - alt
        line = (" " * num_of_space)
        if i < 10:
            line += "     "
        string = (str(i) + " ") * i
        line += string
        print(line)
        alt += 1














prompt = int(input("how many rows:"))
gen_triangle(prompt)