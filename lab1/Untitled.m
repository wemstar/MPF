clc;
clear;
N=1000;
M=20000;
x=zeros(1,M);
y=zeros(1,M);
srednia=0;
for i = 1:N
  x=[x; x(i,:)+randn(1,M)];
  y=[y; y(i,:)+randn(1,M)];
  z=x(i,:).^2+y(i,:).^2;
  srednia=[srednia mean(z)];
  %plot(srednia);
  subplot(3,1,1)
  hist(x(i,:),-100:1:100);
  subplot(3,1,2)
  hist(y(i,:),-100:1:100);
  subplot(3,1,3)
  hist(sqrt(y(i,:).^2+x(i,:).^2),0:1:100);
  %axis([-50 50 -50 50]);
  pause(0.01)
end
    

