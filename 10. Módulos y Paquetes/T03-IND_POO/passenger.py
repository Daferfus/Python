######################################
#       David Fernández Fuster       #
#       13/03/2021                   #
######################################
"""Este módulo incluye la definición para poder representar pasajeros.

    Classes:
        Passenger
"""

class Passenger:
    """Representación de un pasajero.

        Attributes:
            name (str): Nombre del pasajero.
            surname (str): Apellido del pasajero.
            id_card (str): La tarjeta de identificación del pasajero.
  
        Methods:
            passenger_data(): Muestra los datos del pasajero.
    """
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def __init__(self, name, surname, id_card):
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card
    # inicializador()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def passenger_data(self):
        """Obtiene los datos de un pasajero

            Returns:
                name (str): EL nombre del pasajero (por ejemplo, 'Jack').
                family_name (str): El apellido del pasajero (por ejemplo, 'Shephard').
                id_card (str): La tarjeta de identificación del pasajero (por ejemplo, '85994003S').
        """
        name = self.__name
        family_name = self.__surname
        id_card = self.__id_card
        passenger_data = (name, family_name, id_card)
        return passenger_data
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
# clase()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------