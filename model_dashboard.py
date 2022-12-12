import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')

def build_model(taille, nb_rooms, garden):
    if type(taille) != float and type(taille) != int:
        raise Exception("Size must be a numeric value")
    if taille < 0:
        raise Exception("Size must be positive")

    if (type(nb_rooms) != float) and (type(nb_rooms) != int):
        raise Exception("Nb_rooms must be an integer")

    if nb_rooms < 0:
        raise Exception("Nb_rooms must be positive")

    if type(garden) != float and type(garden) != int:
        raise Exception("Garden must be a numeric value")
    if garden < 0:
        raise Exception("Garden must be positif or null")

    model = load_model()

    if taille <= 0:
        return 'mettre taille correcte'
    if nb_rooms <= 0:
        return "mettre nombre de chambre correct"

    if taille > 0 and nb_rooms > 0:
        X = [[taille, nb_rooms, garden]]
        return model.predict(X)[0]



def main():
	st.title("Prediction de prix de maison")
	taille = st.number_input("Taille maison")
	nb_rooms = int(st.number_input("Nombre de chambre"))
	garden = st.number_input("Y a un jardin")
	st.write(f"le prix de la maison est : {build_model(taille, nb_rooms, garden)}")	

if __name__ == "__main__":
    main()
