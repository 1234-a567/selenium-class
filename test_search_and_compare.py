from POM.cameraphoto import CameraPhotoPage
from POM.compareproducts import CompareProductsPage
from POM.loginpage import LoginPage
from POM.productpage import ProductPage


def test_search_and_compare(login_driver):
    login = LoginPage(login_driver)
    login.enter_email("reddyvinuth27@gmail.com")
    login.enter_password("selenium")
    login.click_on_login_btn()
    login.hover_on_electronics()
    login.click_on_camera_photo_link()
    camera = CameraPhotoPage(login_driver)
    camera.click_on_1MP_60GB_HD()
    product = ProductPage(login_driver)
    product.click_on_add_to_compare()
    product.click_on_back_2_times()
    camera.click_on_camcorder()
    product.click_on_add_to_compare()
    compare = CompareProductsPage(login_driver)
    compare.click_on_remove_of_camcorder()
    compare.click_on_remove_of_handycam()
    if compare.check_empty_status() == True:
        assert True
    else:
        assert False
