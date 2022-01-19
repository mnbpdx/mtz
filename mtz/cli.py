import click
import podcastparser
import urllib.request


@click.group()
def cli():
    click.echo("no args")
    feedurl = 'https://feeds.simplecast.com/ZL7iUDiH'

    parsed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))

    file = open("feed.xml", "w")
    file.write(parsed)
    file.close()


@cli.command()
def play():
    click.echo("playing...")

@cli.command()
def play():
    click.echo("pausing...")