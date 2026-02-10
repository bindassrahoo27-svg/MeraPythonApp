import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SuccessApp(App):
    def build(self):
        # 1. Main Layout banaya (Vertical - upar se neeche)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # 2. Ek Label (Text) add kiya
        self.message = Label(
            text="Welcome! App Build Ho Gaya 🚀",
            font_size='24sp',
            color=(1, 1, 1, 1)  # White Color
        )
        layout.add_widget(self.message)

        # 3. Ek Button add kiya
        btn = Button(
            text="Click Me",
            font_size='20sp',
            size_hint=(1, 0.3),  # Width full, Height 30%
            background_color=(0.2, 0.6, 1, 1)  # Blue Button
        )
        btn.bind(on_press=self.update_text) # Button dabane par kya hoga
        layout.add_widget(btn)

        return layout

    # Button click hone par ye function chalega
    def update_text(self, instance):
        self.message.text = "Congratulations! ✅ Working Perfect."
        self.message.color = (0, 1, 0, 1) # Text Green ho jayega

if __name__ == '__main__':
    SuccessApp().run()

