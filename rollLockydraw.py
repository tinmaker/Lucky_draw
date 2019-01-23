import pygame

class RollLockydraw():
	"""docstring for RollLockydraw"""
	def __init__(self, list, ttf):
		self.list = list
		self.ptr = 3
		self.ttf = ttf
		self.color1 = (12, 15, 17)
		self.color_ptr = (102, 15, 17)
		self.fontsize1 = 20 
		self.fontsize_ptr = 40
		self.showsize = 7 
		self.fontinterval = 10
		self.bg_width = 0
		self.bg_height = 0
		self.width_ptr = 0
		self.bg_height_flag = 0
		self.bg_width_flag = 0
		self.rolling_ptr = 0
	def blit(self, surface, pos):
		#bg
		if self.bg_height !=0 and self.bg_width!=0 and self.width_ptr!=0:
			pygame.draw.rect(surface,[255,0,0],[pos[0]-self.width_ptr/2,pos[1]+40,self.bg_width,self.bg_height],0)
		# blit 0
		font = pygame.font.Font(self.ttf, self.fontsize1)
		list = range(0, self.showsize/2)
		for k in range(0, self.showsize/2):
			ptr0 = self.ptr-k-1
			ptr0 %= len(self.list)
			list[-k-1] = self.list[ptr0]
		y = pos[1]
		for name in list:
			# print name
			text_surface = font.render(name, True, self.color1)
			x = pos[0] - text_surface.get_width()/2
			surface.blit(text_surface, (x, y))
			y += text_surface.get_height()+self.fontinterval


		# print self.list[self.ptr]
		font_ptr = pygame.font.Font(self.ttf, self.fontsize_ptr)
		text_surface = font_ptr.render( self.list[self.ptr], True, self.color_ptr)
		x = pos[0] - text_surface.get_width()/2
		surface.blit(text_surface, (x, y))
		y += text_surface.get_height()+self.fontinterval
		if self.bg_width_flag==0:
			self.bg_width_flag = 1
			self.bg_width = text_surface.get_width()
			self.width_ptr = text_surface.get_width()

		font = pygame.font.Font(self.ttf, self.fontsize1)
		for k in range(0, self.showsize/2):
			ptr0 = self.ptr+k+1
			ptr0 %= len(self.list)
			list[k] = self.list[ptr0]
		for name in list:
			# print name
			text_surface = font.render(name, True, self.color1)
			x = pos[0] - text_surface.get_width()/2
			surface.blit(text_surface, (x, y))
			y += text_surface.get_height()+self.fontinterval
		if self.bg_height_flag==0:
			self.bg_height_flag = 1
			self.bg_height = y - self.fontinterval

		# pass
	def setptr(self, ptr):
		self.ptr = ptr
	def addptr(self, n):
		self.ptr += n
		self.ptr %= len(self.list)
	def subptr(self, n):
		self.ptr -= n
		self.ptr %= len(self.list)
	def rolling_add(self, n):
		self.rolling_ptr += n
		self.ptr %= len(self.list)

	def remove(self, x):
		self.list.remove(x)
