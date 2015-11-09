import csv
import numpy as np

from sklearn import decomposition

def uniquify_each_column(data):
    data = data.T #transpose
    all_cats = []
    
    for cIdx, col in enumerate(data): #walk data by column
        d = {}
        num = 0
        for rIdx, row in enumerate(col):
            if row not in d:
                d[row] = num
                num += 1
            data[cIdx][rIdx] = d[row]
        all_cats.append(d)
    return all_cats, data.T

#this means we are running the code from the command line
#you can run the code by type "python parse.py"
if __name__ == "__main__":     
    data = []
    labels = ""

    with open('cleaned.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for idx, line in enumerate(reader):
            if idx == 0: #if its the first row
                    labels = line
            else:
                    data.append(line) #create a list of list


    data = np.asarray(data)
    all_cats, data = uniquify_each_column(data)
    data = data.astype(np.float32)

    pca = decomposition.PCA(n_components = 20)
    data = pca.fit_transform(data)
    print data.shape
    print pca.explained_variance_ratio_
    print pca.components_
