f = open('forces/0/forces.dat','r')
for indx,line in enumerate(f):
	if indx > 0:
		line = line.replace('(','').replace(')','')
		line = line.split()
		line = line[1:7]
		line = [float(i) for i in line]
		magf = ( (line[0]+line[3]) + (line[1]+line[4]) + (line[2]+line[5]) )**(0.5)
		xf   = line[0] + line[3]
		fm   = open('forces_mag','a+')
		fx   = open('forces_x','a+')
		magfstr = str(magf) + ' '
		xfstr   = str(xf) + ' '
		fm.write(magfstr)
		fx.write(xfstr)
