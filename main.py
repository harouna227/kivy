from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class WidgetExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_text = StringProperty('1') 
    text_input_str = StringProperty('Geek')
    # slide_value_txt = StringProperty('50')
    def on_button_click(self):
        print("Button click")
        if  self.compteur_actif:
            self.compteur += 1
            self.mon_text = str(self.compteur)
        
    def on_toggle_button_state(self, widget):
        # print('Toggle state: ' + widget.state)
        if widget.state == 'normal':
            print('OFF')
            widget.text = 'OFF'
            self.compteur_actif = False
        else:
            print('ON')   
            widget.text = 'ON' 
            self.compteur_actif = True    
    
    def on_switch_active(self, Widget):
        print('Switch: ' + str(Widget.active))
        
    # def on_slider_value(self, widget):
        # print('Slider value: ' + str(int(widget.value)))
        # self.slide_value_txt = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation="rl-bt"
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)



# class GridLayoutExemple(GridLayout):
#     pass


class AnchorLayoutExemple(AnchorLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass

"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text= 'A')
        b2 = Button(text= 'B')
        b3 = Button(text= 'C')
        
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""    

class LeLabApp(App):
    pass


LeLabApp().run()