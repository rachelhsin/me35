clc
clear

L1 = 7;
L2 = 13;

%determining path
xpos = 0:10;
ypos = [0 3 5 6 5.5 4.5 3.5 2 1.5 1 0];
cs = spline(xpos,[0 ypos 0]);

steps = 40; 
x = linspace(0,10,steps);
yy = ppval(cs,x);

%plotting path
y = yy-16;
figure(1)
plot(xpos,ypos,'o',x,yy,'-')
ylim([0 16])
xlabel('x displacement(cm)')
ylabel('y displacement(cm)')
title('Leg Path')


% finding angles using IK
for i = 1:length(x)
    
    % formulas
    L3=sqrt(x(i)^2+y(i)^2);
    b1 = (-(L2^2-L1^2-L3^2)/(2*L1*L3));
    a1 = atan2(sqrt(1-b1^2),b1);
    theta1(i) = (atan2(y(i),x(i))-a1)*(180/pi);
    b2 = (-(L3^2-L1^2-L2^2)/(2*L1*L2));
    a2 = atan2(sqrt(1-b2^2),b2);
    theta2(i) = (pi-a2)*(180/pi);

    % motor angles
    if i > 1
        theta11(i) = theta1(i)-theta1(i-1);
        theta22(i) = theta2(i)-theta2(i-1);
    end
    theta11(1) = theta1(1);
    theta22(1) = theta2(1);

    % animation of graph
    figure(2)
    clf
    X = [0 L1*cos(theta1(i)*(pi/180)) x(i)];
    Y = [0 L1*sin(theta1(i)*(pi/180)) y(i)];
    xlim([-16 16])
    ylim([-16 16])
    hold on
    plot(X,Y)

    pause(0.05)
end

% Export angles for MQTT
theta1string = sprintf('%.3f,' , theta1);
theta1string= theta1string(1:end-1);
theta2string = sprintf('%.3f,' , theta2);
theta2string = theta2string(1:end-1);
disp(theta1string)
disp(theta2string)