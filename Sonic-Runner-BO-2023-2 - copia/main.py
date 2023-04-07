from sonic_runner.components.game import Game
#En la revision del proyecto se pidió que se aumente el escudo, el cual ya fue implementado, el cual el
#power up aparece con la figura de una esmeralda, una vez tomado el personaje es inmune y da la impresion
#de que al tocar obstaculos al ser inmune, también los destrulle, cómo pasa en otros juegos.
#Al tomar el power up, en la esquina derecha nos aparecerá el tiempo que nos dura el item
if __name__ == "__main__":
    game = Game()
    game.run()
