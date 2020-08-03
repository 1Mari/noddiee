def five_num_summary(items):
    dictionary = {'max':0, 'median':0, 'min':0, 'q1':0, 'q3':0}
    dictionary['max'] = np.max(items).round(2)
    dictionary['median'] = np.median(items).round(2)
    dictionary['min'] = np.min(items).round(2)
    dictionary['q1'] = np.percentile(items, 25).round(2)
    dictionary['q3'] = np.percentile(items, 75).round(2)
    return dictionary
