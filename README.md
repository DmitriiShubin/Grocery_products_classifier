# General info
The project includes scalable, easy for deploy retail goods categories classifier based on pre-trained Word2Vec model.


The overall project includes several folders and files:

- data: include lists of retail goods and test lists for CPU/memory optimization
- functions:
1. Model_serving.py - class for loading, cashing of the model and category list
2. Text_preprocessing.py - class for text preprocessing (lower casing + removing of stop words)
- logs - includes debugging logs
- models - the folder for storing pre-trained LexVec model
- testing - includes automatic selection of the batch size
- config.py -global config file
- main.py - main function for calling Fast API backend

Prediction of the product category is based on the closest nearest neighbor (euclidian distance). 
In general, the algorithm works as follows:

1. map original product category list into several batches
2. iterate over all batches, find minimum elements inside these butches
3. calculate a minimum between several butches

Due to this approach, the model could be expanded to a wide range of product list (for now 5 categories are running) without significant degradation of the performance because of highly optimized inference pipeline.

#  About Word2Vec:

The idea behind the Word2Vec model is pretty straightforward:
The model is trying to represent the data as vectors in a latent space, i.e. show not only a presence of words but some internal dependencies between words as well.

In order to build a classifier, based on the Word2Vec model, it needs to apply a vector transform to all classed represented in the dataset and on input data and find the nearest vector in represented (euclidean / cosine distance).

# Features:
1) Could be simply expanded both to a larger catalog of retail goods (vertical scaling) and for more users (horizontal scaling)
2) The flexibility of tuning the trade-off between CPU time and memory allocation
3) A semi-automatic search of the optimal batch size
4) Logging for debugging
5) Implemented using FastApi -> fast framework with automatic generated API
6) Deployed using docker
7) Aggegation of history of requiests


# How to launch the solution:

1. install docker, for ubuntu: sudo apt install docker.io
2. open project folder (the folder that includes a Dockerfile)
3. run: sudo docker build --name grocery .
4. wait for a moment. It's going to take some time because of model size 
5. run: sudo docker run  -d --name mygrocery -p 80:80 grocery
6. open ./app/MainPage.html. it should the following message: Product category prediction form
7. Insert your string, push predict button


# How to get model API:
1. launch the docker container
2. open http://127.0.0.1/docs in the browser




#  CPU tests:
In order to find an optimal batch size, the code is running several trials and measure a CPU time.
The number of optimal splits of the data is printed on a screen and could set in cofig.py


# History of inputs over time:

1. launch the docker container
2. open root project folder
3. open terminal, run: sudo docker cp mygrocery:/app/logs . 
