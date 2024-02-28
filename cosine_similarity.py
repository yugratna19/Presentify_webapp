def cosine_similarity(data_dict, image_caption_list):
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np

    def get_cosine_similarity(sentence1, sentence2):
        vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
        vectors = vectorizer.toarray()
        return cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    bullets = []

    captions = []

    for key in data_dict:
        bullets.append(data_dict[key])
    for dicts in image_caption_list:
        captions.append(dicts['caption'])

    similarity_dict = {}

    titles = ['Introduction', 'Literature Review',
              'Methodology', 'Results', 'Conclusion']
    data_dict = {}
    for title in titles:
        data_dict[title] = bullets[titles.index(title)]

    for i in range(len(data_dict)):
        similarity_list = []
        for j in range(len(captions)):
            similarity = get_cosine_similarity(data_dict[titles[i]], captions[j])
            similarity_list.append(similarity)
        similarity_dict[titles[i]] = similarity_list

    # create a dictionary that stores maximum value and its index of each key
    max_index_list = []
    for key in similarity_dict:
        similarity_dict_max = {}
        similarity_dict_max[key] = max(similarity_dict[key])
        similarity_dict_max['Index'] = np.argmax(similarity_dict[key])
        max_index_list.append(similarity_dict_max)

    # Iterate through the data to find the highest similarity score for each index
    filtered_data = {}

    for entry in max_index_list:
        index = entry['Index']
        if index not in filtered_data or entry[next(iter(entry))] > filtered_data[index][next(iter(filtered_data[index]))]:
            filtered_data[index] = entry
    filtered_list = list(filtered_data.values())
    print(max_index_list)
    return filtered_list
