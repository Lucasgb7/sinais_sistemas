%----------------------------------------------------
% Programa para o teste do alg LMS

% Alterado : Walter Gontijo

%----------------------------------------------------
clear;  clc;close all;


% Carregando o arquivo de entrada
 fid = fopen('ruidobranco.pcm', 'rb');
 x = fread(fid, 'short');
 fclose(fid);

% Usando um valor fixo para o mu
mu = 0.000000000005;				    % Parametro de convergencia do LMS

% Comprimento dos filtros
N = 10;			            % Comprimento do filtro W(z) 
Nmax = N;		            % valor maximo dos filtros 


N_ITER = length(x);

% Vetores utilizados
wn = zeros(N,1);			% Coeficientes de W(z)
yn = zeros(Nmax,1);		    % Vetor da saida de W(z)
x_linhan = zeros(Nmax,1);	% Vetor de entrada filtrado por F^(z)


% Definindo a planta 

Wo = [.5; .3; -.5; .8];
NWo = length(Wo);
%----------------------------------------------------------


% Dados de entrada e saida
%x = load('xn.dat');		% Vetor para o sinal de entrada x(n)
%d = load('dn.dat');		% Vetor para o sinal de desejado d(n)

e_salva = zeros(N_ITER,1);		% Vetor para o sinal de erro e(n)
y_salva = zeros(N_ITER,1);		% Vetor para o sinal de controle y(n)
w_salva = zeros(N_ITER,N);      % Para plotar o comportamento dos coeficientes




  

for k=1:N_ITER
    % Lendo a amostra de entrada
    x_new = x(k,1);
   % x_new = randn;
    
    % Filtrando o sinal de entrada x
	x_linhan(1,1) = x_new;
    
    
	% Shift e atualização do vetor x_linhan
	%x_linhan = [x_linha ; x_linhan(1:size(x_linhan,1)-1,1)];
    
    

    % Calculando o vetor de y = x'*w
    %y = x_linhan(1:N,1)'*wn;
    y = 0;
    for j= 1:N
        y = y + x_linhan(j,1) * wn(j,1);
    end
    
    y_salva(k) = y;
    
   

    % Calculando a saida da planta
    %d_new = d(k);
    %d_new = x_linhan(1:length(Wo))'*Wo;  		%----> sinal desejado
    d_new = 0;
    for j= 1:NWo
        d_new = d_new + x_linhan(j,1) * Wo(j,1);
    end
    
    
    % Cálculo do erro e(n) = d(n) - y(n)
     ee = d_new - y;
  
    e_salva(k) = ee; %Salvando o erro 
    
   
    
    % Atualizando os coeficientes do filtro usando LMS
    %wn = wn + mu*ee*x_linhan;
     for j= 1:N
        wn(j,1) = wn(j,1) + mu*ee*x_linhan(j,1);
    end
    

    w_salva(k,:) = wn;  
    
    % Atualizando o vetor x_linhan
     for j= N:-1:2
        x_linhan(j,1) = x_linhan(j-1,1);
    end
    
end

% Plotando os sinais de erro e de controle
figure(1);
plot(e_salva);grid;
title('Sinal de Erro');
xlabel('Amostras');
ylabel('Erro');

figure(2)
plot(w_salva);grid;
title('Comportamento dos Coefs');
xlabel('Amostras');

