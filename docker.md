`# Instruções para executar a aplicação Docker

## Criar a imagem Docker
Para criar uma imagem Docker a partir dos arquivos fornecidos, siga os passos abaixo:

```bash`
docker build -t <nome da imagem> .

Substitua <nome da imagem> pelo nome desejado para a imagem.

Iniciar o contêiner Docker
Existem duas maneiras de iniciar o contêiner Docker, dependendo se você deseja executá-lo em modo interativo ou em segundo plano (daemon):

##Modo Interativo
Use o seguinte comando se desejar executar o contêiner em modo interativo:

`docker run -i -p 8080:8080 --name tableau <nome da imagem>`
