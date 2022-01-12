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
    if luchtbehandeling is "Kies....":
        concept_luchtbehandeling = "maak keuzen"
    return concept_luchtbehandeling

def luchtbehandeling(concept_luchtbehandeling):
    st.caption(concept_luchtbehandeling)
