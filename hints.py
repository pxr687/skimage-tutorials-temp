def hint_corrupted_camera():
	print("""You may want to `permute` some values.""")

def hint_split_i():
	print("""You may want to look for a NumPy function that calculates the
differences between the adjacent values in an array.""")

def hint_cat():
	print("""There is an intermediate stage needed here. You may want to 
explore colouring the image a specific way, and then inverting that image.
You can also try saving the target image, and inverting that saved image, to
see what colour you need.""")
	
def hint_camera():
    print("""Pay close attention to the `dtype` of the target image in the 
attributes printout above...you may need to investigate the `ski.util` module
to ensure your output image matches one of these attributes...you may run into
a nasty error if you try to use other methods to match this attribute...""")
	
def hint_cryptic_camera():
	    print("""In a somewhat revolutionary spirit, this exercise can be solved
by changing the order of power, using the circular mask we showed you above as
a guide...""")