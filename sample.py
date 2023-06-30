import re
txt_dir = "training.txt"
 # dictionary for one row keyboard
one_row = {"q": 1, "a": 1, "z": 1, 
              "w": 2, "s": 2, "x": 2,
              "e": 3, "d": 3, "c": 3,
              "r": 4, "f": 4, "v": 4,
              "t": 5, "g": 5, "b": 5,
              "y": 6, "h": 6, "n": 6,
              "u": 7, "j": 7, "m": 7,
              "i": 8, "k": 8,
              "o": 9, "l": 9,
              "p": 0} 
with open(txt_dir, "r", encoding='utf-8') as f:
    output = list([])
    for line in f:
        w_list = line.split()
        for w in w_list:
            w = re.sub(r"[^a-zA-Z]", "", w)
            word_to_num = ""
            for c in w:
                try:
                    word_to_num += str(one_row[c.lower()])
                except KeyError:
                    break
            if len(word_to_num) > 0:
                output.append(w+"/"+word_to_num)
    # print(output)
with open("output4.txt", "w") as f2:
    for line in output:
        f2.write(line+" ")
            
        

    
