with open('summary_01.txt', 'r') as f:
    counter = 0
    results = {
        'ping' : 0.0,
        'download' : 0.0,
        'upload' : 0.0
    }
    for i, line in enumerate(f):
        if i > 2:
            elements = line.strip('\n').split('\t')
            results['ping'] += float(elements[1])
            results['download'] += float(elements[2])
            results['upload'] += float(elements[3])
            # print(results['ping'], results['download'], results['upload'])
            # exit()
        counter += 1
    
    print(f'Results: \n\n \
    Ping: {results["ping"] / counter}\n \
    Download: {results["download"] / counter}\n \
    Upload: {results["upload"] / counter}\n\n \
    Anzahl der Messungen: {counter} \
    ')