
questions = [
    "1.Expend energy,enjoy groups,           B conserve energy,enjoy one-on-one"
    "2.Interpret literally,                  B look for meaning and possibilities"
    "3.Logical, thinking,questioning,        B Emphaetic,feeling,accomodating"
    "4.Organised,orderly,                    B flexible,adaptable "
    "5.More outgoing,think out loud,         B more reserved,think to yourself"
    "6.Practical,realistic,experiental,      B imaginative,innovative,theoretical "
    "7.Candid,straight forward,frank,        B tactful,kind,encouraging"
    "8.Plan,schedule,                         B unplanned,spontaneous"
    "9.seek many tasks,public activities,interaction with others, B seek private,solitary activities with quite to concentrate "
    "10.Standard,usual,conventional,         B different,novel unique "
    "11.Firm,tend to criticise,hold the line, B gentle,tend to appreciate,conciliate "
    "12.Regulated,structure,                  B easy-going,live and let live"
    "13.External,communicative,express yourself B internal,reticent,keep to yourself"
     "14.Focus on here-and-now,              B look to the future,global perspective,big picture  "
     "15.Tough-minded,just                 B tender_hearted merciful "
     "16.Preparation,plan ahead,           B go with the flow,adapt as you go"
     "17. Active,initiate,                 B reflective,deliberate"
     "18.Facts,things,what is,             B ideas,dreams,what could be,philosphical"
     "19.Matter of fact,issue-oriented,     Bsenstive,people-oriented,compassionate"
      "20.Control,govern,                 B latitude,freedom"

]
options = ["A","B"]

def meyer_briggs_test():
    print("welcome to mbti personality test!")
    feed_back = []
    for question in questions:
        print(questions)
        user_input = input("enter your repesponse A/B").upper()
        if user_input  not in options:
            print("invalid entry. please enter A/B ").upper()
    feed_back.append(user_input)

    personality_test = get_personality_trait(feed_back)
    print("your personality test is " + personality_test)

def get_personality_trait(feed_back):
    trait_mapping = {
                      1: {"A": "E", "B": "I"},
                      2: {"A": "E", "B": "I"},
                      3: {"A": "S", "B": "N"},
                      4: {"A": "J", "B": "P"},
                      5: {"A": "S", "B": "N"},
                      6: {"A":""},


    }
    personality_type = " "
    for i, feed_back in enumerate(feed_back,1):
         trait = trait_mapping.get(i, None)
         if trait is not None:
             personality_type += trait[feed_back]


    trait_information = {
        "ISTJ": "Introverted Sensing Thinking Judging",
        "ISTP": "Introverted Sensing Thinking Perceiving",
        "ISFJ": "Introverted Sensing Feeling Judging",
        "ISFP": "Introverted Sensing Feeling Perceiving",
    }
    return trait_information.get(personality_type)


if __name__ == "__main__":
    meyer_briggs_test()