def MaxMethod(ress):
    list = []
    for selection in ress:
        list.append(np.sqrt((np.mean(selection))/(3)))
    return list




