import sys

sys.path.append("../")
from behave import given, when, then
from access_component.components.implement_personal_data import PersonalData

init_form = PersonalData()


@given(u'Que el usuario ingresa al formulario')
def step_open_form(context):
    init_form.click_button_details()
    init_form.click_link_access()


@then(u'el sistema me muestra la pantalla inicial del formulario')
def step_view_window_initial(context):
    assert init_form.view_windows_initial() is True, "Not view window initial"


@given(u'Que el usuario se encuentra en la pantalla inicial del formulario')
def step_open_form(context):
    assert init_form.view_windows_initial() is True, "Not view window initial"


@when(u'El usuario hace click en el boton EMPEZAR')
def step_open_form(context):
    init_form.click_button_init()


@then(u'El sistema muestra una ventana modal con el texto "{text}"')
def step_get_modal_text(context, text):
    text_input = init_form.get_modal_coverage()
    assert text_input == text, "Texto del modal no coincide"


@given(u'que el usuario se encuentra en la ventana modal de cobertura')
def step_get_modal_coverage(context):
    text_input = init_form.get_modal_coverage()
    assert text_input != "", "Texto del modal no coincide"


@when(u'El usuario da click en el boton aceptar')
def step_click_button_accept(context):
    init_form.click_accept_modal()


@then(u'el sistema dirige a la pantalla "{title_page}"')
def step_get_window_insert_personal_data(context, title_page):
    text_title_page = init_form.get_title_insert_personal_data()
    assert text_title_page == title_page, "Texto del titulo de la pantalla no coincide"


@given(u'que el usuario despliega el combo box de tipo de documento')
def step_deploy_cbx_type_doc(context):
    init_form.deploy_cbx_type_ci()


@when(u'el usuario selecciona un item')
def step_select_item(context):
    init_form.select_item_cbx_type_ci()


@then(u'el item se debe mostrar seleccionado "{item}"')
def step_selected_item(context, item):
    item_selected = init_form.get_selected_item()
    assert item_selected == item, "Item seleccionado no corresponde"


@given(u'que el usuario ingresa un ci "{ci}"')
def step_deploy_cbx_type_doc(context, ci):
    init_form.insert_ci(ci)


@then(u'"{result}"')
def step_select_item(context, result):
    __xpath_txt_number_ci = '//*[@id="ci_2"]'
    if init_form.get_text_ci() == "":
        assert init_form.get_text_ci() == result, "Texto en input no coincide"
    else:
        assert init_form.get_text_ci() == result, "Texto en input no coincide"
        init_form.clear_input(__xpath_txt_number_ci)
        init_form.close_page()
