from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data.locators import SearchPageLocators
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


def test_prueba_crear_tipo():
    driver.get(SearchPageLocators.URL_TIPOS_POKEMONES)

    button_crear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SearchPageLocators.BTN_CREAR_NUEVO_TIPO_ID))
    )
    driver.save_screenshot("results/test_tipo/home_tipos.png")
    button_crear.send_keys(Keys.ENTER)

    nombre_tipo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_TIPO_NAME))
    )

    nombre_tipo.send_keys("Fuego")
    driver.save_screenshot("results/test_tipo/creacion_tipo.png")

    btn_crear = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, SearchPageLocators.BTN_CREAR_TIPO_ID))
    )

    btn_crear.send_keys(Keys.ENTER)
    driver.save_screenshot("results/test_tipo/tipo_list.png")
    return nombre_tipo


def test_prueba_crear_region():
    driver.get(SearchPageLocators.URL_REGIONES_POKEMONES)

    button_crear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SearchPageLocators.BTN_CREAR_NUEVA_REGION_ID))
    )
    driver.save_screenshot("results/test_region/home_regiones.png")
    button_crear.send_keys(Keys.ENTER)

    nombre_region = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_REGION_NAME))
    )

    nombre_region.send_keys("Asia")
    driver.save_screenshot("results/test_region/creacion_region.png")

    btn_crear = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, SearchPageLocators.BTN_CREAR_REGION_ID))
    )

    btn_crear.send_keys(Keys.ENTER)
    driver.save_screenshot("results/test_region/region_list.png")
    return nombre_region


def test_prueba_crear_pokemon():
    driver.get(SearchPageLocators.URL_POKEMONES)

    button_crear = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SearchPageLocators.BTN_CREAR_NUEVO_POKEMON_ID))
    )
    driver.save_screenshot("results/test_pokemon/home_pokemones.png")
    button_crear.send_keys(Keys.ENTER)

    nombre_pokemon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_POKEMON_NAME))
    )

    nombre_pokemon.send_keys("Pikachu")
    driver.save_screenshot("results/test_pokemon/creacion_pokemon_nombre.png")

    image_pokemon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_POKEMON_IMAGE))
    )

    image_pokemon.send_keys("https://www.pokemon.com/static-assets/app/static3/img/og-default-image.jpeg")
    driver.save_screenshot("results/test_pokemon/creacion_pokemon_imagen.png")

    region_pokemon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_POKEMON_REGION))
    )

    select_region = Select(region_pokemon)
    select_region.select_by_value("3")
    driver.save_screenshot("results/test_pokemon/creacion_pokemon_region.png")

    tipo_pokemon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_POKEMON_TIPO))
    )

    select_tipo = Select(tipo_pokemon)
    select_tipo.select_by_value("31")
    driver.save_screenshot("results/test_pokemon/creacion_pokemon_tipo.png")

    btn_crear = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, SearchPageLocators.BTN_CREAR_POKEMON_ID))
    )

    btn_crear.send_keys(Keys.ENTER)
    driver.save_screenshot("results/test_pokemon/pokemon_new_list.png")
    return nombre_pokemon


def test_prueba_filtrar_nombre_pokemon():
    driver.get(SearchPageLocators.URL_HOME)

    input_nombre = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_FILTRAR_POKEMON_NOMBRE))
    )
    driver.save_screenshot("results/test_filtrar_nombre/home.png")
    input_nombre.send_keys("Pikachu")
    driver.save_screenshot("results/test_filtrar_nombre/input_filtrar.png")

    btn_buscar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SearchPageLocators.BTN_FILTRAR_NOMBRE_POKEMON))
    )

    btn_buscar.send_keys(Keys.ENTER)
    driver.save_screenshot("results/test_filtrar_nombre/busqueda.png")

    return input_nombre


def test_prueba_filtrar_region_pokemon():
    driver.get(SearchPageLocators.URL_HOME)

    region_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, SearchPageLocators.INPUT_FILTRAR_POKEMON_REGION))
    )
    driver.save_screenshot("results/test_filtrar_region/home.png")
    select_region = Select(region_select)
    select_region.select_by_value("3")
    driver.save_screenshot("results/test_filtrar_region/pokemon_region.png")

    btn_buscar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SearchPageLocators.BTN_FILTRAR_REGION_POKEMON))
    )

    btn_buscar.send_keys(Keys.ENTER)
    driver.save_screenshot("results/test_filtrar_region/busqueda.png")

    return region_select
