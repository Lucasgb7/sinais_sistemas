% Programa exemplo para PDS

% O programa executa os seguintes passos:
% Limpa as variaveis, figuras e console,
% Le o arquivo de entrada
% Executa o processamento: le amostra, multiplica por uma constante e escreve no vetor de saida
% Escreve no arquivo de saida

% Walter - versao 1.0
clear all;close all;clc;



% lendo arquivo binario
fid = fopen('alo.pcm', 'rb');
s = fread(fid, 'int16');
fclose(fid);

itera = length(s);

subplot(2,1,1);
plot(s);
grid on;
title('Sinal de entrada');

% Salvar valores intermediarios   
sav_y = zeros(itera,1);

ganho = .5;


% Executa o processamento   
 	for j=1:itera,    										
		x = s(j,1);     % lendo amostras do vetor de entrada
        
        y = ganho*x;									
      
        sav_y(j,1) = y;
            
    end
    
  % Plotando a sa�da
 subplot(2,1,2);
 plot(sav_y, 'r');
 title('Saida');
 xlabel('Numero de amostras');
 ylabel('Amplitude da saida');
 grid on;
 
 % Salvando o arquivo de saida
 fid = fopen('sinal_saida.pcm', 'wb');
fwrite(fid,sav_y,'int16');
fclose(fid);
   
  
   
