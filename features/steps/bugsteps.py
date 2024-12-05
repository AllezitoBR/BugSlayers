from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")


@when(u'Insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.ID , "mui-1").send_keys("alle_andrade123@hotmail.com")
    context.driver.find_element(By.ID , "outlined-adornment-password").send_keys("050290")

@when(u'Faço o Login')
def step_impl(context):
    botao_enviar = WebDriverWait(context.driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/form/button"))
    )
    context.driver.execute_script("arguments[0].click();", botao_enviar)