from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window

# Ajuste para visual Mobile
Window.size = (360, 640)

KV = '''
MDScreen:
    md_bg_color: 0.02, 0.02, 0.02, 1  # Fundo Black "Deep"

    MDLabel:
        text: "MK OPTIMIZER v1"
        halign: "center"
        pos_hint: {"center_y": .9}
        font_style: "H5"
        theme_text_color: "Custom"
        text_color: 0.5, 0, 1, 1  # Roxo Neon

    MDBoxLayout:
        orientation: 'vertical'
        spacing: "12dp"
        padding: "30dp"
        pos_hint: {"center_x": .5, "center_y": .45}

        MDRaisedButton:
            text: "1. CLEAN TEMP & DNS"
            size_hint_x: 1
            md_bg_color: 0.3, 0, 0.6, 1
            on_release: app.send_cmd("clean_temp")

        MDRaisedButton:
            text: "2. MAX PERFORMANCE"
            size_hint_x: 1
            md_bg_color: 0.3, 0, 0.6, 1
            on_release: app.send_cmd("high_perf")

        MDRaisedButton:
            text: "3. RAM PURGE"
            size_hint_x: 1
            md_bg_color: 0.3, 0, 0.6, 1
            on_release: app.send_cmd("ram_boost")

        MDRaisedButton:
            text: "4. INPUT LAG FIX"
            size_hint_x: 1
            md_bg_color: 0.3, 0, 0.6, 1
            on_release: app.send_cmd("low_latency")

        MDRaisedButton:
            text: "5. GAME PRIORITY (ON)"
            size_hint_x: 1
            md_bg_color: 0.5, 0, 1, 1 # Cor de destaque
            on_release: app.send_cmd("game_mode")

    MDLabel:
        text: "STATUS: AGUARDANDO PC..."
        id: status_label
        halign: "center"
        pos_hint: {"center_y": .1}
        font_style: "Caption"
        theme_text_color: "Secondary"
'''

class MKOptimizer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def send_cmd(self, command):
        # Aqui o app envia o comando via rede para o PC
        print(f"Comando enviado: {command}")
        self.root.ids.status_label.text = f"EXECUTANDO: {command.upper()}"
        self.root.ids.status_label.theme_text_color = "Custom"
        self.root.ids.status_label.text_color = (0, 1, 0, 1) # Verde quando ativa

if __name__ == "__main__":
    MKOptimizer().run()
