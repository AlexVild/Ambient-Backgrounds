import sys
import ctypes
from weather import Weather, Unit

class AmbientBackgrounds:
    def __init__(self):
        self.selection = None
        self.zip_code = None
        self.unit = None
        self.min_temp = None
        self.dst = None
        self.backgrounds = {
            'day': {
                'warm': {
                    'sunny' : [],
                    'rainy' : []
                },
                'cool': {
                    'sunny' : [],
                    'snowing' : []
                }
            },
            'night': {
                'warm': {
                    'clear' : [],
                    'rainy' : []
                },
                'cool': {
                    'clear' : [],
                    'snowing' : []
                }
            }
        }

    def begin(self):
        while True:
            print('Make your selection: ')
            print('0 - Set up')
            print('1 - Change background')
            selection = raw_input('Selection: ')
            self.handle_selection(selection)

    def handle_selection(self, selection):
        if selection == '0':
            self.setup()
        elif selection == '1':
            self.change_background()
        elif selection == 'q' or selection == 'Q':
            self.quit()
        else:
            print('\nInvalid selection. Please try again!\n')

    def setup_menu(self):
        print('\n--- AMBIENT BACKGROUNDS SETUP ---')

        print('0 - Set up wizard')

        if self.zip_code:
            print('1 - Edit zip code (Current is ',self.zip_code,')')
        else :
            print('1 - Edit zip code')

        if self.unit:
            print('2 - Change temperature unit (Current is ',self.unit,')')
        else:
            print('2 - Change temperature unit')

        if self.min_temp:
            print('3 - Change cold temp threshold (Current is ',self.min_temp,')')
        else:
            print('3 - Change cold temp threshold')

        if self.dst:
            print('4 - Change daylight savings time settings (Currently, daylight savings time does occur in your location)')
        else:
            print('4 - Change daylight savings time settings (Currently, daylight savings time does not occur in your location)')

        print('5 - Edit background selection')

        print('6 - Exit setup')

        selection = raw_input('Selection: ')

    def setup(self):
        self.setup_menu()
        pass

    def change_background(self):
        print('background')

    def quit(self):
        sys.exit()

# SPI_SETDESKWALLPAPER = 20
# ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'E:\Alex Vild\Pictures\Desktop Wallpapers\Other\Hayley Williams 2.jpg' , 0)
#
# weather = Weather(unit=Unit.FAHRENHEIT)
#
# lookup = weather.lookup(43215)
# condition = lookup.condition
#
# print(condition.text)
