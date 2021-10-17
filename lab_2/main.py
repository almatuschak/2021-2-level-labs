"""
Lab 2
Language classification
"""

from lab_1.main import tokenize, remove_stop_words
import math

# 4
def get_freq_dict(tokens: list) -> dict or None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """

    if not isinstance(tokens, list):
        return None

    freq_dict = {}
    for word in tokens:
        if isinstance(word, str):
            freq_dict[word] = round(tokens.count(word)/len(tokens), 5)
        else:
            return None

    return freq_dict



def get_language_profiles(texts_corpus: list, language_labels: list) -> dict or None:
    """
    Computes language profiles for a collection of texts
        and adds appropriate language label for each text
    :param texts_corpus: a list of given texts
    :param language_labels: a list of given language labels
    :return: a dictionary of dictionaries - language profiles
    """

    if not isinstance(texts_corpus, list) or not isinstance(language_labels, list):
        return None
    for label in language_labels:
        if not label:
            return None
    for label in texts_corpus:
        if not label:
            return None

    language_profiles = {}
    for label in range(len(language_labels)):
        language_profiles[language_labels[label]] = get_freq_dict(texts_corpus[label])

    return language_profiles



def get_language_features(language_profiles: dict) -> list or None:
    """
    Gets all unique words from language profiles
        and sorts them in alphabetical order
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if not isinstance(language_profiles, dict) or not language_profiles:
        return None

    features = []
    for lang_profile in language_profiles.values():
        for word in lang_profile.keys():
            features.append(word)
    return sorted(features)



def get_text_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    if not isinstance(original_text, list) or not isinstance(language_profiles, dict) \
            or not language_profiles:
        return None

    features = get_language_features(language_profiles)
    vector_list = []
    for word in features:
        if word in original_text:
            for lang_profile in language_profiles.values():
                if word in lang_profile.keys():
                    vector_list.append(lang_profile[word])
        else:
            vector_list.append(0)
    return vector_list


# 6
def calculate_distance(unknown_text_vector: list, known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    if not isinstance(unknown_text_vector, list) or not \
            isinstance(known_text_vector, list) or:
        return None
    for i in unknown_text_vector:
        if not isinstance(i, float):
            return None
        if not isinstance(i, float):
            return None


    for i in range(len(unknown_text_vector)):
        distance = math.sqrt((unknown_text_vector[i] - known_text_vector[i])**2)
    return distance


def predict_language_score(unknown_text_vector: list, known_text_vectors: list,
                           language_labels: list) -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
    :param unknown_text_vector: vector for unknown text
    :param known_text_vectors: a list of vectors for known texts
    :param language_labels: language labels for each known text
    """
    pass


# 8
def calculate_distance_manhattan(unknown_text_vector: list,
                                 known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using manhattan metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vector: vector for known text
    """
    pass


def predict_language_knn(unknown_text_vector: list, known_text_vectors: list,
                         language_labels: list, k=1, metric='manhattan') -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
        using knn based algorithm and specific metric
    :param unknown_text_vector: vector for unknown text
    :param known_text_vectors: a list of vectors for known texts
    :param language_labels: language labels for each known text
    :param k: the number of neighbors to choose label from
    :param metric: specific metric to use while calculating distance
    """
    pass


# 10 implementation
def get_sparse_vector(original_text: list, language_profiles: dict) -> list or None:
    """
    Builds a sparse vector representation of a given text
        using dictionary with language profiles
    :param original_text: any tokenized text
    :param language_profiles: a dictionary of dictionaries - language profiles
    """
    pass


def calculate_distance_sparse(unknown_text_vector: list,
                              known_text_vector: list) -> float or None:
    """
    Calculates distance between two vectors using euclid metric
    :param unknown_text_vector: sparse vector for unknown text
    :param known_text_vector: sparse vector for known text
    """
    pass


def predict_language_knn_sparse(unknown_text_vector: list, known_text_vectors: list,
                                language_labels: list, k=1) -> [str, int] or None:
    """
    Predicts unknown text label and its distance to the closest known text
        using knn based algorithm
    :param unknown_text_vector: sparse vector for unknown text
    :param known_text_vectors: a list of sparse vectors for known texts
    :param language_labels: language labels for each known text
    :param k: the number of neighbors to choose label from
    """
    pass
