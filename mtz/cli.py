import click
import podcastparser
import urllib.request


@click.group()
def cli():
    click.echo("no args")
    feedurl = 'https://feeds.simplecast.com/ZL7iUDiH'

    parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))


@click.command()
def play():
    click.echo("playing...")

@click.command()
def play():
    click.echo("pausing...")