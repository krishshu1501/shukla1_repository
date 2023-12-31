# -*- coding: utf-8 -*-
"""assignement_s_n_fake_news_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MZF5vvWUzR63uOu2VwckEmxT3JIsA4c7
"""

from google.colab import files


uploaded = files.upload()

import pandas as pd
import io

dataset_one = pd.read_csv(io.BytesIO(uploaded['dataset (1).csv']))
print(dataset_one)

"""## Import Modules"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
import nltk
import warnings
# %matplotlib inline

warnings.filterwarnings('ignore')

"""pandas - used to perform data manipulation and analysis

numpy - used to perform a wide variety of mathematical operations on arrays

matplotlib - used for data visualization and graphical plotting

seaborn - built on top of matplotlib with similar functionalities

re – used as a regular expression to find particular patterns and process it

nltk –  a natural language processing toolkit module

warnings - to manipulate warnings details

%matplotlib inline - to enable the inline plotting

filterwarnings('ignore') is to ignore the warnings thrown by the modules (gives clean results)

## Loading the Dataset
"""

#create a copy of the original dataset to work on and retain the original dataset
df = dataset_one.copy()

df.head()

"""We can see the top 5 samples from the data

Important information is in the 'content_text' column and the 'class' column

## Let us see the datatypes and no. of samples in the dataframe
"""

df.info()

"""## Data Preprocessing"""

#checking for null values in the dataframe
df.isnull().sum()

# creating a new dataset df1 with rows and columns with 'en' (english) as language
df1 = df[df['lang']=='en']

df1.head()

df1.info()

#checking again for null values in the datatframe df1
df1.isnull().sum()

# creating dataframe only with features required for classification
df_new = df1[['verifiedby', 'country', 'title', 'content_text', 'published_date', 'ref_source', 'category', 'lang', 'class']]

df_new.head()

# checking values in the class column
df_new['class'].value_counts()

# lowercasing the values in class column
df_new['class'] = df_new['class'].apply(lambda x: x.lower())

df_new.head()

# creating datadrame classification_df by filtering rows and coloumns having true or false values under class column
classification_df = df_new.loc[df_new['class'].isin(['true', 'false'])]

classification_df.head()

"""## Visualization"""

from matplotlib import pyplot as plt
import seaborn as sns
_df_0.groupby('verifiedby').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
_df_1.groupby('country').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
_df_2.groupby('title').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['country'].value_counts()
    for x_label, grp in _df_8.groupby('verifiedby')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('verifiedby')
_ = plt.ylabel('country')

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['title'].value_counts()
    for x_label, grp in _df_9.groupby('country')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('country')
_ = plt.ylabel('title')

# dealing with missing values in the country column
column_with_missing_values = 'country'
missing_indices = classification_df[classification_df[column_with_missing_values].isnull()].index
unique_categories = classification_df[column_with_missing_values].unique()
classification_df.loc[missing_indices, column_with_missing_values] = np.random.choice(unique_categories, len(missing_indices))
print(classification_df[column_with_missing_values].isnull().sum())

classification_df.isnull().sum()

# dealing with missing values in the category column
column_with_missing_values_one = 'category'
missing_indices = classification_df[classification_df[column_with_missing_values_one].isnull()].index
unique_categories = classification_df[column_with_missing_values_one].unique()
classification_df.loc[missing_indices, column_with_missing_values_one] = np.random.choice(unique_categories, len(missing_indices))

classification_df.head()

# checking for null values
classification_df.isnull().sum()

# dropping the existing null values in the classification_df dataframe
classification_df.dropna(inplace=True)

#checking for null values
classification_df.isnull().sum()

classification_df.head()

# normalizing published_date feature to get same date format for all values in the published_date column
classification_df['published_date'] =  pd.to_datetime(classification_df['published_date']).dt.normalize()

classification_df.head()

classification_df.info()

#remove special characters and punctuation
classification_df['clean_news'] = classification_df['content_text'].str.lower()
classification_df['clean_news']

"""str.lower() - converts all characters to lower case"""

classification_df.shape

classification_df.reset_index(inplace = True)

classification_df.head()

classification_df.drop('index', axis = 1, inplace = True)

classification_df.head()

## converting true and false values to numbers, true = 1 and false = 0 and creating column label with these values

classification_df['label'] = classification_df['class'].apply(lambda x:1 if x == 'true' else 0)

classification_df.head()

classification_df['label'].value_counts()

# dropping class column
classification_df.drop('class', axis = 1, inplace = True)

classification_df.head()

#cl_df = classification_df.sample(frac=1)
#cl_df.reset_index(inplace=True)
#cl_df.drop(["index"], axis=1, inplace=True)

# creating count plot for the class1 colulmn to visualize category count
sns.countplot(data=cl_df,
              x='label',
              order=cl_df['label'].value_counts().index)

"""Now we proceed in removing the punctuations and special characters


"""

cl_df['clean_news'] = cl_df['clean_news'].str.replace('[^A-Za-z0-9\s]', '')
cl_df['clean_news'] = cl_df['clean_news'].str.replace('\n', '')
cl_df['clean_news'] = cl_df['clean_news'].str.replace('\s+', ' ')
cl_df['clean_news']

"""All special characters and punctuations are removed

Escape characters are removed

Extra spaces are removed
"""

import nltk
nltk.download('stopwords')

# remove stopwords
from nltk.corpus import stopwords
stop = stopwords.words('english')
cl_df['clean_news'] = cl_df['clean_news'].apply(lambda x: " ".join([word for word in x.split() if word not in stop]))
cl_df.head()

"""Stop words are meaningless information, removing them simplifies the text data for good feature extraction

Stop words are removed from text by splitting the original text and comparing with the STOPWORDS list

## Exploratory Data Analysis
"""

# visualize the frequent words
all_words = " ".join([sentence for sentence in cl_df['clean_news']])

wordcloud = WordCloud(width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

# plot the graph
plt.figure(figsize=(13, 9), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

"""Concatenation of all the sentences from clean_news column

The most frequent words are larger and less frequent words are smaller

Visualization of frequent words from true and false news
"""

all_words = " ".join([sentence for sentence in cl_df['clean_news'][cl_df['label']==0]])

wordcloud = WordCloud(width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

# plot the graph
plt.figure(figsize=(13, 9), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

"""Concatenation of sentences of genuine news only

Visualization of most frequent words of false news
"""

all_words = " ".join([sentence for sentence in cl_df['clean_news'][cl_df['label']==1]])

wordcloud = WordCloud(width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

# plot the graph
plt.figure(figsize=(13, 9), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

"""Concatenation of sentences of genuine news only

Visualization of most frequent words of true news
"""

from sklearn.feature_extraction.text import CountVectorizer


def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1],
                        reverse=True)
    return words_freq[:n]


common_words = get_top_n_words(cl_df['clean_news'], 20)
cl_df1 = pd.DataFrame(common_words, columns=['Review', 'count'])

cl_df1.groupby('Review').sum()['count'].sort_values(ascending=False).plot(
    kind='bar',
    figsize=(10, 6),
    xlabel="Top Words",
    ylabel="Count",
    title="Bar Chart of Top Words Frequency"
)

"""## Create Word Embeddings

"""

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

"""Tokenizer - used for loading the text and convert them into a token

pad_sequences - used for equal distribution of words in sentences filling the remaining spaces with zeros
"""

# tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(cl_df['clean_news'])
word_index = tokenizer.word_index
vocab_size = len(word_index)
vocab_size

"""Returns all unique words as tokens

vocab_size returns the total number of unique words from the data
"""

# padding data
sequences = tokenizer.texts_to_sequences(cl_df['clean_news'])
padded_seq = pad_sequences(sequences, maxlen=500, padding='post', truncating='post')

"""Padding the data equalizes the length of all sentences


"""

#Downloading Glove Embedding File
!wget http://nlp.stanford.edu/data/glove.6B.zip

!apt install unzip
!unzip "glove.6B.zip.3"

# create embedding index
embedding_index = {}
with open('glove.6B.100d.txt', encoding='utf-8') as f:
    for line in f:
         values = line.split()
         word = values[0]
         coefs = np.asarray(values[1:], dtype='float32')
         embedding_index[word] = coefs

"""Glove embedding dictionary contains vectors for words in 100 dimensions, mainly all words from the dictionary"""

# create embedding matrix
embedding_matrix = np.zeros((vocab_size+1, 100))
for word, i in word_index.items():
    embedding_vector = embedding_index.get(word)
    if embedding_vector is not None:
         embedding_matrix[i] = embedding_vector

embedding_matrix[1]

"""Vectors in the embedding matrix as float32 data type

The 100 values represents a single word

## Input Split
"""

padded_seq[1]

"""Visualization of word index from the padded sequence

Good example viewing a padded sentence, remaining spaces filled with zero to match the max length

## Now we proceed in splitting the data for training
"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(padded_seq, cl_df['label'], test_size=0.20, random_state=42, stratify=cl_df['label'])

"""80% data split for training and remaining 20% for testing

Stratify will equally distribute the samples for train and test

## SMOTE Analysis for Creating Balanced Label
"""

from imblearn.over_sampling import SMOTE
smt = SMOTE()
x_train_sm, y_train_sm = smt.fit_resample(x_train, y_train)

from imblearn.over_sampling import SMOTE
smt = SMOTE()
x_test_sm, y_test_sm = smt.fit_resample(x_test, y_test)

"""## Model Training

"""

from keras.layers import LSTM, Dropout, Dense, Embedding
from keras import Sequential

# model = Sequential([
#     Embedding(vocab_size+1, 100, weights=[embedding_matrix], trainable=False),
#     Dropout(0.2),
#     LSTM(128, return_sequences=True),
#     LSTM(128),
#     Dropout(0.2),
#     Dense(512),
#     Dropout(0.2),
#     Dense(256),
#     Dense(1, activation='sigmoid')
# ])

model = Sequential([
    Embedding(vocab_size+1, 100, weights=[embedding_matrix], trainable=False),
    Dropout(0.2),
    LSTM(128),
    Dropout(0.2),
    Dense(256),
    Dense(1, activation='sigmoid')
])

"""Embedding - maps the word index to the corresponding vector representation

LSTM - process sequence of data

Dense - single dimension linear layer

Use Dropout if augmentation was not applied on the data to avoid over fitting

activation='sigmoid' - used for binary classification
"""

model.compile(loss='binary_crossentropy', optimizer='adam', metrics='accuracy')
model.summary()

"""model.compile() - compilation of the model

optimizer='adam' - automatically adjust the learning rate for the model over the no. of epochs

loss='binary_crossentropy' - loss function for binary outputs
"""

# train the model
history = model.fit(x_train, y_train, epochs=10, batch_size=256, validation_data=(x_test, y_test))

"""Set the no. of epochs and batch size according to the hardware specifications

Training accuracy and validation accuracy increases each iteration

Training loss and validation loss decreases each iteration

The maximum validation accuracy is 98.37

## Now we visualize the results through a plot graph
"""

# visualize the results
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['Train', 'Test'])
plt.show()

"""## Final Thoughts

Training the model by increasing the no. of epochs can give better and more accurate results.

Processing large amount of data can take a lot of time and system resource.

Basic deep learning model trained in a small neural network, adding new layers may improve the results.

We trained a LSTM model to predict the fake news and other models like GRU, Bi-LSTM, Transformers (BERT, T5, Xlnet, GPT etc.) can be used to improve the performance of the model.
"""

