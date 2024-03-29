import json
import matplotlib.pyplot as plt 

from eurito_indicators import PROJECT_DIR

FIG_PATH = f"{PROJECT_DIR}/outputs/figures"

def save_matplot(name, path=FIG_PATH):
    plt.tight_layout()
    plt.savefig(path+f"/{name}.png", dpi=1000)

def save_lookup(file, name):
    with open(f"{PROJECT_DIR}/inputs/data/{name}.json", 'w') as outfile:
        json.dump(file,outfile)

def clean_table(table, columns, clean_lookup):
    t = table.copy()
    for c in columns:
        t[f"{c}_clean"] = t[c].map(clean_lookup)
    return t