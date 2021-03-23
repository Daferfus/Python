######################################
#       David Fernández Fuster       #
#       13/03/2021                   #
######################################
"""Este módulo incluye la definición para poder representar vuelos.

    Classes:
        Flight
"""
from pprint import pprint

class Flight:
    """Representación de un vuelo.

        Attributes:
            number (str): Número de vuelo.
            aircraft (Aircraft): Características del avión.
            seating (lista de diccionarios): Plan de asientos del avión.

        Getters:
            get_number()
            get_aircraft_model()

        Methods:
            allocate_passenger(): Asigna un pasajero en un asiento.
            reallocate_passenger(): Reasigna un pasajero a un nuevo asiento.
            num_available_seats(): Devuelve el número de asientos disponibles del avión.
            print_seating(): Imprime el plan de asientos del vuelo.          
            print_boarding_cards(): Imprime las tarjetas de embarque de los pasajeros.
            __parse_seat(): Divide un designador de asiento en filas y letras.
            __passenger_seats(): Iterar las ubicaciones de los asientos ocupados. 
    """
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def __init__(self, number, aircraft):
        if (number[0:2].isalpha()) and (number[0:2].isupper()) and (number[-1].isdigit()):
            if (int(number[2:len(number)]) < 9999):
                self.__number = number
        else:
            raise ValueError("El número asignado no cumple con los requisitos establecidos de dos letras mayuscula y número menor que 9999.")
        self.__aircraft = aircraft
        self.__seating = self.__aircraft.seating_plan()
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    # Getters
    #-----------------------------------------------------------------------------------------------------------
    def get_number(self):
        return self.__number
    # ()

    def get_aircraft_model(self):
        return self.__aircraft.get_model()
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    # Métodos
    #-----------------------------------------------------------------------------------------------------------
    def allocate_passenger(self, seat, passenger):
        """Asigna un pasajero en un asiento.

        Args:
            seat (str): Asiento a asignar al pasajero.
            passenger (tuple): Datos del pasajero.
        """
        parsed_seat = self.__parse_seat(seat)
        dictionaries = self.__seating
        new_dic = {}
        row = dictionaries[int(parsed_seat[0])]
        valor = row[parsed_seat[1]]
        if valor != None:
            raise ValueError("El asiento no está vacío.")
        else:
            for key, value in dictionaries[int(parsed_seat[0])].items():
                if(value == None):
                    if(key == parsed_seat[1]):
                        new_dic[key] = passenger
                    else:
                        new_dic[key] = None
                    # if()
                else:
                    new_dic[key] = value
                # if()
            # for()

            dictionaries[int(parsed_seat[0])] = new_dic
            self.__seating[int(parsed_seat[0])] = dictionaries[int(parsed_seat[0])]
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def reallocate_passenger(self, from_seat, to_seat):
        """Reasigna un pasajero a un nuevo asiento.

        Args:
            from_seat (str): Asiento original del pasajero.
            to_seat (str): Nuevo asiento al que se le quiere asignar al pasajero.
        """

        #-----------------------------------------------------------------------------------------------------------
        # Sacar al Pasajero de su Asiento Original
        #-----------------------------------------------------------------------------------------------------------
        previous_seat = self.__parse_seat(from_seat)
        previous_row = self.__seating[int(previous_seat[0])]
        values = previous_row[previous_seat[1]]
        if values == None:
            raise ValueError("El asiento no está ocupado.")
        else:
            previous_row[previous_seat[1]] = None


            #-----------------------------------------------------------------------------------------------------------
            # Asignar Pasajero a Nuevo Asiento
            #-----------------------------------------------------------------------------------------------------------
            new_seat = self.__parse_seat(to_seat)
            dictionaries = self.__seating
            new_dic = {}

            for key, value in dictionaries[int(new_seat[0])].items():
                if(value == None):
                    if(key == new_seat[1]):
                        new_dic[key] = values
                    else:
                        new_dic[key] = None
                    # if()
                else:
                    new_dic[key] = value
                # if()
            # for()

            dictionaries[int(new_seat[0])] = new_dic
            self.__seating[int(new_seat[0])] = dictionaries[int(new_seat[0])]
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def num_available_seats(self):
        """Devuelve el número de asientos disponibles del avión.

        Returns:
            num_available_seats (int): Número de asientos disponibles.
        """
        num_available_seats = 0
        
        for seat in self.__seating[1:]:
            for key, value in seat.items():
                if value == None:
                    num_available_seats+=1
                # if()
            # for()
        # for()

        return num_available_seats
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def print_seating(self):
        """Imprime el plan de asientos del vuelo.
            Ejemplo de una Fila:
                {A: None, B: None, C: None, D: None, E: None, F: None}
        """
        #-----------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------
        print("-------")
        print("Seating")
        print("-------")
        #-----------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------
        
        pprint(self.__seating)
    
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def print_boarding_cards(self):
        """Imprime en consola la tarjeta de embarque de cada pasajero.
            Ejemplo de una tarjeta de embarque:
                ----------------------------------------------------------
                |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
                ----------------------------------------------------------
        """
        #-----------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------
        print("-------")
        print("Boarding Card")
        print("-------")
        #-----------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------
        
        generator = self.__passenger_seats()
        
        for seat in self.__seating[1:]:
            
            for key, value in seat.items():
                if value != None:
                    data = next(generator)
                    passenger_data = data[0]
                    pprint("-----------------------------------------------")
                    pprint("   " + passenger_data[0] + " " + passenger_data[1] + " " + passenger_data[2] + " " + str(data[1]) + "" + data[2] + " " + self.get_number() + " " + self.get_aircraft_model() + " ")
                    pprint("-----------------------------------------------")
                # if()
            # for()
        # for()
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def __parse_seat(self, seat):
        """Divide un designador de asiento en filas y letras.

        Args:
            seat (str): El designador de asiento (por ejemplo, "12C")

        Returns:
            row (str): Número de fila (por ejemplo, "12)
            letter (str): Letra representado el asiento (por ejemplo, "C")
        """
        if (seat[-1].isalpha()) and (int(seat[0:2].isalnum()) <= self.__aircraft.num_seats()):
            row = "".join([num for num in seat if num.isdigit()])
            letter = "".join([letter for letter in seat if letter.isalpha()])
            return row, letter
        else:
            raise ValueError("El asiento no existe o está mal escrito.")

    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
    def __passenger_seats(self):
        """Iterar las ubicaciones de los asientos ocupados.

        Yields:
            value (tuple): Datos del pasajero.
            row (int): Número de fila de asientos.
            key (str): Letra de asiento.
        """
        row = 0
        for seat in self.__seating[1:]:
            row+=1
            for key, value in seat.items():
                if value != None:
                    yield value, row, key
    # ()
    #-----------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------
# class()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------