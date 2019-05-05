# -*- coding: utf-8 -*-

import random
import click
import csv


@click.group()
def cli():
    pass


def load_corpus(lang):
    with open('./src/%s.txt' % lang, 'r') as txtf:
        return txtf.read().splitlines()


def generate_bs(lang, length):
    corpus = load_corpus(lang)
    if int(length) > len(corpus):
        return
    bs = []
    n = 0
    while n < int(length):
        bs.append(random.choice(corpus))
        n += 1
    return ' '.join(bs)


@cli.command(help='generate bullshit(s)')
@click.option('--lang', help='language', type=click.Choice(['en']))
@click.option('--length', help='length of a bullshit')
@click.option('--number', help='number of bullshits')
def bullshitter(lang, length, number):
    bullshits = []
    n = 0
    while n < int(number):
        bullshits.append(generate_bs(lang, length))
        n += 1
    with open('./output/%s-%s-%s.csv' % (lang, length, number), 'w') as csvf:
        writer = csv.writer(csvf, delimiter='\n')
        writer.writerow(bullshits)


if __name__ == '__main__':
    cli()
