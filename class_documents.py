from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg
from nltk.corpus import brown

class Documents():

    def __init__(self):
        self.filenames = brown.fileids()
        #pre-processing the data for a filtered list of purely words

    def pre_process(self, token_list):
        token_list = [token.lower() for token in token_list]
        return token_list

    def get_documents(self, n):

        n_fn = self.filenames[:n]
        doc_list = [brown.words(x) for x in n_fn]
        bags = [self.pre_process(doc) for doc in doc_list]
        
        return bags

    #creating sparse representation of the bags of words\n",
    def make_dict(self, bag_list):
        
        docdicts=[] 
        
        for bag in bag_list:
            docdicts.append(self.compose_dic(bag))
                
        return docdicts

    def compose_dic(self, bag):
        
        all_freq = {}
        
        for item in bag:
            if item in all_freq:
                all_freq[item] += 1
            else:
                all_freq[item] = 1
                
        return all_freq

    def join_docs(self, doc_a,doc_b):
        pass

    # The function is to make the dense vectors from dictionary
    def make_matrix(self, list_of_dicts):
        
        #first of all make a list of all of the features that occur in any document - these will be the dimensions of the matrix
        allfeatures = {}
        
        for docdict in list_of_dicts:
    #         print('docdict',docdict)
            for feat in docdict.keys():
    #             print('feat',feat)
                allfeatures[feat]=1
    #             print('allfeatures',allfeatures)
        dimensions=list(allfeatures.keys())
        
        #don't strictly need to sort it - but it is good practise to make sure it is reproducible
        so=sorted(dimensions)
        matrix=[]

        #each row in the matrix will be one of the dimensions\n",
        for dimension in dimensions:
            row = []
            #look up the appropriate value for each document
            for docdict in list_of_dicts:
                row.append(docdict.get(dimension,0)) #this will append the document's value if present, 0 otherwise
            matrix.append(row)
            
        return matrix

    ## it might be useful to be able to transpose a matrix so we can compare documents\n",
    def transpose(self, matrix):
        
        transposed = []
        
        for i in range(0,len(matrix[0])):
            transposed.append([row[i] for row in matrix])
            
        return transposed
