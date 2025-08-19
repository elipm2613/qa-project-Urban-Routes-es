import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    confort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_button = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_field = (By.ID, "phone")
    siguiente_button = (By.XPATH, "//button[contains(@class, 'full') and text()='Siguiente']")
    sms_code_field = (By.ID, "code")
    confirmar_button = (By.XPATH, "//button[contains(@class, 'full') and text()='Confirmar']")
    pago_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    tarjeta_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID, 'number')
    cvv_field = (By.XPATH, "//input[@placeholder='12']")
    add_card_window = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active')
    link_card_button = (By.CSS_SELECTOR, '.pp-buttons > button:nth-child(1)')
    close_button = (By.XPATH, "//button[contains(@class, 'button full') and text()='Agregar']")
    pp_value = (By.CLASS_NAME, "pp-value-text")
    close_button_pago = (By.CSS_SELECTOR, '.payment-picker .close-button.section-close')

    message_input = (By.ID, 'comment')

    blanket_and_tissues = (By.CSS_SELECTOR, '.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    ice_cream_add_button = (By.CSS_SELECTOR,
                            '.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    helado_cantidad = (By.CSS_SELECTOR, '.counter-value')
    viaje_button = (By.CSS_SELECTOR, '.smart-button-wrapper > button')
    taxi_modal = (By.CSS_SELECTOR, '.order.shown > div.order-body')
    driver = (By.CSS_SELECTOR, '.order-subbody > div.order-buttons > div:nth-child(1) > div.order-button > img')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

#  Getter, Setter, Reader, Clicker

    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.confort_icon))

    def click_on_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_phone_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_button))

    def click_on_phone_button(self):
        self.get_phone_button().click()

    def set_phone(self, from_phone):
        field = self.wait.until(EC.visibility_of_element_located(self.phone_field))
        field.clear()
        field.send_keys(from_phone)
        assert from_phone == field.get_attribute("value")

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def get_next_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.siguiente_button))

    def click_on_next_button(self):
        self.get_next_button().click()

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.sms_code_field))
        sms_field = self.driver.find_element(*self.sms_code_field)
        sms_field.clear()
        sms_field.send_keys(code)
        self.driver.find_element(*self.confirmar_button).click()

    def retrieve_phone_code(driver):
        return "123456"

    def get_pago_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pago_button))

    def click_on_pago_button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "overlay")))
        button = self.wait.until(EC.element_to_be_clickable(self.pago_button))
        button.click()

    def get_tarjeta_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.tarjeta_button))

    def click_on_tarjeta_button(self):
        self.get_tarjeta_button().click()

    def click_card(self, card_number):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.card_number_field).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_number_field)).send_keys(card_number)

    def fill_cvv_field(self, card_code):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.cvv_field).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cvv_field)).send_keys(card_code)


    def get_aceptar_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.add_card_window))
        return self.wait.until(EC.element_to_be_clickable(self.link_card_button))

    def click_on_aceptar_button(self):
        self.get_aceptar_button().click()

    def get_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_button))

    def click_on_close_button(self):
        self.driver.implicitly_wait(20)
        self.get_close_button().click()

    def is_card_linked(self):
        return self.driver.find_element(*self.pp_value).text

    def get_close_button_pago(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_button_pago))

    def click_on_button_pago(self):
        self.get_close_button_pago().click()

    def get_message_input(self, message):
        message_box = self.wait.until(EC.presence_of_element_located(self.message_input))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_box)
        message_box.clear()
        message_box.send_keys(message)

    def is_message_sent(self, expected_message):
        message_input = self.driver.find_element(*self.message_input)
        return expected_message in message_input.get_attribute("value")

    def get_manta(self):
        return self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues))

    def click_on_pedir_manta(self):
        self.get_manta().click()

    def get_seleccionar_helado(self):
        counter = self.driver.find_element(*self.helado_cantidad)
        return int(counter.text.strip())

    def click_on_helado(self, cantidad=2):
        button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        for _ in range(cantidad):
            button.click()
            self.wait.until(EC.element_to_be_clickable(self.ice_cream_add_button))

    def helado(self):
        return self.get_seleccionar_helado() == 2

    def get_confirmar_viaje(self):
        return self.wait.until(EC.element_to_be_clickable(self.viaje_button))

    def click_on_confirmar_viaje(self):
        self.driver.implicitly_wait(10)
        self.get_confirmar_viaje().click()

    def get_viaje(self):
        return self.wait.until(EC.presence_of_element_located(self.taxi_modal))
        return self.wait.until(EC.element_to_be_clickable(self.driver))

    def click_viaje(self):
        self.get_viaje().click()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)



    def test_1_set_route(self):
        # Prueba 1: Configurar la dirección
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort(self):
        # Prueba 2: Seleccionar la tarifa Comfort
        self.routes_page.click_on_request_taxi_button()
        self.routes_page.click_on_comfort_icon()

    def test_3_set_phone(self):
        # Prueba 3: Rellenar el numero de teléfono
        self.routes_page.click_on_phone_button()
        self.routes_page.set_phone(data.phone_number)
        assert self.routes_page.get_phone() == data.phone_number

    def test_siguiente(self):
        self.routes_page.click_on_next_button()

    def test_set_sms(self):
        self.routes_page.set_sms_code()

    def test_4_pago(self):
        # Prueba 4: Agregar una tarjeta de crédito
        self.routes_page.click_on_pago_button()

    def test_tarjeta(self):
        self.routes_page.click_on_tarjeta_button()

    def test_set_card(self):
        self.routes_page.click_card(data.card_number)
        self.routes_page.fill_cvv_field(data.card_code)

    def test_aceptar_button(self):
        self.routes_page.click_on_aceptar_button()
        assert self.routes_page.is_card_linked(), "La tarjeta no fue vinculada correctamente"

    def test_close_button(self):
        self.routes_page.click_on_close_button()

    def test_button_pago(self):
        self.routes_page.click_on_button_pago()

    def test_5_mensaje_conductor(self):
        # Prueba 5: Escribir un mensaje para el controlador.
        self.routes_page.get_message_input(data.message_for_driver)
        assert self.routes_page.is_message_sent(data.message_for_driver), "El mensaje no se ingresó correctamente"


    def test_6_pedir_manta(self):
        # Prueba 6: Pedir manta y pañuelos.
        self.routes_page.click_on_pedir_manta()
        assert self.routes_page.get_manta(), "La opción de manta y pañuelos no fue activada"

    def test_7_pedir_helado(self):
        # Prueba 7: Pedir 2 helados.
        self.routes_page.click_on_helado()
        assert self.routes_page.helado(), "No se agregaron 2 helados"

    def test_8_confirmar_viaje(self):
        # Prueba 8: Aparece el modal para buscar un taxi.
        self.routes_page.click_on_confirmar_viaje()
        time.sleep(25)

    def test_9_viaje_espera(self):
        # Prueba 9: Esperar a que aparezca la información.
        self.routes_page.get_viaje()
        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
