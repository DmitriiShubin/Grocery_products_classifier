#imports
from functions.Model_serving import *
from functions.Text_preprocessing import *
from testing.CPU_test_config import *

#measure the cpu time
from time import time

def Run_CPU_test(model,
                 test_data_name,
                 product_data_name,
                 split_list):
    """
    input: model - method for calling the prediction function
    input: test_data_name - string, name of the test data, including path
    input: product_data_name - string, name of the product data, including path
    input: split_list - list[1,...] - list of integers

    outpur: integer, optimal number of splits

    """

    test_data = pd.read_csv(test_data_name).values.tolist()
    data_length = len(pd.read_csv(product_data_name,header=None).values.tolist())


    test_time = list()

    for ind,i in enumerate(split_list):

        if i >= data_length:
            break

        model.set_n_splits(i)

        start = time()
        for sample in test_data:
            model.predict(sample[0])

        end = time()

        test_time.append(end - start)

        print('Current number of splits: ',i)

    return split_list[test_time == min(test_time)]



if __name__ == '__main__':

    print(

        'Minimum computation time was reached using '+

        str(
        Run_CPU_test(
        model = Model(model_name=MDOEL_NAME,
                      product_names=DATA_NAME,
                      text_cleaning=text_cleaning(),
                      n_splits=3),

        test_data_name=TEST_DATA,
        product_data_name = DATA_NAME,
        split_list = SPLIT_LIST
        )
        )
        +' split(s)'
    )





