import streamlit as st

def algemeen():
    luchtbehandeling = st.selectbox(
        'Luchtbehandeling:',
        ('Kies....', "centrale mech. ventilatie", "decentrale mech. ventilatie"))
    if luchtbehandeling is "centrale mech. ventilatie":
        concept_luchtbehandeling = st.selectbox(
            'Centrale luchtbehandeling concept:',
            ('Kies....', "cera-unit met CO2 regeling", "VAV-units"))

    if luchtbehandeling is "decentrale mech. ventilatie":
        concept_luchtbehandeling = st.selectbox(
            'Decentrale luchtbehandeling concept:',
            ('Kies....', "Type D vent. met WTW", "Type C vent. met raamroosters"))
    if concept_luchtbehandeling == "cera-unit met CO2 regeling":
        st.checkbox('Tekeningen van Cera-unit toevoegen aan bijlage?')
    if concept_luchtbehandeling == "Type D vent. met WTW":
        st.checkbox('Tekeningen van WTW-unit toevoegen aan bijlage?')
    return concept_luchtbehandeling

def luchtbehandeling(concept_luchtbehandeling):
    st.caption(concept_luchtbehandeling)
