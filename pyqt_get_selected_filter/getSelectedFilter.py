def getSelectedFilter(lst):
    selectedFilterExtensionsLst = list(map(lambda x: '*' + x, lst))
    selectedFilterExtensionsStr = ''
    for ext in selectedFilterExtensionsLst:
        selectedFilterExtensionsStr += ext + ' '
    selectedFilterExtensionsStr = f'({selectedFilterExtensionsStr.rstrip()})'
    return selectedFilterExtensionsStr