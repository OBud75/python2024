import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as tfhub


tf.experimental.numpy.experimental_enable_numpy_behavior()
embed_fn = tfhub.load(
    "https://www.kaggle.com/models/google/universal-sentence-encoder/TensorFlow2/universal-sentence-encoder/2")

def get_silimarity_score(embed_fn, text1, text2):
    """Calculate similarity score with the texts
    """
    encoded_text1 = embed_fn([text1])
    encoded_text2 = embed_fn([text2])
    return np.dot(encoded_text1, encoded_text2.T).T


class NaturalLanguageProcessing():
    """This is the main model of the application
    We use it to translate words into a vector
    """
    def __init__(self):
        """Initialisation
        Downloads google encoder if not found on the server
        """
        # Get google encoder
        file_name = "1fb57c3ffe1a38479233ee9853ddd7a8ac8a8c47.descriptor.txt"
        if not os.path.exists(os.path.join(os.path.abspath(__name__), file_name)):
            self.get_universal_encoder()

    def get_universal_encoder(self):
        """Creates the directory to cache the universal sentence encoder.
        """
        os.environ["TFHUB_CACHE_DIR"] = os.path.dirname(__name__)
        tfhub.load("https://tfhub.dev/google/universal-sentence-encoder/2")

    def embed_tensorflow(self):
        """Initialize the model with TensorFlow
        Train the model with the univeral sentence encoder

        Returns:
            Dict: Map of the words
        """
        with tf.Graph().as_default():
            text_input = tf.compat.v1.placeholder(dtype=tf.string, shape=[None])
            folder_name = '1fb57c3ffe1a38479233ee9853ddd7a8ac8a8c47'
            embed = tfhub.Module(os.path.join(os.path.dirname(__name__), folder_name))
            em_txt = embed(text_input)
            session = tf.compat.v1.train.MonitoredSession()
        return lambda x: session.run(em_txt, feed_dict={text_input: list(x)})

    def get_silimarity_score(self, text1, text2):
        """Calculate similarity score with the texts
        """
        embed_fn = self.embed_tensorflow()
        encoded_text1 = embed_fn([text1])
        encoded_text2 = embed_fn([text2])
        return np.dot(encoded_text1, encoded_text2.T).T
