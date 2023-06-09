from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16

model = VGG16()
model.summary()
image = load_img('data/mug.jpg', target_size=(224, 224))
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)
predicted = model.predict(image)
label = decode_predictions(predicted)
label = label[0][0]
print('%s (%.2f%%)' % (label[1], label[2]*100))