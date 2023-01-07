# Instala Selenium
# pip install selenium

# Importa las librerías necesarias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crea una función para iniciar sesión en TikTok
def login_to_tiktok(username, password):
    # Crea un objeto webdriver y abre TikTok
    driver = webdriver.Firefox()
    driver.get("https://www.tiktok.com/")

    # Haz clic en el botón "Iniciar sesión"
    login_button = driver.find_element_by_xpath("//a[@href='/login/email']")
    login_button.click()

    # Introduce tu nombre de usuario y contraseña
    username_field = driver.find_element_by_xpath("//input[@name='email']")
    password_field = driver.find_element_by_xpath("//input[@name='password']")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Haz clic en el botón "Iniciar sesión"
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    
    # Espera a que la página de inicio de sesión cargue
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/@tuusuario']")))

# Inicia sesión en TikTok utilizando tu nombre de usuario y contraseña
login_to_tiktok("joseramosb@gmail.com", "j0s33l173")

# Accede a la página de videos que le has dado "me gusta"
driver.get("https://www.tiktok.com/favorite/list")

# Crea una carpeta para guardar los videos descargados
if not os.path.exists("videos"):
    os.makedirs("videos")

# Obtén la lista de elementos de video de la página
video_elements = driver.find_elements_by_xpath("//a[@title='Video']")

# Descarga cada uno de los videos con yt-dlp
for element in video_elements:
    # Obtén la URL del video
    video_url = element.get_attribute("href")
    
    # Descarga el video con yt-dlp
    os.system(f"yt-dlp -o videos/{video.title} {video_url}")

# Cierra el navegador
driver.quit()

# Finaliza la sesión de TikTok
tiktok.logout()
