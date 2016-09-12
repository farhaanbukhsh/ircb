# -*- coding: utf-8 -*-
import click

from ircb.bouncer import runserver
from ircb.web.app import runserver as webserver


@click.group(name='run')
def run_cli():
    """Implement run commands"""
    pass


@click.command(name='allinone')
@click.option('--host', '-h', default='0.0.0.0',
              help='Host, defaults to 0.0.0.0')
@click.option('--port', '-p', default=9000,
              help='Port, defaults to 9000')
def run_allinone(host, port):
    """Run ircb in a single process"""
    runserver(host, port, 'allinone')


@click.command(name='stores')
def run_stores():
    """Run ircb stores"""
    import ircb.stores
    import ircb.stores.base
    ircb.stores.initialize()
    ircb.stores.base.dispatcher.run_forever()


@click.command(name='bouncer')
@click.option('--host', '-h', default='0.0.0.0',
              help='Host, defaults to 0.0.0.0')
@click.option('--port', '-p', default=9000,
              help='Port, defaults to 9000')
def run_bouncer(host, port):
    """Run ircb bouncer"""
    runserver(host, port)


@click.option('--host', '-h', default='0.0.0.0',
              help='Host, defaults to 0.0.0.0')
@click.option('--port', '-p', default=10000,
              help='Port, defaults to 10000')
@click.command(name='web')
def run_web(host, port):
    """Run ircb web server"""
    webserver(host, port)

run_cli.add_command(run_allinone)
run_cli.add_command(run_bouncer)
run_cli.add_command(run_stores)
run_cli.add_command(run_web)
