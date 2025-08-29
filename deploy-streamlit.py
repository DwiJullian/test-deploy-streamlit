import joblib
import pandas as pd
import numpy as np
import streamlit as st

model = joblib.load("model_rf_vectra.pkl")
scaler = joblib.load("standard_scaler.pkl")
columns = joblib.load("features_name.pkl") # ['score_pretest_py', 'score_pretest_ml', 'score_pretest_st', 'mini_project', 'ispeserta', 'weekly_quiz']

st.title("Prediksi Kelulusan Peserta Bootcamp")

score_py = st.number_input("Masukan score python :", max_value=100)
score_ml = st.number_input("Masukan score machine learning :", max_value=100)
score_st = st.number_input("Masukan score statistika :", max_value=100)
mini_project = st.number_input("Apakah mengumpulkan mini project ? :", max_value=1, placeholder="inputkan 1 untuk iya, inputkan 0 untuk tidak")
is_peserta = st.number_input("Apakah anda peserta bootcamp ? :", max_value=1, placeholder="inputkan 1 untuk iya, inputkan 0 untuk tidak")
weekly_quiz = st.number_input("Apakah anda menyelesaikan quiz ? :", max_value=1, placeholder="inputkan 1 untuk iya, inputkan 0 untuk tidak")

df = pd.DataFrame(
    [[score_py, score_ml, score_st, mini_project, is_peserta, weekly_quiz]],
    columns=['score_pretest_py', 'score_pretest_ml', 'score_pretest_st', 'mini_project', 'ispeserta', 'weekly_quiz']
)

score_col = ['score_pretest_py', 'score_pretest_ml', 'score_pretest_st']

for col, std in scaler.items():
    col_trans = std.transform(pd.DataFrame(df[col], columns=[col]))
    df[col+"_scaled"] = col_trans

df = df.drop(score_col, axis=1)

df = df.rename(
    columns={
        'score_pretest_py_scaled' : "score_pretest_py", 
        'score_pretest_ml_scaled' : "score_pretest_ml", 
        'score_pretest_st_scaled' : "score_pretest_st"
})

if st.button("Prediksi kelulusan", type="primary"):
    model_pred = model.predict(df[["score_pretest_py", "score_pretest_ml", "score_pretest_st", "mini_project", "ispeserta", "weekly_quiz"]])
    if model_pred == 1:
        st.write("Peserta Lulus")
    elif model_pred == 0:
        st.write("Peserta Tidak Lulus")
    else:
        st.write("Error")

