def convert_conllu_to_text_file(input_file, output_file, data_list_name):
    data_list = [[]]
    with open(input_file, "r") as f:
        for l in f:
            if not l.startswith("#"):
                if l.strip()=="":
                    if len(data_list[-1])>0:
                        data_list.append([])
                else:
                    row = l.split("\t")
                    if not "-" in row[0]:
                      data_list[-1].append(row[1])

    data_list.pop()

    data_rows = [ " ".join(row) for row in data_list ]
    data_text = "\n".join(data_rows)
    with open(output_file, 'w') as f:
        f.write(data_text)

    globals()[data_list_name] = data_list
