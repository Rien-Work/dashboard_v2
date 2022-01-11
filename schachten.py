import streamlit as st
import graphviz as graphviz

def relatieschema():
    graph = graphviz.Digraph()
    graph.node('bk', label='Badkamer', shape='box', color='black')
    graph.node('t', label='Toilet', shape='box', color='black')
    graph.node('s', label='Schacht', shape='box', color='black')
    graph.node('tr', label='Techische ruimte', shape='box', color='black')
    graph.node('wm', label='Warme Meterkast', shape='box', color='black')
    graph.node('vv', label='Vloerverwarming-verdeler', shape='box', color='black')

    graph.edge('s', 't', style='dashed', color='green')
    graph.edge('s', 'tr', style='dashed', color='green')
    graph.edge('tr', 'bk', style='dashed', color='red')
    graph.edge('tr', 'bk', style='dashed', color='red')

    st.graphviz_chart(graph)


