from random import choice

airport_data = {}
def add_airport():
    icao_code = input('Enter the ICAO code of the airport: ')
    airport_name = input('Enter airport name: ')

    airport_data[icao_code] = airport_name
    print(f'Airport {airport_name} with ICAO code {icao_code} added.\n')

def fetch_airport():
    icao_code = input('Enter the ICAO code of the airport: ').upper()
    if icao_code in airport_data:
        print(f'The airport with ICAO code {icao_code} is {airport_data[icao_code]}.\n')
    else:
        print(f'No airport found with ICAO code {icao_code}.\n')
def main():
    while True:
        print('Choose an option: ')
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input('Enter  your choice (1/2/3): ')
        if choice == '1':
            add_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please enter 1,2,3.\n')

main()
