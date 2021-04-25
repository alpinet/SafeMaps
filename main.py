from kivy.app import App
from kivy_garden.mapview import MapView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput
from geopy.geocoders import Nominatim
from kivy_garden.mapview import MapMarkerPopup

class RootWidget(FloatLayout):
    lat = NumericProperty(33.6405)
    lon = NumericProperty(-117.8443)

    def __init__(self, **kwargs):
        super(RootWidget,self).__init__(**kwargs)
        mapview = MapView(zoom = 14, lat = self.lat, lon = self.lon)
        self.add_widget(mapview)


class MainApp(App):
    def on_enter(self,value):
        marker = MapMarkerPopup(lat = 33.6405, lon = -117.8443)
        print("enter pressed")

    def build(self):
        parent = FloatLayout()
        #initializing map
        mapview = MapView(zoom=14, lat=33.6405, lon=-117.8443)
        parent.add_widget(mapview)
        #initialize starting address text box
        starting_address = TextInput(pos = (0,60),size_hint=(.4, None), height=60, multiline=False, text="Starting Address")
        starting_address.bind(on_text_validate=self.on_enter)
        parent.add_widget(starting_address)
        #initialize destination address text box
        dest_address = TextInput(pos = (0,0),size_hint=(.4, None), height=60, multiline=False, text="Destination Address")
        dest_address.bind(on_text_validate=self.on_enter)
        parent.add_widget(dest_address)
        return parent

geolocator = Nominatim(user_agent = "tee")
location = geolocator.geocode("1338 Stanford Irvine")
print(location.address)
print((location.latitude,location.longitude))
MainApp().run()