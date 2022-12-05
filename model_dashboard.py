import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')

def build_model(taille, nb_rooms, garden):
    model = load_model()

    if taille <= 0:
        return 'mettre taille correcte'
    if nb_rooms <= 0:
        return "mettre nombre de chambre correct"

    if taille > 0 and nb_rooms > 0:
        X = [[taille, nb_rooms, garden]]
        return model.predict(X)


def main():
	st.title("Prediction de prix de maison")
	taille = st.number_input("Taille maison")
	nb_rooms = st.number_input("Nombre de chambre")
	garden = st.number_input("Y a un jardin")
	st.write("le prix de la maison est : {}".format(build_model(taille, nb_rooms, garden)))	

if __name__ == "__main__":
    main()
