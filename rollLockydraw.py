import pygame

class RollLockydraw():
	"""docstring for RollLockydraw"""
	def __init__(self, list, ttf):
		self.list = list
		self.ptr = 3
		self.ptr_old = self.ptr
		self.ttf = ttf
		self.color1 = (0, 255, 0)
		self.color_ptr = (0, 255, 0)
		self.color_line = (12, 15, 17)
		self.fontsize1 = 30 
		self.fontsize_ptr = 40
		self.showsize = 3 
		self.fontinterval = 0
		self.bg_width = 0
		self.bg_height = 0
		self.height0 = 0
		self.width_ptr = 0
		self.bg_height_flag = 0
		self.bg_width_flag = 0
		self.rolling_ptr = 0
		self.pos = [0, 0]
		self.subsurface0 = 0
		self.subsurface1 = 0
		self.subsf_pos0 = [0 ,0]
		self.subsf_pos1 = [0 ,0]
		self.subsf_rect = [0 ,0]
		self.list0 = []
		self.list1 = []
		self.lenstname = self.getlenstname(self.list)
		print self.lenstname

		self.sound = 0
	def getlenstname(self, list):
		lenst = ""
		for name in list:
			if len(lenst)<len(name):
				lenst = name
		return lenst

	def setsound(self, sound):
		self.sound = pygame.mixer.Sound(sound)
	def blit(self, surface, pos):
		#bg
		#if self.bg_height !=0 and self.bg_width!=0 and self.width_ptr!=0:
		#	pygame.draw.rect(surface,[255,0,0],[pos[0]-self.width_ptr/2,pos[1]+40,self.bg_width,self.bg_height],0)
		# blit 0
		# print self.height0, self.fontinterval
		# if self.height0!=0:
		if len(self.list)==0:
			return 
		elif len(self.list)==1:
				self.rolling_ptr = 0
		pos_y = pos[1] - (self.height0+self.fontinterval)
		if self.rolling_ptr >=self.height0+self.fontinterval:
			#self.ptr -= 1
			self.subptr(1)
			self.rolling_ptr = 0
		elif self.rolling_ptr<= -(self.height0+self.fontinterval):
			#self.ptr += 1
			self.addptr(1)
			self.rolling_ptr = 0
		if pos!=self.pos:
			self.rolling_ptr = 0	
		y = pos_y+self.rolling_ptr
		#
		font = pygame.font.Font(self.ttf, self.fontsize1)
		if self.rolling_ptr==0:
			self.list0 = range(0, self.showsize/2+1)
			for k in range(0, self.showsize/2+1):
				ptr0 = self.ptr-k-1
				ptr0 %= len(self.list)
				self.list0[-k-1] = self.list[ptr0]
		for name in self.list0:
			# print name
			text_surface = font.render(name, True, self.color1)
			x = pos[0] - text_surface.get_width()/2
			if pos == self.pos:
				surface.blit(text_surface, (x, y))
			y += text_surface.get_height()+self.fontinterval
			self.height0 = text_surface.get_height()
		#
		font_ptr = pygame.font.Font(self.ttf, self.fontsize_ptr)
		text_surface = font_ptr.render( self.list[self.ptr], True, self.color_ptr)
		x = pos[0] - text_surface.get_width()/2
		if pos == self.pos:
			surface.blit(text_surface, (x, y))
			if self.ptr != self.ptr_old :
				self.ptr_old = self.ptr
				if self.sound!=0:
					self.sound.stop()
					self.sound.play()
					print self.ptr

		pygame.draw.line(surface,self.color_line,(self.subsf_pos0[0],y-self.rolling_ptr),(self.subsf_pos0[0]+self.subsf_rect[0],y-self.rolling_ptr),3)		
		y += text_surface.get_height()+self.fontinterval
		pygame.draw.line(surface,self.color_line,(self.subsf_pos0[0],y-self.rolling_ptr),(self.subsf_pos0[0]+self.subsf_rect[0],y-self.rolling_ptr),3)		

		#
		if self.bg_width_flag==0:
			self.bg_width_flag = 1
			self.bg_width = text_surface.get_width()
			self.width_ptr = text_surface.get_width()
		#
		font = pygame.font.Font(self.ttf, self.fontsize1)
		if self.rolling_ptr==0:
			self.list1 = range(0, self.showsize/2+1)
			for k in range(0, self.showsize/2+1):
				ptr0 = self.ptr+k+1
				ptr0 %= len(self.list)
				self.list1[k] = self.list[ptr0]
		for name in self.list1:
			text_surface = font.render(name, True, self.color1)
			x = pos[0] - text_surface.get_width()/2
			if pos == self.pos:
				surface.blit(text_surface, (x, y))
			y += text_surface.get_height()+self.fontinterval
		if self.bg_height_flag==0:
			self.bg_height_flag = 1
			self.bg_height = y - self.fontinterval
		#
		if self.height0!=0 and pos != self.pos:
			self.pos = pos
			pos_y = pos[1] - 2*(self.height0+self.fontinterval)
			text_surface = font.render(self.lenstname, True, self.color1)
			width = text_surface.get_width()
			self.subsf_pos0 = [pos[0]-width/2,pos_y]
			self.subsf_pos1 = [pos[0]-width/2,y-2*(self.height0+self.fontinterval)]
			self.subsf_rect = [width, 2*(self.height0+self.fontinterval)]
			self.subsurface0 = surface.subsurface([self.subsf_pos0[0],self.subsf_pos0[1],self.subsf_rect[0],self.subsf_rect[1]]).copy()
			self.subsurface1 = surface.subsurface([self.subsf_pos1[0], self.subsf_pos1[1], self.subsf_rect[0],self.subsf_rect[1]]).copy()
		#
		surface.blit(self.subsurface0, self.subsf_pos0)
		surface.blit(self.subsurface1, self.subsf_pos1)
		# pygame.draw.line(surface,(0,255,0),self.subsf_pos1,(self.subsf_pos1[0]+self.subsf_rect[0],self.subsf_pos1[1]),1)
		# pygame.draw.line(surface,(0,255,0),(self.subsf_pos1[0], self.subsf_pos1[1]+self.subsf_rect[1]),(self.subsf_pos1[0]+self.subsf_rect[0],self.subsf_pos1[1]+self.subsf_rect[1]),1)

	def getptr(self):
		return self.ptr
	def getptrname(self):
		return self.list[self.ptr]
	def addptr(self, n):
		self.ptr += n
		self.ptr %= len(self.list)
	def subptr(self, n):
		self.ptr -= n
		self.ptr %= len(self.list)
	def rolling(self, n):
		self.rolling_ptr += n
	def getrolling(self):
		return self.rolling_ptr
	def remove(self, x):
		self.list.remove(x)
		a = len(self.list)
		if a!=0:
			self.ptr %= a
