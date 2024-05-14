def read_and_parse_stanza_data(stanza_file):
    stanza_data = []

    for file in stanza_files:
        data = [[]]

        with open(file, "r") as f:
            for l in f:
                if not l.startswith("#"):
                    if l.strip() == "":
                        if len(data[-1]) > 0:
                            data.append([])  
                    else:
                        row = l.split("\t")
                        if not "-" in row[0]:
                            data[-1].append([row[0], row[1], row[3], row[6], row[7]])

        data.pop()
        stanza_data.append(data)

    return stanza_data
