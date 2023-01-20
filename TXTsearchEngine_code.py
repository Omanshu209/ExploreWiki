from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
import wikipedia as info

KV="""
MDScreen:
	
	MDTextField:
		id:search_bar
		mode:'round' 
		hint_text:'Search..'
		icon_left:'card-search' 
		pos_hint:{'center_y':.96}
		size_hint:.9,None
		padding:15
		
	MDRoundFlatButton:
		text:'Search' 
		pos_hint:{'center_x':.5,'center_y':.89}
		size_hint:.2,.06
		on_press:
			root.ids.output_screen.text='Searching......'
		on_release:
			import wikipedia as info
			question=root.ids.search_bar.text
			try:root.ids.output_screen.text=info.summary(question)
			except:root.ids.output_screen.text=app.error_msg(question)
			
	MDRoundFlatButton:
		text:'Clear' 
		pos_hint:{'center_x':.95,'center_y':.96}
		size_hint:.09,.004
		on_release:
			root.ids.search_bar.text=""
			root.ids.output_screen.text="Zzzz......"
	
	MDCard:
		size_hint:.95,.72
		pos_hint:{'center_x':.5,'center_y':.47}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical' 
		
		MDScrollView:
			do_scroll_x:False 
			do_scroll_y:True
			MDLabel:
				size_hint_y: None
				height: self.texture_size[1]
				text_size: self.width, None
				padding: 10, 10
				bold:True 
				color:(0,.5,1,1)
				id:output_screen
				text:'Zzzz......'
				halign:'center' 
	
	MDRectangleFlatButton:
		text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
		pos_hint:{'center_x':.5,'center_y':0.045}
		size_hint:1,.05
		bold:True

"""

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style='Dark' 
		self.theme_cls.primary_palette='DeepPurple'
		return Builder.load_string(KV)
	def error_msg(self,topic):
		return f"ERROR\n\n\nPossible reasons for the error:\n\n1) No Internet Connection\n3) Spelling of \"{topic}\" might be incorrect \n2) Information might not be available for \"{topic}\""
	
if __name__=='__main__':
	MainApp().run()
