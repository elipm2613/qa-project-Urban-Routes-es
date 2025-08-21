import time
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from data import data


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)



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
        assert self.routes_page.get_comfort_icon(), "La tarifa Comfort no fue seleccionada correctamente"

    def test_3_set_phone(self):
        # Prueba 3: Rellenar el numero de teléfono
        self.routes_page.click_on_phone_button()
        self.routes_page.set_phone(data.phone_number)
        assert self.routes_page.get_phone() == data.phone_number

    def test_4_pago(self):
        # Prueba 4: Agregar una tarjeta de crédito
        self.routes_page.click_on_next_button()
        self.routes_page.set_sms_code()
        self.routes_page.click_on_pago_button()
        assert self.routes_page.is_card_linked(), "La tarjeta no fue vinculada correctamente"

    def test_5_mensaje_conductor(self):
        # Prueba 5: Escribir un mensaje para el controlador.
        self.routes_page.click_on_tarjeta_button()
        self.routes_page.click_card(data.card_number)
        self.routes_page.fill_cvv_field(data.card_code)
        self.routes_page.click_on_aceptar_button()
        assert self.routes_page.is_card_linked(), "La tarjeta no fue vinculada correctamente"
        self.routes_page.click_on_close_button()
        self.routes_page.click_on_button_pago()
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
        #assert self.routes_page.taxi_modal(), "No apareció el modal para buscar un taxi"
        assert self.routes_page.get_confirmar_viaje(),"El viaje no fue confirmado"
        time.sleep(25)

    def test_9_viaje_espera(self):
        # Prueba 9: Esperar a que aparezca la información.
        self.routes_page.get_viaje()
        assert self.routes_page.get_viaje(), "No fue posible mostrar la información del conductor"
        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
