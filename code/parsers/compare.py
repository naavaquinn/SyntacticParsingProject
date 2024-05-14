def read_conllu_and_parse_gold_data(input_file, gold_data):
    with open(input_file, "r") as f:
        for l in f:
            if not l.startswith("#"):
                if l.strip()=="":
                    if len(gold_data[-1])>0:
                        gold_data.append([])
                else:
                    row = l.split("\t")
                    if not "-" in row[0]:
                        gold_data[-1].append([row[0], row[1], row[3], row[6], row[7]])

    gold_data.pop()
