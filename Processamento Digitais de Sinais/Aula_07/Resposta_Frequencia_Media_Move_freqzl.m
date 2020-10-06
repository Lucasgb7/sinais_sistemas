% Resposta de frequência da média móvel
clc; close all; clear all;

% Variaveis
passo = pi/1000;
w = 0:passo:pi;
L = 8;
Fs = 8000;

% Numerador e Denominador
num = sin(w*L/2);
den = sin(w/2);

% Equação Base
temp = num./den;

% Rad
X = (1/L) *( abs(temp));
subplot(3,1,1);
plot(w,X);
xlabel('Frquência');
title('Frequêncua Rad');
grid on;

% Hz
F_Hz = (w/pi)*(Fs/2);
subplot(3,1,2);
plot(F_Hz,X);
xlabel('Frequência');
title('Frequência em Hz');
grid on;

% Db
X_Db = 20* log10 (X);
subplot(3,1,3);
plot(F_Hz,X_Db);
ylabel('Atenuação DB');
xlabel('Frequência');
title('Frequência em Hz');
grid on;
 axis([0 4000 -70 0]);
 
figure(2)
% Usando freqz para obter a resposta em frequencia
%num = [ .25 .25 .25 .25];
num = zeros(1,L);
num(1,:) = 1/L;
den = [1];
[H, Freq] = freqz(num,den,Fs);
plot(Freq*Fs/(2*pi), 20*log10(abs(H)));
title('Magnitude da resposta em frequencia')
grid on;


 