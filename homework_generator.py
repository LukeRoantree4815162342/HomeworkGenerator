from md_components import MD
from topics import *
import numpy as np
import argparse as ap
from gooey import Gooey, GooeyParser

topic_options = ['WholeAddition',
                 'NegativeNumberAddition',
                 'DecimalAddition',
                 'WholeSubtraction',
                 'NegativeNumberSubtraction',
                 'DecimalSubtraction']
topic_options = sorted(topic_options)

@Gooey
def main():
    parser = GooeyParser()

    parser.add_argument('title', type=str, help='Title: Topic, Homework No., Due Date')
    parser.add_argument('topic', type=str, help='Topic to generate questions for', choices=topic_options, nargs='+', widget='Dropdown')
    parser.add_argument('--number', '-n', type=int, help='number of questions (default is 10)', default=10)

    args = parser.parse_args()
    t = False

# Re-do this control structure as a hash
    if args.topic[0] == 'WholeAddition':
        t = WholeAddition
    elif args.topic[0] == 'NegativeNumberAddition':
        t = NegativeNumberAddition
    elif args.topic[0] == 'DecimalAddition':
        t = DecimalAddition
    elif args.topic[0] == 'WholeSubtraction':
        t = WholeSubtraction
    elif args.topic[0] == 'NegativeNumberSubtraction':
        t = NegativeNumberSubtraction
    elif args.topic[0] == 'DecimalSubtraction':
        t = DecimalSubtraction

    print('Generating questions...')

    questions, answers = [],[]
    for i in range(args.number):
        q,a = t.make_qa_pair()
        questions.append(q+'\n')
        answers.append(a)

    print('making homework sheet...')

    with open('Homework_{}.md'.format(args.title), 'w') as f:
        f.write(MD.to_title(args.title))
        f.write('\n')
        f.write(MD.to_subtitle(args.topic))
        f.write('\n')
        f.write("{}".format('\n\n'.join(questions)))

    print('making solutions sheet...')
    
    with open('Sols_{}.md'.format(args.title), 'w') as f2:
        f2.write(MD.to_title(args.title))
        f2.write('\n')
        f2.write(MD.to_subtitle(args.topic))
        f2.write('\n\n')
        if t.is_decimal:
            f2.write("{}".format('\n'.join(['{:.1f}\n'.format(a) for a in answers])))
        else:    
            f2.write("{}".format('\n'.join(['{}\n'.format(a) for a in answers])))

if __name__ == '__main__':
    main()
