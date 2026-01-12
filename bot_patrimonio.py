import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select 
from webdriver_manager.chrome import ChromeDriverManager
import time


ITENS_JA_FEITOS = 00


FILTRO_UNIDADE = "JP" 


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
# Caminho das credenciais (verifique se o arquivo está nessa pasta mesmo)
creds = ServiceAccountCredentials.from_json_keyfile_name(r'c:\Projeto Python\credenciais.json', scope)
client = gspread.authorize(creds)

print("Conectando à planilha...")

sheet = client.open("Inventario UP VIX").sheet1 
dados = sheet.get_all_records(head=2)
print(f"Planilha carregada! Analisando linhas...")


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()


navegador.get("https://servicos.upvix.com.br") 

print("--- ATENÇÃO ---")
print(f"O bot vai processar APENAS itens com a sigla: '{FILTRO_UNIDADE}'")
print(f"Começando a partir da linha {ITENS_JA_FEITOS} (da contagem do código).")
print("Faça o LOGIN e vá para a tela de lista de itens.")
print("Você tem 30 segundos...")
time.sleep(30) 

def preencher(xpath, valor):
    texto = str(valor).strip()
    if texto and texto != "-" and texto != "":
        try:
            campo = navegador.find_element(By.XPATH, xpath)
            campo.clear()
            campo.send_keys(texto)
        except: pass 

contador_real = 0 

for i, linha in enumerate(dados):

    if i < ITENS_JA_FEITOS:
        continue
    unidade_linha = str(linha['ESTA']).strip().upper()
    
    if unidade_linha != FILTRO_UNIDADE:
        continue
    
    try:
        nome_prod = linha['NOME DOS PRODUTOS']
        if not nome_prod: continue 

        cod_raw = linha['CODIGO']

        if str(cod_raw).strip() == "-" or str(cod_raw).strip() == "":
            patrimonio = "" 
        else:

            patrimonio = str(cod_raw).zfill(8) 
            
        local = linha['LOCAL']
        marca = linha['Marca']
        modelo = linha['Modelo']
        estado_planilha = str(linha['Estado']).strip().lower()

        contador_real += 1
        print(f"Cadastrando {contador_real} (Linha planilha: {i+3}): {nome_prod} | Unidade: {unidade_linha}")

        try:
            navegador.find_element(By.XPATH, "//button[contains(., 'Novo Item')]").click()
            time.sleep(2)
        except:
            print("ERRO: Botão 'Novo Item' não encontrado. Tentando continuar...")
            continue 


        preencher('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div[1]/input', nome_prod)

        preencher('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/input', patrimonio)
        # Local, Marca, Modelo
        preencher('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div[2]/div[2]/input', local)
        preencher('/html/body/div[2]/div/div/div[3]/div/div[3]/div/div[1]/input', marca)
        preencher('/html/body/div[2]/div/div/div[3]/div/div[3]/div/div[2]/input', modelo)

        try:
            xpath_status = '/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/select'
            elemento = navegador.find_element(By.XPATH, xpath_status)
            selecao = Select(elemento)

            palavra_chave = "estoque" # Padrão
            if "uso" in estado_planilha: palavra_chave = "uso"
            elif "reparo" in estado_planilha: palavra_chave = "reparo"
            elif "baixado" in estado_planilha or "descartado" in estado_planilha: palavra_chave = "baixado"


            encontrou = False
            for opcao in selecao.options:
                if palavra_chave in opcao.text.lower():
                    selecao.select_by_visible_text(opcao.text)
                    encontrou = True
                    break
            
            if not encontrou:
                selecao.select_by_visible_text("Estoque")

        except Exception as e:
            print(f"Aviso Status: {e}")

        try:
            navegador.find_element(By.XPATH, "//button[contains(., 'Salvar')]").click()
            time.sleep(3) # Tempo para salvar
        except:
            print("Erro ao clicar em Salvar.")

    except Exception as e:
        print(f"Erro geral na linha {i+3}: {e}")

print("Automação Finalizada!")