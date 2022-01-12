import streamlit as st
import pandas as pd
import numpy as np
from docx import Document
import bestand_verwerking as bv
import algemeen as a
import werktuigbouw as w
import document_opbouwen as toe
import schachten as s


st.title("Document samenstellen")
with st.expander("Algemeen"):
     algemeen = a.projectnaam_invoer()
st.subheader("Werktuigbouwkunde")
with st.expander("Algemeen"):
     st.write("hallo Algemeen")
     w.algemeen()
with st.expander("Luchtbehandeling"):
     st.write("hallo luchtbehandeling")
with st.expander("Verwarming"):
     st.write("hallo Verwarming")
with st.expander("Koeling"):
     st.write("hallo Koeling")
st.subheader("Elektrotechniek")
with st.expander("Elektrotechniek"):
     st.write("hallo Elektrotechniek")
st.subheader("Schachten en ruimtebeslag")
with st.expander("schachten"):
     st.write("schachten")
     s.relatieschema()

toe.document_maken()
toe.inleiding(algemeen[2], algemeen[3])
toe.algemeen(concept_luchtbehandeling)
result = st.button("document maken")

if result:
     bv.document_genereren(algemeen[0], algemeen[1])

