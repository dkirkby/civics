#!/usr/bin/env python

import re
import pathlib
import random
import shutil


def load_questions(name='questions.txt'):
    # Read the questions.
    qpat = re.compile('^([0-9]+)\. (.*)$')
    apat = re.compile('^ - (.*)$')
    questions = []
    with open('questions.txt') as f:
        for i, line in enumerate(f):
            line = line.rstrip()
            qm = qpat.match(line)
            qa = apat.match(line)
            if qm:
                n, text = qm.groups()
                current = [text]
                questions.append(current)
            elif qa:
                text = qa.group(1)
                current.append(text)
            else:
                print('Invalid line {i}: {line}')
                break
    return questions


def load_weights(name='weights.dat'):
    with open(name) as f:
        wgts = [int(line.strip()) for line in f]
    return wgts


def save_weights(wgts, name='weights.dat'):
    with open(name, 'w') as f:
        for wgt in wgts:
            print(wgt, file=f)


def main(qname='questions.txt', sname='sorted.txt', wname='weights.dat'):

    # Load the questions.
    questions = load_questions(qname)

    wfile = pathlib.Path(wname)
    if wfile.exists():
        # Load existing weights.
        wgts = load_weights(wname)
    else:
        # Initialize and save new weights.
        wgts = [5] * len(questions)
        save_weights(wgts, wname)

    # Pick a random question.
    def nextq():
        x = random.randint(0, sum(wgts) - 1)
        cumsum = 0
        for i, wgt in enumerate(wgts):
            cumsum += wgt
            if x < cumsum:
                return i
        assert False, 'should never get here'

    # Loop over questions to ask.
    n = 0
    while True:
        n += 1
        i = nextq()
        Q = questions[i]
        print(f'[{n}] {i}. {Q[0]}')
        q = input('Hit RETURN to view the answer or q to quit: ')
        if q == 'q':
            # Save questions in order of decreasing weight.
            isort = sorted(range(len(questions)), key=lambda i: wgts[i])
            with open(sname, 'w') as f:
                for j in isort:
                    Q = questions[j]
                    print(f'[{j + 1}](wgt={wgts[j]}) {Q[0]}', file=f)
                    for ans in Q[1:]:
                        print(f' - {ans}', file=f)
            break
        # Print the answers.
        for a in Q[1:]:
            print(f' - {a}')
        w0 = wgts[i]
        w = input(f'Enter the new weight 0-9 for this question or RETURN for {w0}: ')
        if w == '':
            w = w0
        wgts[i] = int(w)
        # Save the weights after each question.
        shutil.copy(wname, wname + '.bak')
        save_weights(wgts, wname)


if __name__ == '__main__':
    main()
