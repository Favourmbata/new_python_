def welcome_page():
    response = len(input("welcome  to  nokia press 1 for main menu or press any_other value to quit"))
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
    else:
        print("invalid_option")
        main_menu()


def phone_book_Options():
    response = int(input("""
     1.=>Type of view
       2.=>Memory status
     **** 700 for mainMenu
    """))
    if response == 1:
        phone_book_Options()
    if response == 2:
        phone_book_Options()
    if response == 700:


        main_menu()


def phone_book_option_type_of_view():
    response = int(input("""
       1.=> type of view
        press 700 for menu
      """))
    if response == 00:
        phone_book_Options()
    if response == 700:
        main_menu()


def phone_book_option_memory_status():
    response = int(input("""
     1.=> memory status
      press 700 for main menu
     """))
    if response == 00:
        phone_book_Options()
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
    response = (input("""
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
    4. => Edith
    5. => Erase
    6. => Assign tone
    7. => Send b card
    8. => Options
    9. => Speed dials
    10. => Voice tags
    press 00 phone book
    press 700 to go to main menu
         """))

    if response == 1:
        search()
    if response == 2:
        service_Nos()
    if response == 3:
        add_name()
    if response == 4:
        edith()
    if response == 5:
        erase()
    if response == 6:
        assign_tone()
    if response == 7:
        send_b_card()
    if response == 8:
        phone_book_Options()
    if response == 9:
        main_menu()
    if response == 10:
        main_menu()
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def search():
    response = int(input("""
        1.=> search
        press 700 to go main menu
        """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def service_Nos():
    response = (input("""
      1.=> service Nos
      press 700 to go main menu
      """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def add_name():
    response = (input("""
      1.=> Add name
       press 700 to go main menu
      """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def send_b_card():
    response = int(input("""
     1.=> send b card
     press 700 to for main menu
        """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def erase():
    response = int(input("""
     1.=> Erase
     press 700 to go main menu
    """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def assign_tone():
    response = int(input("""
    1.=> Add tone
    press 700 to main menu
    """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def speed_dials():
    response = int(input("""
     1.=> spee dials
     press 700 to go main menu
    """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def send_b_card():
    response = int(input("""
     1.=> send b' card
      press 700 for main menu
      """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def Voice_tags():
    response = int(input("""
     1.Voice tags
     press 700 to go main menu
    """))
    if response == 00:
        phone_book()
    if response == 700:
        main_menu()


def edith():
    response = int(input("""
     1.=> Edith
     press 700 to main menu
    """))
    if response == 00:
        phone_book()
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
    if response == 1:
        message_write_messages()
    if response == 2:
        message_inbox()
    if response == 3:
        message_outbox()
    if response == 4:
        message_picture_messages()
    if response == 5:
        message_templates()
    if response == 6:
        message_smiley()
    if response == 7:
        message_message_setting_set()
    if response == 8:
        message_info_service()
    if response == 9:
        message_voice_mailbox_number()
    if response == 10:
        message_service_command_editor()
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_write_messages():
    response = int(input("""
     1.=> write message
      press 700 to main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_inbox():
    response = int(input("""
    1.=> inbox
     press 700 to go main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_outbox():
    response = int(input("""
     1.=> Outbox
     press 700 to main menu
   """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_service_command_editor():
    response = int(input("""
     1.=> Service command editor
     press 700 to main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_picture_messages():
    response = int(input("""
        1.=> picture messages
        press 700 for main menu
        """))


def message_templates():
    response = int(input("""
     1.=> Templates
     press 700 for main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_smiley():
    response = int(input("""
        1.=> Smiley
        press 700 for main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_info_service():
    response = int(input("""
    1.=> Info Service
     press 700 for main menu
    """))
    if response == 00:
        messages()
    if response == 700:
        main_menu()


def message_voice_mailbox_number():
    response = int(input("""
        1.=> Voice Mail Box Number
         press 700 for main menu
        """))
    if response == 00:
        messages()
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
    if response == 1:
        call_register_missed_calls()
    if response == 2:
        call_register_received_call()
    if response == 3:
        call_register_dialled_numbers()
    if response == 4:
        call_register_erase_recent_call_lists()
    if response == 5:
        call_register_show_call_duration()
    if response == 6:
        call_register_show_call_duration()
    if response == 7:
        Call_register_prepid_credit()
    if response == 8:
        Call_register_prepid_credit()
    if response == 00:
        call_register()
    if response == 700:
        main_menu()


def call_register_missed_calls():
    response = int(input("""
    1.=> Missed calls
    press 700 for main menu
    """))
    if response == 00:
        call_register()
    if response == 700:
        main_menu()


def call_register_received_call():
    response = int(input("""
     1.=> Receved calls
     press 700 for main menu
    """))
    if response == 00:
        call_register()
    if response == 700:
        main_menu()


def call_register_dialled_numbers():
    response = int(input("""
        1.=> Dialled Numbers
        press 700 for main menu
       """))
    if response == 00:
        call_register()
    if response == 700:
        call_register()


def call_register_erase_recent_call_lists():
    response = int(input("""
     1.=> _Erase_recent_call_lists
      press 700 for main menu
     """))
    if response == 00:
        call_register()
    if response == 700:
        call_register()


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


def Call_register_prepid_credit():
    response = int(input("""
  1.=> prepaid credit
  press 700 for main menu
   """))
    if response == 00:
        call_register()
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
    if response == 1:
        tones_ringing_tone()
    if response == 2:
        tones_ringing_volume()
    if response == 3:
        tones_incoming_call_alert()
    if response == 4:
        tones_composer()
    if response == 5:
        tones_message_alert_tone()
    if response == 6:
        tones_keypad_tones()
    if response == 7:
        tones_warning_and_game_tones()
    if response == 8:
        tone_vibrating_alert()
    if response == 9:
        tone_screen_saver()
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_ringing_tone():
    response = int(input("""
    1.=> ringing tone
    press 700 for main menu
    """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_ringing_volume():
    response = int(input(""""
    1.=> ringing volume
    press 700 for main menu
    """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_incoming_call_alert():
    response = int(input("""
     1.=> incoming call alert
      press 700 for main menu
      """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_composer():
    response = int(input("""
     1.=> composer
     press 700 for main menu
     """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_message_alert_tone():
    response = int(input("""
    1.=> message alert tone
        press 700 for main menu
    """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_keypad_tones():
    response = int(input("""
         1.=> keypad tones
        press 700 for main menu
          """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tones_warning_and_game_tones():
    response = int(input("""
      1.=> warning and game tones
      press 700 for main menu
    """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tone_vibrating_alert():
    response = int(input("""
        1.=> vibrating alert
         press 700 for main menu
       """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def tone_screen_saver():
    response = int(input("""
        1.=> screen saver
        press 700 for main menu
         """))
    if response == 00:
        tones()
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
    if response == 4:
        setting_restore_factory_setting()
    if response == 00:
        settings()
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
    if response == 1:
        call_settings_automatic_redial()
    if response == 2:
        call_setting_speed_dials()
    if response == 3:
        call_setting_Call_waiting_option()
    if response == 4:
        call_setting_own_numbers_sending()
    if response == 5:
        call_setting_phone_line_in_use()
    if response == 6:
        call_setting_automatic_answer()
    if response == 00:
        setting_call_setting()
    if response == 700:
        main_menu()


def call_settings_automatic_redial():
    response = int(input("""
        1.=> automatic redial
        press 700 for main menu
        """))
    if response == 00:
        setting_call_setting()
    if response == 700:
        main_menu()


def call_setting_speed_dials():
    response = int(input("""
     1.=> speed dials
     press 700 for main menu
       """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def call_setting_Call_waiting_option():
    response = int(input("""
       1.=> Call_waiting_option
         press 700 for main menu
         """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def call_setting_own_numbers_sending():
    response = int(input("""
     1.=> own number sending
      presss 700 for main menu
        """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def call_setting_phone_line_in_use():
    response = int(input("""
      1.=> phone line in use
        press 700 for main menu
       """))
    if response == 00:
        tones()
    if response == 700:
        main_menu()


def call_setting_automatic_answer():
    response = int(input("""
     1.=> automatic answer
      press 700 for main menu
       """))
    if response == 00:
        tones()
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
    if response == 1:
        setting_pone_setting_language()
    if response == 2:
        setting_phone_setting_call_info_display()
    if response == 3:
        setting_phone_setting_welcome_note()
    if response == 4:
        setting_phone_setting_network_selection()
    if response == 5:
        setting_phone_setting_light()
    if response == 6:
        setting_phone_setting_Confirm_sim_service_action()
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_pone_setting_language():
    response = int(input("""
     1.=> language
      press 700 for main menu
      """))
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_phone_setting_call_info_display():
    response = int(input("""
      1.=> call info display
       press 700 for main menu
        """))
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_phone_setting_welcome_note():
    response = int(input("""
        1.=> welcome note
        press 700 for main menu
        """))
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_phone_setting_network_selection():
    response = int(input("""
        1.=> network selection
        press 700 for main menu
          """))
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_phone_setting_light():
    response = int(input("""
       1.=> light
        press 700 for main menu
         """))
    if response == 00:
        setting_phone_setting()
    if response == 700:
        main_menu()


def setting_phone_setting_Confirm_sim_service_action():
    response = int(input("""
       1.=> Confirm sim service action
          press 700 for main menu
            """))
    if response == 00:
        setting_phone_setting()
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
    if response == 1:
        setting_security_setting_pin_code_request()
    if response == 2:
        setting_security_setting_call_barring_service()
    if response == 3:
        setting_security_setting_fixed_dialling()

    if response == 4:
        setting_security_setting_closed_user_group()
    if response == 5:
        setting_security_setting_phone_security()
    if response == 6:
        setting_security_setting_change_access_codes()
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_pin_code_request():
    response = int(input("""
      1.=> PIN code request
       press 700 for mai menu
        """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_call_barring_service():
    response = int(input("""
      1.=> Call barring service
       press 700 for main service
        """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_fixed_dialling():
    response = int(input("""
       1.=> Fixed dialling
        press 700 for main menu
         """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_closed_user_group():
    response = int(input("""
       1.=> Closed user group
         press 700 for main menu
      """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_phone_security():
    response = int(input("""
       1.=> Phone security
        press 700 for main menu
         """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_security_setting_change_access_codes():
    response = int(input("""
      1.=> Change access codes
       press700 for main menu
        """))
    if response == 00:
        setting_security_setting()
    if response == 700:
        main_menu()


def setting_restore_factory_setting():
    response = int(input("""
       1.=> Restore factory settings
        press 700 for main menu
          """))
    if response == 00:
        settings()
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
     1. Alarm clock
     2. Clock settings
     3. Date setting
     4. Stopwatch
     5. Countdown timer
     6. Auto update of date and time
     press 700 for main menu
       """))
    if response == 1:
        alarm_clock()
    if response == 2:
        clock_settings()
    if response == 3:
        date_setting()
    if response == 4:
        stopwatch()
    if response == 5:
        countdown_timer()
    if response == 6:
        auto_update_of_date_time()


def alarm_clock():
    response = int(input("""
      1.=> alarm clock
       press 700 for main menu
      """))
    if response == 00:
        clock()
    if response == 700:
        main_menu()


def clock_settings():
    response = int(input("""
      1.=> clock setting
        press 700 for main menu 
         """))
    if response == 00:
        clock()
    if response == 700:
        main_menu()


def date_setting():
    response = int(input("""
      1.=> date setting
      press 700 for min menu
        """))
    if response == 00:
        clock()
    if response == 700:
        main_menu()


def stopwatch():
    response = int(input("""
        1.=> stopwatch
         press 700 for main menu
         """))
    if response == 00:
        clock()
    if response == 700:
        main_menu()


def countdown_timer():
    response = int(input("""
       1.=> countdown timer
       press 700 for main menu
       """))
    if response == 00:
        clock()
    if response == 700:
        main_menu()


def auto_update_of_date_time():
    response = int(input("""
     1.=> Auto update of date and time
      press 700 for main menu
       """))
    if response == 00:
        clock()
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
