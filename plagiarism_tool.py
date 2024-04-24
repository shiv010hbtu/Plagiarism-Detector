def tool(sent1 = 'Sample Text',sent2 = 'sample text'):
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    import nltk
    from nltk.stem import PorterStemmer , LancasterStemmer
    from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
    import pandas as pd
    import numpy as np

    def cosine_similarity(a1,a2):
        from math import sqrt
        sum = 0
        sum1 = 0
        sum2 = 0
        for i , j in zip(a1,a2):
            sum += i*j
            sum1 += i*i
            sum2 += j*j

        cs = sum / (sqrt(sum1) * sqrt(sum2))
        return cs

    x = stopwords.words('english')

    if sent1 == '' and sent2 == '':
        sent1 = 'Sample Text'
        sent2 = 'sample text'
        

    # # sent1 = input("Enter the first sentence : ").split()
    # sent1 = sent1.split()
    # # Instead of splitting the text we can use word tokenize
    
    
    from nltk.tokenize import word_tokenize
    sent1 = word_tokenize(sent1)
    
    
    sent1 = [b.lower() for b in sent1]

    # sent2 = input("Enter the second sentence : ").split()
    # sent2 = sent2.split()
    
    sent2 = word_tokenize(sent2)
    sent2 = [b.lower() for b in sent2]

    # StopWord removal
    word1 = [ww for ww in sent1 if ww not in x]
    word2 = [ww for ww in sent2 if ww not in x]

    # # Stemming for smooth and better performance
    # stemmer = PorterStemmer()
    # word1 = [stemmer.stem(word) for word in word1]
    # word2 = [stemmer.stem(word) for word in word2]
    
    
    # Instead of porter stemmer we can use Lancaster Stemmer as it can be more accurate
    # Stemming for smooth and better performance
    stemmer = LancasterStemmer()
    word1 = [stemmer.stem(word) for word in word1]
    word2 = [stemmer.stem(word) for word in word2]
    

    # Joining the sentence back
    word1 = ' '.join(word1)
    word2 = ' '.join(word2)


    document = [word1,word2]


    vectorizer = CountVectorizer(binary = False)
    # vectorizer = TfidfVectorizer(ngram_range=(1,2))
    bow_model = vectorizer.fit_transform(document)
    row = bow_model.toarray()

    row = bow_model.toarray().T
    column = vectorizer.get_feature_names_out()


    y={}

    for i in range(len(column)):
        y[column[i]] = row[i]

    row = bow_model.toarray()       
    q1 = cosine_similarity(row[0], row[1])
    
    ret_data = [q1,y]
    
    return ret_data

