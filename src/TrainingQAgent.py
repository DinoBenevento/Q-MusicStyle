import numpy as np
import csv


def training(instrument, chord, iterations, QAgent):
    dicts = create_notes_dictionary()

    playable_actions = []
    playable_actions_reward = []

    rewards_new = set_rewards(instrument, chord)

    for i in range(iterations):
        current_note_p_1 = np.random.randint(-1, 20)
        current_note_p_2 = np.random.randint(1, 8)
        current_note_p_1 = dicts[0][current_note_p_1]
        if current_note_p_1 == 'Rest' or current_note_p_1 == 'Mute' or current_note_p_1 == 'Void':
            current_note = current_note_p_1
        else:
            current_note_p_2 = dicts[1][current_note_p_2]
            current_note = current_note_p_1 + str(current_note_p_2)
        try:
            for k in range(len(rewards_new[0])):
                if rewards_new[0][k] == chord and rewards_new[1][k] == current_note:
                    if float(rewards_new[2][k]) > 0:
                        if current_note not in playable_actions and float(rewards_new[2][k]) not in \
                                playable_actions_reward:
                            playable_actions.append(current_note)
                            playable_actions_reward.append(float(rewards_new[2][k]))
        except KeyError:
            continue

    if len(playable_actions) == 0:
        return QAgent
    play_note = np.random.choice(playable_actions)
    play_note_index = playable_actions.index(play_note)
    if chord in QAgent.Q[0] and play_note in QAgent.Q[1]:
        Q_index_TD = QAgent.Q[0].index(chord)
        if QAgent.Q[0].index(chord) == QAgent.Q[1].index(play_note):
            TD = QAgent.Q[2][Q_index_TD] + \
                 QAgent.gamma * playable_actions_reward[play_note_index] - QAgent.Q[2][Q_index_TD]
            QAgent.Q[2][Q_index_TD] += QAgent.alpha * TD
            return QAgent
    else:
        QAgent.Q[0].append(chord)
        QAgent.Q[1].append(play_note)
        QAgent.Q[2].append(0)
        Q_index_TD = QAgent.Q[0].index(chord)
        TD = 0 + \
             QAgent.gamma * playable_actions_reward[play_note_index] - 0
        QAgent.Q[2][Q_index_TD] += QAgent.alpha * TD
        return QAgent


def exploiting_note(chord, QAgent):
    prob_values = []
    notes_to_chord = []
    try:
        for i in range(len(QAgent.Q[0])):
            if QAgent.Q[0][i] == chord:
                notes_to_chord.append(QAgent.Q[1][i])
                prob_values.append(QAgent.Q[2][i])
        if len(prob_values) != 0:
            max_prob = max(prob_values)
            index_max_prob = prob_values.index(max_prob)
            out_note = notes_to_chord[index_max_prob]
            return out_note
        else:
            print('No Chord found')
            return 'No Note'
    except KeyError:
        print("Expoiting failed")
        return


def set_rewards(instrument, chord):
    info = csv_reader(instrument)
    rewards = [[], [], []]
    for i in range(len(info[0])):
        if info[0][i] == chord:
            rewards[0].append(chord)
            rewards[1].append(info[1][i])
            rewards[2].append(info[2][i])
    return rewards


def csv_reader(file):
    info = []

    file_notes = []
    file_chords = []
    file_prob = []

    with open("statFiles/" + file + ".txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                file_chords.append(row[0])
                file_notes.append(row[1])
                file_prob.append(row[2])
                line_count += 1
        info.append(file_chords)
        info.append(file_notes)
        info.append(file_prob)
    return info

def get_max_note(QAgent):

    maxNote = QAgent.Q[1][QAgent.Q[2].index((max(QAgent.Q[2])))]
    return maxNote



def create_notes_dictionary():
    dicts = []
    DictNotes = {1: 'C', 2: 'C#', 3: 'D-', 4: 'D', 5: 'D#', 6: 'E-', 7: 'E', 8: 'F', 9: 'F#', 10: 'G-', 11: 'G',
                 12: 'G#', 13: 'A-', 14: 'A', 15: 'A#', 16: 'B-', 17: 'B', 0: 'Rest', -1: 'Mute', 18: 'E#', 19: 'B#',
                 20: 'Void'}
    DictOctave = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
    dicts.append(DictNotes)
    dicts.append(DictOctave)
    return dicts
