# Análisis de sentimientos
import numpy as np

def generate_list_of_words(strings): #trasforma el tweet en una lista de palabras
    strings = strings.replace("!", "").replace(",", "").replace(".", ""). replace("()", "").replace(")", "").lower().split()
    return strings

def generate_vector_w(words_list, tweet_list): #w_vector es el número de elementos que existen en el tweet de una arrat ya definido
    pass
    w_vector = np.zeros(len(words_list))
    
    for element in range(len(words_list)):
        if words_list[element] in tweet_list:
            w_vector[element]+= 1
    
    return w_vector
            
def generate_vector_s(tweet_list): # s_vector es nuestro vector de sentimientos contabilizando el número de palabras positivas, negativas y neutras de nuestra lista de palabras
    positive = ['excelente', 'gran', 'positivo']
    neutral = ['pérdida']
    negative = ['muerte', 'luto']
    s_vector = np.zeros(3)
    
    for i in range(len(tweet_list)):
        if tweet_list[i] in positive:
            s_vector[0] += 1
        elif tweet_list[i] in negative:
            s_vector[2] += 1
        elif tweet_list[i] in neutral:
            s_vector[1] += 1

    return s_vector
    
def mean_w_vector(w_vector):
    return round(np.mean(w_vector), 2)

    
if __name__ == '__main__':

    tweet_1 = "Gran mexicano y excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!"

    tweet_2 = "Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt."

    tweet_3 = "Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"

    tweet_4 = "Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!"

    words_to_find = "muerte, pérdida, luto, excelente, gran y positivo"
    words_to_find = generate_list_of_words(words_to_find)
    
    tweet_1 = generate_list_of_words(tweet_1) 
    
    w_vector_tweet_1 = generate_vector_w(words_to_find, tweet_1) 
    
    s_vector_tweet_1 = generate_vector_s(tweet_1) 

    w_vector_mean_tweet_1 = mean_w_vector(w_vector_tweet_1)
    



