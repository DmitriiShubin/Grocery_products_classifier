#imports
from config import *
from models.lexvec.model import Model as lexvec_model

class Model:

    def __init__(self,
                      model_name,
                      product_names,
                      text_cleaning,
                      n_splits):

        """
        input: model - method for calling the prediction function
        input: test_data_name - string, name of the test data, including path
        input: product_data_name - string, name of the product data, including path
        input: split_list - list[1,...] - list of integers

        """

        self.__product_names = product_names

        #class for text preprocessing
        self.__text_cleaning = text_cleaning

        #load the model
        self.__model = lexvec_model(model_name)

        #number of splits of the vector during vector distance calculation
        self.__n_splits = n_splits

        #load data from grocery list
        self.load_product_data()

    # make prediction
    def predict(self, data):
        """
        input: data - string for prediction
        output: min_key - predicted class
        """

        # apply text preprocessing
        data = self.__text_cleaning.preprocessing_text(data)

        #get word2vec
        data = self.__model.word_rep(data)

        #map the inpur dctionary
        mapping = dict()
        for ind,i in enumerate(self.__categories_vector):
            distance = np.sum(np.power((i - data),2),axis=1)
            mapping[self.__categories_name[ind][np.argmin(distance)][0]] = np.min(distance)

        #reduce
        min = np.inf
        min_key = None
        for i in mapping.keys():
            if mapping[i] < min:
                min_key = i
                min = mapping[i]

        if min_key is not None:
            return min_key
        else:
            return 'N/A'

    def set_n_splits(self,n_splits):
        """

        input: n_splits - interger, number of splits of the group list
        """
        self.__n_splits = n_splits
        #update the data according to the new shape of the list
        self.load_product_data()

        return 0

    def load_product_data(self):

        """

        """

        logging.debug('Upploading the product list')

        self.__categories_name = pd.read_csv(self.__product_names, header=None).values
        self.__categories_vector = np.array([self.__model.word_rep(i[0]) for i in self.__categories_name]).tolist()

        self.__categories_vector = np.array_split(self.__categories_vector, self.__n_splits)
        self.__categories_name = np.array_split(self.__categories_name, self.__n_splits)

        logging.debug('Product list is ready')

        return 0

