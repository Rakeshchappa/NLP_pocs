import random
import streamlit as st


def Guess_Num():
    st.title('Number Guessing Game')
    sys_generate_Num = random.randint(1, 20)
    print('System generated number is :' + str(sys_generate_Num))
    st.write('System generated number is:', sys_generate_Num)
    number_of_Guess = 0
    Score = 20

    while number_of_Guess < 5:
        # Player_Input = int(input('Hello please guess the number below 20  :'))
        player_input = st.number_input('Hello, please guess the number below 20:', min_value=0, max_value=20, step=1)

        # Display the user input
        st.write('You guessed:', player_input)
        number_of_Guess += 1
        if sys_generate_Num == player_input:
            # print('You won the game Random Number is :' + str(sys_generate_Num))
            # print('your score is :' + str(Score))
            st.success(f'You won the game! Random Number is: {sys_generate_Num}')
            st.write(f'Your score is: {Score}')
            # User_input = str(input('Please Type yes Do you want to play again '))
            user_input = st.text_input('Do you want to play again? Type "yes" or "no".')
            if user_input.lower() == 'yes':
                Guess_Num()
            else:
                print('Thanks For Playing')
                return
        elif sys_generate_Num < player_input:
            Score -= 1
            # print('Your number too high and your Score is:' + str(Score))
            st.write(f'Your score is: {Score}')
        elif sys_generate_Num > player_input:
            Score -= 1
            # print('your number is too low and your Score is:' + str(Score))
            st.write(f'Your score is: {Score}')
        else:
            # print('no more choices')
            st.write(f'no more choices')
            break
    # User_Play_Again = str(input('Choices are over Do you want to try again? Please type Yes '))
    User_Play_Again = st.text_input('Choices are over Do you want to try again? Please type Yes')
    if User_Play_Again.lower() == 'yes':
        Guess_Num()
    else:
        print('thanks for playing')


Guess_Num()
