import streamlit as st

def projectnaam_invoer():
    projectnaam = st.text_input('Project naam:', "nog geen projectnaam")
    st.caption('De projectnaam is: ' + projectnaam)
    projectnummer = st.text_input('Projectnummer:', "nog geen projectnummer!")
    st.caption('Projectnummer is: ' + projectnummer)
    gebouwcategorie = st.selectbox(
        'Gebouwcategorie:',
        ('Kies....', 'Kantoor (vrije markt)', 'Kantoor (overheid)', 'kantoor (projectontwikkelaar)', "bedrijfshal", "sporthal",
         "Verpleegshuis", "Apartementen", "Grondgebonden woningen", "Woontoren"))
    if gebouwcategorie is not "Apartementen" or "Grondgebonden woningen" or "Woontoren":
        bvo = st.text_input("BVO in m2: ")
    else:
        bvo = st.text_input("BVO in m2 per woning: ")
    return projectnaam, projectnummer, gebouwcategorie, bvo

def type_bouw():
    option = st.selectbox(
        'selecteer het type bouw',
        ('hoogbouw', 'laagbouw'))
    st.caption('je selecteerde: ' + option)
    if option == "hoogbouw":
        bouwlagen = st.slider('Aantal bouwlagen?', 0, 30, 1)
        st.write("het gebouw heeft ", bouwlagen, 'aantal bouwlagen')
        hoogte = st.slider('hoogte bouwlaag in meter?', 0.0, 4.0, 0.1)
        hoogte = round(bouwlagen * hoogte, 2)
        st.write("Het gebouw is ", hoogte, 'meter hoog')
        hoogte_string = str(hoogte)
    return option


def energie_opwekking():
    option = st.selectbox(
        'selecteer type warmte/koude opwekker:',
        ('warmtenet', 'warmtepomp'))
    if option == "warmtenet":
        option1 = st.selectbox(
            'Type warmtenet:',
            ('statsverwarming', 'collective WKO met warmtepomp'))
    if option == "warmtepomp":
        option2 = st.selectbox(
            'bron WP:',
            ("lucht", "bodemlus", "WKO")
        )