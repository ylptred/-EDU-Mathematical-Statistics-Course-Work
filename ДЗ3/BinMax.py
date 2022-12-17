n = 87
def Opt(ress):
    list = []
    for selection in ress:
        list.append(np.mean(selection)/n)
    return list
