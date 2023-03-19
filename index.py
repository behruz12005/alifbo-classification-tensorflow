import streamlit as st
import tensorflow as tf
from PIL import Image
import tensorflow as tf
from PIL import Image as PILImage
import numpy as np
from keras.models import load_model


# Tasvir qabul qilish oynasi
image_file = st.file_uploader("Tasvirni yuklang", type=["jpg", "jpeg", "png"])
if image_file is not None:
    img = PILImage.open(image_file)
    img = img.resize((70, 70))


# Tasvirni ko'rish uchun funksiya
def view_image(image):
    st.image(image, width=50,caption='Tasvir', use_column_width=True)

# Modelni boshqarish uchun funksiya
def load_model():
    model = tf.keras.models.load_model('my_model.h5')
    return model


# Tasvir qabul qilishni tekshirish



if image_file is not None:
    CATEGORIES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    # Tasvirni yuklash va ko'rsatish


    IMG_SIZE = 70
    image = Image.open(image_file)
    view_image(image)
    img = np.array(img)
    if len(img.shape) == 3:       
        img = img[:,:,0]
    img = img.reshape(-1, 70, 70, 1)
    img = img / 255.0
    model = load_model()
    import numpy as np

    # Test array
    arr = np.random.rand(300, 300)

    # Resizing array to (70, 70)
    resized_arr = np.resize(arr, (70, 70))



    # Tasvirlarni sinash va natijani ko'rsatish
    predictions = model.predict(img)
    natija=CATEGORIES[np.argmax(predictions)]
    # Tasvirni konsolga chiqarish
    st.write(f"<p style='text-align: center; font-size: 80px;'>{natija}</p>", unsafe_allow_html=True)
    # st.write(f'Natija: {natija}')
else:
    st.write("Iltimos, tasvirni yuklang!")

