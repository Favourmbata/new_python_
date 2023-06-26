def welcome_page():
    response = input("welcome  to  nokia press 1 for main menu or press any_other value to quit")
    if response != 1:
        print("thanks for using our service")
    main_menu()


def main_menu():
    response = int(input("""
    1. => Phone book
    2. => Messages
    3. => Chat
    4. => Call register
    5. => Tones
    6. => Setting
    7. => Call divert
    8. => Games
    9. => Calculator
    10. => Reminders
    11. => Clock 
    12. => Profiles
    13. => Sim services
    press 700 to Exit
     """))
    if response == 1:
        phone_book()
    if response == 2:
        messages()
    if response == 3:
        chat()
    if response == 4:
        call_register()
    if response == 5:
        tones()
    if response == 6:
        settings()
    if response == 7:
        call_divert()
    if response == 8:
        games()
    if response == 9:
        calculator()
    if response == 10:
        reminders()
    if response == 11:
        clock()
    if response == 12:
        profile()
    if response == 13:
        sim_services()


def phone_book_Options():
    response = int(input("""
     1.=>Type of view
       2.=>Memory status
     **** 700 for mainMenu
    """))
    if response == 700:
        main_menu()


def message_message_setting_set():
    response = int(input("""
    1. => Set 1
   press 700 to go main menu
    """))
    if response == 1:
        message_message_settings_set1()
    if response == 2:
        message_message_setting_common()
    if response == 700:
        main_menu()


def message_message_setting_common():
    response = int(input("""
    1. => delivery reports
    2. => reply via same centre
    3. => character support
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def message_message_settings_set1():
    response = int(input("""
    1. => message centre number
    2. => message sent as
    3. => message validity
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def call_register_show_call_duration():
    response = int(input("""
    1. => Last call duration
    2. => All call's duration
    3. => Received call's duration
    4. => Dialled call's duration
    5. => clear timers
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def message_message_setting_common():
    response = int(input("""
    1. => Delivery reports
    2. => Reply via same center
    3. => Character support
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def phone_book():
    response = int(input(""""
    1. => Search
    2. => Service Nos.
    3. => Add name
    4. => Erase
    5. => Edith
    6. => Assign tone
    7. => Send b'card
    8. => Options
    9. => Speed dials
    10. => Voice tags
        press 700 to go to main menu
         """))
    if response == 8:
        phone_book_Options()
    if response == 700:
        main_menu()

def messages():
        response = int(input("""
        1. =>Write messages
        2. =>Inbox
        3. => OutBox
        4. => Picture messages
        5. => Templates
        6. => Smiley
        7. => Message settings
       8. => Info service
       9. => Voice mailbox number
       10. => Service command Editor
        press 700 to go to main menu
        """))
        if response == 7:
            message_message_setting_set()
        if response == 700:
            main_menu()


def chat():
    response = int(input("""
   """))
    if response == 700:
        main_menu()


def call_register():
    response = int(input("""
    1. => missed calls
    2.  => received calls
    3. => Dialled numbers
    4. => Erase recent call lists
    5. => Show call duration
    6. => show call cost
    7.=> call cost settings
    8.=> prepaid credit
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def call_register_show_call_cost():
    response = int(input("""
    1.=> Last call cost
    2. => All calls cost
    3. => clear counter
    press 700 to go to main menu
    """))
    if response == 6:
        call_register_show_call_cost()
    if response == 700:
        main_menu()


def call_register_show_call_duration():
    response = int(input("""
    1. => last call duration
    2.=> All call's duration
    3. => Received calls duration
    4. => Dialled calls duration
    5.=> Clear times
        press 700 to go main menu
    """))
    if response == 5:
        call_register_show_call_duration()
    if response == 700:
        main_menu()


def call_register_call_cost_setting():
    response = int(input("""
   1.=> Call cost limit
   2. => show costs in
    press 700 to go main menu
   """))
    if response == 7:
        call_register_call_cost_setting()
    if response == 700:
        main_menu()


def tones():
    response = int(input("""
    1. => Ringing tone
    2. => Ringing volume
    3. => Incoming call
    4. => Composer
    5. => Messages alert tone
    6. => Keypad tones
    7. => warning and game tones
    8. => Vibrating alert
    9. => Screen saver
    press 700 to go main menu
    """))
    if response == 700:
        main_menu()


def settings():
    response = int(input("""
    1. => Call settings
    2. => Phone settings
    3. => Security settings
    4. => Restore settings
    press 700 to go to main menu
    """))
    if response == 1:
        setting_call_setting()
    if response == 2:
        setting_phone_setting()
    if response == 3:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_call_setting():
    response = int(input("""
    1. => Automatic redial
    2. => Speed dialing
    3. => Call waiting option
    4. => Own numbers sending
    5. => Phone line in use
    6. => Automatic answer
        press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def setting_phone_setting():
    response = int(input("""
    1. => Language
    2. => Cell info display
    3. => Welcome note
    4. => Network selection
    5. => lights
    6. => Confirm sim service action
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def setting_security_setting():
    response = int(input("""
      1. => Pin code request
      2. => Call barring service
      3. => Fixed dialling
      4. => Closed user group
      5. => Phone security
      6. => Change access codes
        press 700 to go to main menu
      """))
    if response == 700:
        main_menu()


def call_divert():
    response = int(input("""
    1. => Call divert
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def games():
    response = int(input("""
    1. => games
        press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def calculator():
    response = int(input("""
    1. => Calculator
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def reminders():
    response = int(input("""
 1. => Reminders
   press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def clock():
    response = int(input("""
1.  =>  clock
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()

    def clock_alarm_clock():
        response = int(input("""
    1.=> Alarm clock
    2. => Clock settings
    3. => Date setting
    4. => Stopwatch
    5. => Countdown timer
    6. => Auto update of date and time
    press
    press 700 to go to main menu 
       
    """))
        if response == 700:
            main_menu()


def profile():
    response = int(input("""
    1. => Profile
    press 700 to go to main menu
    """))
    if response == 700:
        main_menu()


def sim_services():
    response = int(input("""
    1. => Sim services
    press 700 to go to main menu
 """))


if __name__ == '__main__':
    welcome_page()
