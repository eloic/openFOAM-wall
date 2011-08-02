fid = fopen('ff_x','r');
ff = fscanf(fid, '%f\n');
fclose(fid);

fid = fopen('ff_time');
tt = fscanf(fid, '%f\n');
fclose(fid);

plot(tt,ff,'k-','linewidth',2)
xlabel('time (seconds)','fontsize',15)
ylabel('force (Newtons)','fontsize',15)
title('Forces on a rigid wall using interDyMFoam','fontsize',15)
axis([0 10 0 475])

print -dpng 'I:\Rigid wall results\1-processor\rigid-wall-interDyMFoam\ff_interDyMFoam.png'
