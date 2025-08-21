
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import helpers


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
        code = helpers.retrieve_phone_code(self.driver)
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
        return self.wait.until(EC.visibility_of_element_located(self.taxi_modal))
        return self.wait.until(EC.element_to_be_clickable(self.driver))

    def click_viaje(self):
        self.get_viaje().click()
