Feature: Ingresar o fallar ingreso a la APP

  Scenario: As usuario del sistema I want abrir el sistema For poder solicitar una cuenta
    Given Que el usuario ingresa al formulario
     Then el sistema me muestra la pantalla inicial del formulario

  Scenario Outline: As usuario del sistema I want iniciar el llenado del formulario For solicitar una cuenta
    Given Que el usuario se encuentra en la pantalla inicial del formulario
     When El usuario hace click en el boton EMPEZAR
     Then El sistema muestra una ventana modal con el texto "<text>"

        Examples: Text Modal
                    |text                                                                                                                                                                        |
                    |Estimado Cliente, la solicitud de contratación de la cuenta digital está habilitada para las ciudades de Cochabamba, La Paz, El Alto, Oruro, Potosí, Sucre, Tarija, Santa Cruz de la Sierra y Montero.|


  Scenario Outline: As usuario del sistema I want ingresar a la pantalla de datos personales For llenado de formulario
    Given que el usuario se encuentra en la ventana modal de cobertura
     When El usuario da click en el boton aceptar
     Then el sistema dirige a la pantalla "<title_page>"

      Examples: Text Modal
                    |title_page                  |
                    |Ingrese sus datos personales|

  Scenario Outline: As usuario del sistema I want seleccionar un tipo de documento For determinar el tipo de documento que registraré
    Given que el usuario despliega el combo box de tipo de documento
     When el usuario selecciona un item
     Then el item se debe mostrar seleccionado "<item>"

      Examples: Item_selected
                |item               |
                |Cédula de identidad|

  Scenario Outline: As usuario del sistema I want ingresar un documento de identidad For registrar un documento de identificación
    Given que el usuario ingresa un ci "<ci>"
    Then "<result>"

      Examples: CI
          |ci     |result |
          |dfgdxcv|       |
          |!"=&/%/|       |
          |2535612|2535612|
