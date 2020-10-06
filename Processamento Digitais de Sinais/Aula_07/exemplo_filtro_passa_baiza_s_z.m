% Exemplo de um filtro passa baixa
% H(s) = a/(s + a)
% s ----> z via Tustin
% H[z] = Y[z]/X[z] = 
% Walter 1.0

clear all; close all; clc;

% Definindo a especificação do filtro

% R = 10;
% C = 10*10^-6;
% W0 = 1/(R*C)
W0 = 2*pi*1000;

f0 = W0/(2*pi); % frequencia de sintonia em Hz

%w0 = 2*pi*f0;

%Definindo os coeficientes em s

num  = [0 W0];
den =  [1 W0];

H = tf(num,den);
bode(H)

% Aplicando a transf Biliner S->Z



Fs=8000; % Frequência de amostragem 
Ts=1/Fs; % 

Hd = c2d(H,Ts, 'tustin') % Convertendo para discreto



% Plotar em frequencia
[H, w] = freqz(Hd.Numerator{1,1},Hd.Denominator{1,1});
figure(2)
plot(w*Fs/(2*pi), 20*log10(abs(H)));
grid on

