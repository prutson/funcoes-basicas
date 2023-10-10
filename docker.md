# Instruções para executar a aplicação Docker

## Criar a imagem Docker
Para criar uma imagem Docker a partir dos arquivos fornecidos, siga os passos abaixo:

`docker build -t <nome da imagem> .`

Substitua **'<nome da imagem>'** pelo nome desejado para a imagem.

## Iniciar o contêiner Docker
Existem duas maneiras de iniciar o contêiner Docker, dependendo se você deseja executá-lo em modo interativo ou em segundo plano (daemon):

### Modo Interativo
Use o seguinte comando se desejar executar o contêiner em modo interativo:

`docker run -i -p 8080:8080 --name tableau <nome da imagem>`

Explicação do comando:

**'docker run'**: Inicia um novo contêiner Docker.
**'-i'**: Esta opção torna o contêiner "interativo", permitindo entrada do terminal. No entanto, como você está usando o Gunicorn para servir uma aplicação web, essa opção pode não ser estritamente necessária.
**'-p 8080:8080'**: Mapeia a porta 8080 do host para a porta 8080 do contêiner, permitindo o acesso à aplicação dentro do contêiner a partir do seu host.
**'--name tableau'**: Define o nome do contêiner como "tableau", permitindo que você faça referência a ele por esse nome.
<nome da imagem>: Especifica o nome da imagem Docker a ser usada para criar o contêiner.
Modo Daemon (Segundo Plano)
Use o seguinte comando se desejar executar o contêiner em segundo plano (modo daemon):
