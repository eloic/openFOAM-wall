file_forcesdat = open('forces/0/forces.dat','r')
tt, ff = [], []
for indx,line in enumerate(file_forcesdat):
	if indx > 0:
          	line = [float(i) for i in line.replace('(','').replace(')','').split()]
		t    = line[0]
		f    = line[1] + line[4] # directional along the x-axis, sum of pressure and viscous forces
		tt  += [t]
		ff  += [f]
file_fx = open('ff_x','w+')
file_ft = open('ff_time','w+')
file_fx.write('\n'.join([str(i) for i in ff]))
file_ft.write('\n'.join([str(i) for i in tt]))
