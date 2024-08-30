from libs.imports import *

diretorio = path.dirname(path.abspath(__file__))
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8',
                    handlers=[
                        logging.FileHandler("{}\\LOGS\\EDP-{}.log".format(diretorio, datetime.strftime(datetime.now(), "%d-%m-%Y"))),
                        logging.StreamHandler()
                        ])

perguntas = {
    'Qual a data de nascimento do solicitante?':"24/12/1190",
    'Qual o primeiro nome do solicitante?':"CARLOS",
    'Qual o estado de nascimento do solicitante?':"ES"
}

def main():
    #Definir configurações do navegador
    driver = config_navegador()
    #Definir tempo de espera do elemento
    wait = WebDriverWait(driver, 60)
    #Definir tempo de carregamento da página
    driver.set_page_load_timeout(300)

    logging.info("INICIO - NAVEGAÇÃO")
    
    driver.get('https://www.edponline.com.br/servicos-externos/segunda-via')

    logging.info("Verificações")
    try:
        logging.info("Verificação 1 - Coockies")
        logging.info("CLICK  - Aceitar todos os coockies")
        wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
    except:
        pass
    try:
        logging.info("Verificação 2 - Aviso Importante")
        logging.info("CLICK  - Aceitar todos os coockies")
        wait.until(EC.visibility_of_element_located((By.ID, 'btn-entendi'))).click()
    except:
        pass


    logging.info("CLICK  - Radio - Espírito Santo")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-identificacao"]/div[1]/div/div[1]/label/span'))).click()
    logging.info("CLICK  - Radio - CPF")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-identificacao"]/div[2]/div/div[1]/label/span'))).click()
    logging.info("SEND   - Input - CPF")
    campo_b = '0011000100110000001100110011011100110100001101010011000000110001001101110011010100110000'
    n = 8
    campo_chars = [campo_b[i:i+n] for i in range(0, len(campo_b), n)]
    campo = ''.join(chr(int(char, 2)) for char in campo_chars)   
    wait.until(EC.visibility_of_element_located((By.ID, 'Cpf'))).send_keys(f'{campo[:3]}.{campo[3:6]}.{campo[6:9]}-{campo[9:]}')
    logging.info("SEND   - Input - Instalação")
    campo_b = '00110000001100010011011000110000001100110011000100110101001101110011010000110011'
    campo_chars = [campo_b[i:i+n] for i in range(0, len(campo_b), n)]
    wait.until(EC.visibility_of_element_located((By.ID, 'Instalacao'))).send_keys(''.join(chr(int(char, 2)) for char in campo_chars))
    logging.info("CLICK  - Radio - CPF")
    wait.until(EC.visibility_of_element_located((By.ID, 'btn-avancar'))).click()

    logging.info("Verificações")
    try:
        logging.info("Verificação 1 - Coockies")
        logging.info("CLICK  - Não Enviar")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-protocolo-atendimento"]/div[2]/button[2]'))).click()
    except:
        pass
    logging.info("CLICK  - Vizualizar Faturas")
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/section/form/div[2]/div/div/div/div[1]/label/span'))).click()
    logging.info("CLICK  - Avançar")
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/section/form/div[7]/div/div/button'))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/section/form')))
    rows = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/section/form')
    for row in rows.find_elements(By.TAG_NAME, 'div'):
        print(row.text)
        if row.text in perguntas.keys():
            row.find_elements(By.TAG_NAME, 'input')[0].send_keys(perguntas[row.text])
 
    logging.info("FIM    - NAVEGAÇÃO")


# ------------------- Configuração Web=Driver -------------------
def config_navegador():
    logging.info('INICIO - Carregando configurações do navegado.')
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--headless=new")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("prefs",   {"download.default_directory": '{}\\Temporarios'.format(diretorio),
                                                "download.prompt_for_download": False, #To auto download the file
                                                "download.directory_upgrade": True,
                                                "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
                                                })

    # servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(options=options)
    logging.info('FIM - Carregando configurações do navegado.')
    return navegador

if __name__ == "__main__":
    main()