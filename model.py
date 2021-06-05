import tensorflow as tf
import numpy as np
from os import system

EMBEDDING_DIM = 512



def transform(txt):
  return np.asarray([ord(c) for c in txt if ord(c) < 255], dtype=np.int32)


def lstm_model(seq_len=100, batch_size=None, stateful=True):
  source = tf.keras.Input(
      name='seed', shape=(seq_len,), batch_size=batch_size, dtype=tf.int32)

  embedding = tf.keras.layers.Embedding(input_dim=256, output_dim=EMBEDDING_DIM)(source)
  lstm_1 = tf.keras.layers.LSTM(EMBEDDING_DIM, stateful=stateful, return_sequences=True)(embedding)
  lstm_2 = tf.keras.layers.LSTM(EMBEDDING_DIM, stateful=stateful, return_sequences=True)(lstm_1)
  predicted_char = tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(256, activation='softmax'))(lstm_2)
  return tf.keras.Model(inputs=[source], outputs=[predicted_char])


def create_a_music_with_model(title, size):
  PREDICT_LEN = size

  seed = transform(title)
  seed = np.repeat(np.expand_dims(seed, 0), BATCH_SIZE, axis=0)

  prediction_model.reset_states()
  for i in range(len(title) - 1):
    prediction_model.predict(seed[:, i:i + 1])

  predictions = [seed[:, -1:]]
  for i in range(PREDICT_LEN):
    last_word = predictions[-1]
    next_probits = prediction_model.predict(last_word)[:, 0, :]
    
    next_idx = [
        np.random.choice(256, p=next_probits[i])
        for i in range(BATCH_SIZE)
    ]
    predictions.append(np.asarray(next_idx, dtype=np.int32))
    
  system('cls')
  for i in range(BATCH_SIZE):
    p = [predictions[j][i] for j in range(PREDICT_LEN)]
    generated = ''.join([chr(c) for c in p])  # Convert back to text

  return generated


BATCH_SIZE = 1
prediction_model = lstm_model(seq_len=1, batch_size=BATCH_SIZE, stateful=True)
prediction_model.load_weights('model/bard.h5')

if __name__ == '__main__':
  create_a_music_with_model('Yesterday', 800)