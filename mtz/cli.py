from time import sleep
import click
from pygame import mixer

# mock state for now
current_episode = 0
current_position = 0

# these will grab from cache/backend evenutally
def get_current_episode(): return current_episode
def get_current_position(): return current_position

@click.group()
def cli():
    mixer.init()

    file = "../originals/101 - All Hail the Federated Alliance!-101-all-hail-the-federated-alliance_tc.mp3"
    mixer.music.load(file)

    mixer.music.play(start=0)
    input(" ")
    pause_position = mixer.music.get_pos()
    click.echo(pause_position)
    mixer.music.stop()
    input(" ")
    mixer.music.play(start=(pause_position / 1000))
    click.echo(mixer.music.get_pos())
    input(" ")
    click.echo(mixer.music.get_pos())




@cli.command()
def play(episode: int = 0, position: float = 0):

    # TODO: queue up episode based on episode parameter
    file = "../originals/101 - All Hail the Federated Alliance!-101-all-hail-the-federated-alliance_tc.mp3"
    mixer.music.load(file)

    mixer.music.play(start=position)


    click.echo("playing...")

@cli.command()
def pause():
    click.echo("pausing...")