import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Limpar Dados',
    page_icon = '🧹',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Limpar Dados')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.markdown(
    '''<p style="text-align: justify;">
    Permite excluir dados com erros ou fora de padrão (outlier). Limitar dados dentro de um determinado intervalo de valores.
    Excluir dados indesejados. Resumir os dados para uma determinada pesquisa.
    </p>'''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
