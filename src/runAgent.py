from QAgent import *
from TrainingQAgent import *

def runAgent(QAInstrument, file):

    with open("statFiles/" + file + ".txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        chord = ""
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                chord = row[0]
                training(QAInstrument.instrument, chord, 1000, QAInstrument)






    '''
    pred_note_S = exploiting_note('C5,E4,B-3,D3', QASoprano)
    pred_note_A = exploiting_note('C5,E4,B-3,D3', QAAlto)
    pred_note_T = exploiting_note('C5,E4,B-3,D3', QATenore)
    pred_note_B = exploiting_note('C5,E4,B-3,D3', QABasso)


    print('Nota predetta Soprano:' + pred_note_S)
    print('Nota predetta Alto:' + pred_note_A)
    print('Nota predetta Tenore:' + pred_note_T)
    print('Nota predetta Basso:' + pred_note_B)
    '''


QASoprano = QAgent('Soprano')
QAAlto = QAgent('Alto')
QATenore = QAgent('Tenore')
QABasso = QAgent('Basso')

runAgent(QASoprano, 'Soprano')
runAgent(QAAlto, 'Alto')
runAgent(QATenore, 'Tenore')
runAgent(QABasso, 'Basso')

print(QASoprano.Q)
print(QAAlto.Q)
print(QATenore.Q)
print(QABasso.Q)

print('Size Q-Table Soprano:')
print(len(QASoprano.Q[0]))
print('Size Q-Table Alto:')
print(len(QAAlto.Q[0]))
print('Size Q-Table Tenore:')
print(len(QATenore.Q[0]))
print('Size Q-Table Basso:')
print(len(QABasso.Q[0]))

print('Nota con max accurancy Soprano:')
print(get_max_note(QASoprano))
print('Nota con max accurancy Alto:')
print(get_max_note(QAAlto))
print('Nota con max accurancy Tenore:')
print(get_max_note(QATenore))
print('Nota con max accurancy Basso:')
print(get_max_note(QABasso))

print('Soprano')
print(QASoprano.Q[1])
print(QASoprano.Q[2])

print('Alto')
print(QAAlto.Q[1])
print(QAAlto.Q[2])

print('Tenore')
print(QATenore.Q[1])
print(QATenore.Q[2])

print('Basso')
print(QABasso.Q[1])
print(QABasso.Q[2])

for i in range(10):
    print(get_random_note(QASoprano))
    print(get_random_note(QAAlto))
    print(get_random_note(QATenore))
    print(get_random_note(QABasso))