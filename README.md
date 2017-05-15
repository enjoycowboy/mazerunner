# mazerunner

Pgm de geração e resolução paralela de labirintos

TODO:

~> procedimento de geraçao do labirinto, sementes, aleatoriedade, import, algo do tipo;
~> engine de orientaçao basica de cada thread (i.e como discernir parede de caminho, norte sul leste oeste etc)
~> geraçao de output de cada thread (uma imagem bmp?)

# broad

  cada thread vai tentar achar uma saida, caso esteja em um beco, a thread se mata. quando houver dois ou mais caminhos, cada possibilidade é testada por um novo thread. Pra paralelizar o programa, vai ter um tempo de execução de cada thread, o que vai causar varios data race e necessidade de semáforos. (a otimização aqui vai ser mais por parte do algoritmo de solução em relaçao ao threading do que no threading em si, pra evitar chaveamento de contexto desnecessario)
  
  leitura:
  
  sobre geração de labirintos:
  http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap
  https://en.wikipedia.org/wiki/Maze_generation_algorithm
  http://stackoverflow.com/questions/38502/whats-a-good-algorithm-to-generate-a-maze
  http://rosettacode.org/wiki/Maze_generation
  
  http://www.openmp.org/wp-content/uploads/cspec20.pdf manuel do openmp
