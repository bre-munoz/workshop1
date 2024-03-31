import streamlit as st 

class ExcelValidadorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema excel"
        )
        
    def display_header(self):
        st.title("Insira o seu excel para validação")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

    def display_results(self, result, error):
        if error:
            error_messages = error.split('\n')  # Separa as diferentes mensagens de erro
            formatted_errors = []
            for msg in error_messages:
                # Extrai apenas a parte relevante da mensagem de erro
                error_part = msg.split("[", 1)[0].strip()
                formatted_errors.append(error_part)
            
            st.error("Ocorreram os seguintes erros durante a validação:")
            for err in formatted_errors:
                st.error(err)
        else:
            st.success("O schema do arquivo Excel está correto!")
        

    def display_save_button(self):
        return st.button("Salvar no Banco de Dados")
    
    def display_wrong_message(self):
        return st.error("Necessário corrigir a planilha!")
    
    def display_success_message(self):
        return st.success("Dados salvos com sucesso no banco de dados!")