import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


image = Image.open('images/DNAcount.png')
st.image(image=image, use_column_width=True)
# Page Title
st.write("""
         # DNA Nucleiotide Count
         ---- 
         """)


# Input section for DNA sequence: 
st.header('Enter DNA sequence: ')

sequence = st.text_input('>DNA Query:')

st.write("""
         ----
         """)


st.header("Your input: ")
st.write(sequence)

st.write("""
         ----
         """)


def DNA_nuecleotide_count(sequence):
    d = { 
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }
    return d


X = DNA_nuecleotide_count(sequence)
df = pd.DataFrame.from_dict(X, orient='index', columns=['count'])
df.index.name = 'nucleotide'
# Reset the index so that the index becomes the nucleotide names: 
df = df.reset_index()

st.write(df)

st.bar_chart(x='nucleotide', y='count', data=df)

st.write("""
         ---
         """)

st.header("GC Content:")

dna_len = len(sequence)
# Handle division by 0 case:
if (dna_len <= 0):
    dna_len = 1

sequence = sequence.upper()

st.write("""
     
         """)

gc_content =  ( ( sequence.count('G') + sequence.count('C') )/ dna_len ) * 100

st.write(f'Length of sequence is:  {dna_len}')
st.write(f'GC Content is:  %.2f' %gc_content + '%')
