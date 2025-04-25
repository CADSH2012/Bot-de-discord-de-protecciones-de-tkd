from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def clasf(imagen):
    
# Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

# Load the model
    model = load_model("C:/Users/Usuario/Downloads/Bot_ia - copia/keras_model.h5", compile=False)

# Load the labels
    class_names = open("C:/Users/Usuario/Downloads/Bot_ia - copia/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
    image = Image.open(imagen).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
    image_array = np.asarray(image)

# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
    data[0] = normalized_image_array

# Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    if index == 0:
        return "Esto parece un peto, sirve para protejer tu pecho y abdomen de las patadas y golpes y debes ponertelo en el pecho y amarrarlo a la espalda"
    if index == 1:
        return "Esto parece un casco, sirve para protejer tu cabeza de las patadas, se coloca sobre la cabeza y se ajusta a tu barbilla o mentón"
    if index == 2:
        return "Esto parece que son unas empeineras, sirven para proteger tus empeines y en algunos modelos la plantas, se colocan los pies adentro y algunas veces se amarran"
    if index == 3:
        return "Estos parecen unos guantes, sirve para protejer tus manos cuando  haces defensas o golpeas al peto, se pones como unos guantes normales y tienen un doble amarre en la misma dirección"
    if index == 4:
        return "Estas parecen unas antebraceras, al igual que los guantes sirven para proteger, como el nombre lo indica, tus antebrazos, se tiene que meter los brazos y ajustar "
    if index == 5:
        return "Estas parecen unas espinilleras, como las empeineras te protegen a la hora de patear, se mete el pie y como el nombre lo dice se ajustan a las espinillas o tibia"





