import pygtk,pprint
pygtk.require('2.0')
import gtk

class Calculator:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.connect("key_press_event",self.keypress)
		self.window.set_border_width(1)

		self.numpad = gtk.VBox(False,0)
		self.display = gtk.Label("0")
		self.display.show()
		self.numpad.pack_start(self.display,False,0,0)
		self.numpadrows = []
		for i in xrange(3):
			self.numpadrows.append(gtk.HBox(False,0))
			self.numpad.pack_start(self.numpadrows[i],False,0,0)
			self.numpadrows[i].show()
			for j in xrange(3):
				b = gtk.Button(str(j*3+i+1))
				b.set_size_request(55,30)
				b.show()
				self.numpadrows[i].pack_start(b,False,0,0)
		
		self.numpad.show()
		self.window.add(self.numpad)
		self.window.show()

	def main(self):
		gtk.main()

	def keypress(self,widget,data=None):
		if data.keyval == 65307: 
			gtk.main_quit()
		elif data.string in map(str,range(0,10)):
			n = int(self.display.get_text())
			self.display.set_text(str(n*10+int(data.string)))

	def destroy(self,widget,data=None):
		gtk.main_quit()

print __name__
if(__name__=='__main__'):
	app = Calculator()
	app.main()

