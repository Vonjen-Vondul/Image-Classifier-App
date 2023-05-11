import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL as Image
from io import BytesIO
from keras.preprocess.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.inception_v3 import preprocess_input
from keras.models import load_model


model= load_model('.best_model.h5')
classes={0:'cat',1:'dog'}
img_file=st.file_uploader('select an image', type=['jpg','png','jpeg','gif'])

if img_file is not None:
    img=Image.open(img_file)
    st.image(img,caption='uploaded image sucessfully')
    
    if st.button('Predict'):
        img=img.resize((256,256))
        i=img_to_array(img)
        i=preprocess_imput(i)
        input_arr=np.array([i])
        
        y_out=np.argmax(model.predict(input_arr))
        y_out1=classes[y_out]
        
        st.write(f'This image is a {y_out1}')