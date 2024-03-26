# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t")    # dataFrame이 입력된다
    return df

def plot_matplotlib():        #streamlit 문법
    st.title("Categorical Bar Plot with Seaborn")   # 대시보드 제목을 지정
    df = load_data()
    fig, ax = plt.subplots() # 시각화 하는 메소드
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Categorical Bar Plot")
    
    st.pyplot(fig)         # 대시보드에 출력하는 코드

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')
    
    df = load_data()
    st.dataframe(df, use_container_width=True)   # 대시보드에 표 삽입하는 코드

    #pandas style  -  두번째 표 데이터를 만드는 코드
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib()  # 그래프 삽입하는 코드
    
    
if __name__ == "__main__":
    main()