from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.popup import Popup
import webbrowser as wb
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

class URLPopup(Popup):
    pass

class MainApp(MDApp):
	
	def build(self):
		self.wikipedia = WikipediaQueryRun(api_wrapper = WikipediaAPIWrapper())
		self.theme_cls.theme_style = 'Dark' 
		self.theme_cls.primary_palette = 'DeepPurple'
		return Builder.load_file("Design.kv")
		
	def search(self):
		try:
			self.root.ids.output_screen.text = self.wikipedia.run(self.root.ids.search_bar.text)
		except Exception:
			self.root.ids.output_screen.text = self.error_msg()
	
	def error_msg(self):
		return "ERROR\n\n\nPossible reasons for the error:\n\n1) No Internet Connection\n2) The server might be under maintainance"
		
	def on_url_button_press(self):
	    popup = URLPopup()
	    popup.open()
	    
	def search_url(self,url):
		if 'https' in url:
			try:
				wb.open(url)
			except Exception:
				pass
		else:
			try:
				wb.open("https://"+url)
			except Exception:
				pass
	
if __name__ == '__main__':
	MainApp().run()