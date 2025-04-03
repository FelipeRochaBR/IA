Projeto - Carro automático

Este projeto implementa e exibe a movimentação de um carro em um grid 10x15, utilizando diferentes algoritmos de busca para encontrar o melhor caminho entre um ponto inicial e um objetivo.

Tecnologias utilizadas:

Backend: Python (Flask)

Frontend: HTML, CSS e JavaScript

Para rodar:

O projeto utiliza o Flask para criar uma aplicação web em um servidor local. Portanto, dentro da pasta do projeto, abra o terminal e digite o comando:

python main.py
(Caso o Flask não esteja instalado, digite o comando)
pip install flask
O servidor será iniciado e o endereço fornecido será: http://127.0.0.1:7000

Acesse esse endereço no navegador e comece a testar o programa.

Algumas restrições do programa: O carro não irá rodar se:

A célula de origem for um obstáculo.

A célula de destino for um obstáculo.

A célula de origem ou destino estiver cercada por obstáculos.

Os obstáculos são gerados automaticamente; basta recarregar a página.