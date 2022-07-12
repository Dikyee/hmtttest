import yaml

def read_yaml(file):
    arr = []
    file = f"./data/{file}"
    with open(file,"r",encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
        return arr
