import pandas as pd
import streamlit as st
import altair as alt
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Avaliações de Imóveis',
    page_icon = '🏘️',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

dfActual = st.session_state['data']

# dfActual

# st.dataframe(dfActual,
#              column_config={
#                 #  'Overall': st.column_config.ProgressColumn(
#                 #      'Overall', format='%d', min_value = 0, max_value = 100
#                 #  ),
#                  'Valor total': st.column_config.ProgressColumn(
#                      'Valor Total', format='R$%f', min_value = 0, max_value = dfActual['Valor total'].max()
#                  ),
#                  #'TipoLogo': st.column_config.ImageColumn()
#              })


# Exclude the ID column
if 'ID' in dfActual.columns:
    dfActual = dfActual.drop(columns=['ID'])

# Format the column value type
dfActual['Valor total'] = dfActual['Valor total'].astype(float)

# Create the DataFrame wiht special format for same datass
st.dataframe(
    dfActual,
    column_config={
        'Valor total': st.column_config.ProgressColumn(
            'Valor Total', format='R$ %f', min_value = 0, max_value = dfActual['Valor total'].max()
        ),
        'Tipo': st.column_config.ImageColumn()
    }
)