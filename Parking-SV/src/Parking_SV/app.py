import toga
from toga.style import Pack
import os
 
 
class ParkingSV(toga.App):
 
    def startup(self):
 
        self.main_window = toga.MainWindow(
            title="Parking-SV"
        )
 
        self.cargar_html()
 
        self.main_window.show()
 
    def cargar_html(self):
 
        base_dir = os.path.dirname(__file__)
 
        resources_dir = os.path.join(
            base_dir,
            "resources"
        )
 
        html_path = os.path.join(
            resources_dir,
            "Index.html"
        )
 
        with open(html_path, "r", encoding="utf-8") as file:
            html_content = file.read()
 
        webview = toga.WebView(
            style=Pack(flex=1)
        )
 
        webview.set_content(
            f"file:///{resources_dir.replace(os.sep, '/')}/",
            html_content
        )
 
        self.main_window.content = webview
 
 
def main():
    return ParkingSV()