# 階層が深いJsonData を引っ張り出すプログラム
def search(arg, cond):
    res = []
    if cond(arg):
        res.append(arg)
    if isinstance(arg, list):
        for item in arg:
            res += search(item, cond)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += search(value, cond)
    return res

def has_start_key(arg):
    if isinstance(arg, dict):
        return arg.keys() == {"pred","obj"}

def get_start(arg):
    return search(arg, has_start_key)

# 値の
def get_value(key, list_datas):
    all_value = []
    for data in list_datas:
        pred = data['pred']['value']
        obj = data['obj']['value']
        all_value.append([key, pred, obj])
    return all_value