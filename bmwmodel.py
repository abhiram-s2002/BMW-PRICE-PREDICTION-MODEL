import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":rainbow[BMW PRICE PREDICTION]")
    image = Image.open("bmw-logo.jpg")
    st.image(image, width=800)

    
    model_dict = {
        '3 Series': 2, '1 Series': 0, '2 Series': 1, '5 Series': 4, '4 Series': 3, 
        'X1': 13, 'X3': 15, 'X5': 17, 'X2': 14, 'X4': 16, 'M4': 10, '6 Series': 5, 
        'Z4': 21, '7 Series': 6, 'X6': 18, 'X7': 19, '13': 22, '8 Series': 7, 
        'M5': 11, 'M3': 9, 'M2': 8, '18': 23, 'M6': 12, 'Z3': 20
    }

    transmission_dict = {
        'Automatic': 2, 'Manual': 0, 'Semi-Auto': 1
    }

    fuelType_dict = {
        'Diesel': 0, 'Petrol': 4, 'Hybrid': 2, 'Other': 3, 'Electric': 1
    }

    
    model = st.selectbox("Model", list(model_dict.keys()))
    model_value = model_dict[model]

   
    transmission = st.selectbox("Transmission", list(transmission_dict.keys()))
    transmission_value = transmission_dict[transmission]

    
    fuelType = st.selectbox("Fuel Type", list(fuelType_dict.keys()))
    fuelType_value = fuelType_dict[fuelType]

    year = st.selectbox("Year", list(range(2000, 2025)))
    tax = st.number_input("Tax", min_value=0, max_value=580, step=5)
    engineSize = st.number_input("Engine Size (L)", min_value=0.0, max_value=10.0, step=0.1)

    
    features = [model_value, year, transmission_value, fuelType_value, tax, engineSize]

 

    model = pickle.load(open('bmw.sav', 'rb'))
    scalar = pickle.load(open('std_scalar_bmw_.sav', 'rb'))

    
    pred = st.button('PREDICT PRICE')

    if pred:
        
        transformed_features = scalar.transform([features])
        prediction = model.predict(transformed_features)

        # Display 
        st.write(f"The predicted car price is:   £ {prediction[0]:,.2f}")

main()

