import os
import json
from functions import Functions

def main():
    diretorio_pesquisa = ''


    arquivos_vue = Functions.find_vue_files(diretorio_pesquisa)
    nome_arquivo_vue_json = 'VUE_FILES.json'
    Functions.save_files_to_json(arquivos_vue, nome_arquivo_vue_json)

    strings_para_traducao, arquivos_sem_padrao = Functions.extract_strings_for_translation(arquivos_vue)
    nome_arquivo_translateds_json = 'TRANSLATEDS.json'
    Functions.save_strings_to_json(strings_para_traducao, nome_arquivo_translateds_json)

    nome_arquivo_non_t_json = 'NON_T_FILES.json'
    Functions.save_files_without_pattern(arquivos_sem_padrao, nome_arquivo_non_t_json)

    print(f'Arquivos Vue salvos em {nome_arquivo_vue_json}')
    print(f'Strings para tradução salvos em {nome_arquivo_translateds_json}')
    print(f'Arquivos sem o padrão $t( salvos em {nome_arquivo_non_t_json}')

if __name__ == "__main__":
    main()
