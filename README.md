# BSer

## What is BSer

A bullshit generator. 

## How BSer works

Generate non-sense sentence(s) of the required length by joining the words randomly selected from the corpus.

## Target usage

@nlper: random corpus as the baseline in model verification.

@designer: non-sense content to fill in the blank(s) for preview.

@blogger: anti-search.

...

## How to use BSer

```
$ python bs.py bullshitter --help

  generate bullshit(s)

Options:
  --lang [en]    language
  --length TEXT  length of a bullshit
  --number TEXT  number of bullshits
```

For an output, please refer to '/output/en-20-3.csv'.
  
## TODO

- support more languages

## Author

yuqing.ji@outlook.com