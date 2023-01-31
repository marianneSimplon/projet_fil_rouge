# streamlit run app.py
import os
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import matplotlib.pyplot as plt


### Load PIPELINE ###
# PIPELINE_VERSION = 'model.pickle'
# PIPELINE_PATH = os.path.join(os.getcwd(), 'my_pickles',
#                           PIPELINE_VERSION)  # path vers le pipeline
# with open(PIPELINE_PATH, 'rb') as handle:
#     PIPELINE = pickle.load(handle)

## Load MODEL ###
MODEL_VERSION = 'rfr.pkl'
MODEL_PATH = os.path.join(os.getcwd(), '../my_pickles',
                          MODEL_VERSION)  # path vers le modèle
with open(MODEL_PATH, 'rb') as handle:
    MODEL = pickle.load(handle)

## Load SCALER ###
SCALER_VERSION = 'minmaxscaler.pkl'
SCALER_PATH = os.path.join(os.getcwd(), '../my_pickles',
                           SCALER_VERSION)  # path vers le modèle
with open(SCALER_PATH, 'rb') as handle:
    SCALER = pickle.load(handle)

## Load ENCODER ###
ENCODER_VERSION = 'onehotencoder.pkl'
ENCODER_PATH = os.path.join(os.getcwd(), '../my_pickles',
                            ENCODER_VERSION)  # path vers le modèle
with open(ENCODER_PATH, 'rb') as handle:
    ENCODER = pickle.load(handle)

### RECUPERATION DES INPUTS ###


def inputs_to_df(longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity):
    data = {'longitude': [float(longitude)], 'latitude': [float(latitude)], 'housing_median_age': [housing_median_age], 'total_rooms': [total_rooms], 'total_bedrooms': [
        total_bedrooms], 'population': [population], 'households': [households], 'median_income': [float(median_income)], 'ocean_proximity': [ocean_proximity]}
    my_inputs_dataframe = pd.DataFrame(data)
    # st.dataframe(my_inputs_dataframe)
    return my_inputs_dataframe


def preprocess_inputs(input_dataframe):
    # preprocess_data = PIPELINE.transform(input_dataframe)
    non_cat = pd.DataFrame(input_dataframe[input_dataframe.columns[0:8]])
    cat = pd.DataFrame(input_dataframe[input_dataframe.columns[-1]])
    # st.dataframe(non_cat)
    # st.dataframe(cat)
    scale_data = pd.DataFrame(SCALER.transform(non_cat), columns=[
                              "longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income"])
    encode_data = pd.DataFrame(pd.DataFrame.sparse.from_spmatrix(
        ENCODER.transform(cat)))
    encode_data.rename({0: 'H_OCEAN', 1: 'INLAND', 2: 'ISLAND',
                       3: 'NEAR_BAY', 4: 'NEAR_OCEAN'}, inplace=True, axis=1)
    encode_data = encode_data.drop(["H_OCEAN", "ISLAND"], axis=1)
    # print(encode_data)
    # st.dataframe(scale_data)
    # st.dataframe(encode_data)
    preprocess_data = pd.concat([scale_data, encode_data], axis=1)
    # st.dataframe(preprocess_data)
    # print(preprocess_data)
    return preprocess_data


def predict(preprocessed_input):
    # pred = PIPELINE.predict(pd.DataFrame(preprocessed_input))
    pred = MODEL.predict(pd.DataFrame(preprocessed_input))
    return pred[0]


#############################################################################################
######################################### STREAMLIT #########################################
#############################################################################################

### BODY ###
st.title("Prédiction du prix médian d'un quartier de logements en Californie")

image = Image.open('san-francisco-210230_960_720.jpg')
st.image(image, caption='Maisons de San Francisco')

# EXPANDER
with st.expander("Rappels sur le prix médian des logements du quartier et sur le modèle de prédiction"):
    st.write("RMSE du modèle = XXXX")
    df = pd.read_csv(
        r'C:/Users/Admin/Documents/marianneSimplon/simplon/immo_SiliconValley_marianneD/data/traindata_ori.csv', delimiter=',', decimal='.')
    median_house_value = df['median_house_value']
    fig, ax = plt.subplots()
    ax.hist(median_house_value	, bins=20)
    ax.set_title(
        "Distribution du prix médian d'un quartier de logements en Californie")
    ax.set_xlabel("Prix médian d'un quartier")
    st.pyplot(fig)

st.subheader(
    "Veuillez entrer les caractéristiques du quartier de logement qui vous intéresse :")

longitude = st.text_input('Longitude')

latitude = st.text_input('Latitude')

housing_median_age = st.number_input('Age médian des logements', step=1)

total_rooms = st.number_input('Nombre total de pièces', step=1)

total_bedrooms = st.number_input('Nombre total de chambres', step=1)

population = st.number_input('Nombre total de résidents', step=1)

households = st.number_input('Nombre total de ménages', step=1)

median_income = st.text_input('Revenu médian des ménages')

ocean_proximity = st.selectbox(
    "Proximité de l'océan (Sélectionnez une option ci-dessous)",
    ('INLAND', '<1H OCEAN', 'NEAR BAY', 'NEAR OCEAN', 'ISLAND'))


# # SIDEBAR
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

if st.button(label="Estimer le prix médian"):
    try:
        datas = inputs_to_df(longitude, latitude, housing_median_age, total_rooms,
                             total_bedrooms, population, households, median_income, ocean_proximity)
        if datas.isnull().values.any() == False:
            preprocess_datas = preprocess_inputs(datas)
            my_pred = predict(preprocess_datas)
            st.write('Prix médian estimé du quartier de logements :')
            st.write(my_pred)
        else:
            st.write(
                "Veuillez remplir tous les champs du formulaire s'il vous plait")
    # except Exception as e:
    except Exception:
        st.write("Une erreur s'est produite.")
        # st.write(e)
        # print(e)
