import time
import scrollphat as s

s.clear()
s.set_brightness(2)

#time.sleep(2)

# draw arrow
s.set_pixel(5, 4, 1)
s.set_pixel(5, 0, 1)
s.set_pixel(4, 1, 1)
s.set_pixel(4, 3, 1)
s.set_pixel(3, 2, 1)
s.set_pixel(4, 2, 1)
s.set_pixel(5, 2, 1)
s.set_pixel(6, 2, 1)
s.set_pixel(7, 2, 1)
s.set_pixel(8, 2, 1)
s.set_pixel(9, 2, 1)
s.set_pixel(10, 2, 1)


while True:
	s.scroll()
	s.update()
	time.sleep(0.05)




















