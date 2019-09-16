def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    
    return data_transmitter


a = transmit_to_space("message")
b = transmit_to_space("message2")

a()

b()