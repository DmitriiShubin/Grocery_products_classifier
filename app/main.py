#imports
from functions.Text_preprocessing import *
from functions.Model_serving import *



logging.debug('Upploading the model')
#upload the model
model = Model(model_name=MDOEL_NAME,
                     product_names=DATA_NAME,
                     text_cleaning=text_cleaning(),
                     n_splits=3)


logging.debug('The model is upload')

#launch fast api
app = FastAPI()


#call prediction function
@app.get("/items/{item_id}")
def read_item(q: str = None):
    """
    input: q - string
    output: result - string
    """

    logging.debug('Making prediction')
    start = time.time()

    logging.debug('Execution time :'+str(time.time()-start))

    #make prediction
    result = model.predict(q)

    logging.info(q + ', '+result)

    return 'Product category is: ' + result



