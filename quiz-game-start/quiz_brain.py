class QuizBrain:
    # TODO:
    #   A)Ask the questions
    #   B)Check the correct answer
    #   C)Check if the quiz has ended
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        list_size = len(self.question_list)
        if list_size < self.question_number + 1:
            return False
        else:
            return True

    def next_question(self):
        from random import randint
        from time import sleep
        from data import quiz_game_art
        LIST_INDEX = 0
        P_STARTING_POINTS = 0
        SIXTY_PCENT = 0.6
        answer_list = []
        correct_answer_list = []
        print('Welcome to the', end='')
        for x in range(0, 3):
            print('.', end='')
            sleep(.4)
        print(quiz_game_art, '\n\n')
        sleep(1)
        input('Press enter to start the quiz!')
        print('Type quit to get out before the game finishes(but you will have a penalty of 3 points)')
        while self.still_has_questions():
            current_question = self.question_list[randint(0, 49)]
            correct_answer_list.append(current_question.answer)
            current_question_number = self.question_number + 1
            answer = input(f"{current_question_number}) {current_question.text}(True/False)?").capitalize()
            while answer not in ['F', 'T', 'False', 'True', 'Quit']:
                print('Please choose (True/False)')
                answer = input(f"{current_question_number}) {current_question.text}(True/False)?").capitalize()
            if answer in ['F', 'T']:
                if answer == 'F':
                    answer = 'False'
                elif answer == 'T':
                    answer = 'True'
            for x in range(0,3):
                print('.')
                sleep(.2)
            if answer == current_question.answer:
                P_STARTING_POINTS += 1
                print(f'You got it right!\n You have {P_STARTING_POINTS} out of {current_question_number}')
            elif answer == 'Quit':
                P_STARTING_POINTS -= 3
                break
            else:
                print(f'Bummer! That is wrong! Good luck next time \n You have {P_STARTING_POINTS} out of '
                  f'{current_question_number}')
            self.question_number += 1
        player_points = P_STARTING_POINTS
        # looping through the correct answers up to where it was answered, while comparing to see if the user_answer
        # was correct
        print(f'Your score was {player_points}!')
        if player_points > self.question_number * SIXTY_PCENT:
            print('Wow you are very good!')
        else:
            print('Gotta study more...')
