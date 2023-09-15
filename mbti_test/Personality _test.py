def personality_test():
    extrovertCount = 0

    introvertCount = 0

    sensitiveCount = 0

    intuitiveCount = 0

    thinkerCount = 0

    feelerCount = 0

    judgingCount = 0

    perspectiveCount = 0

  questions = {
    "1) A. Expend energy, enjoy groups.       B. Conserve energy, one-on-one",
    "2) A. Interpret literally.               B. Look for meaning and possibilities",
    "3) A. Logical, thinking, questioning.    B. Empathetic, feeling, accommodating",
    "4) A. Organized, orderly.                B. Flexible, adaptable",
    "5) A. More outgoing, think out loud.     B. More reserved, think to yourself.",
    "6) A. Practical, realistic, experiential.B. Imagination, innovative, theoretical.",
    "7) A. Candid, straight forward, frank.   B. Tactful, kind, encouraging.",
    "8) A. Plan, schedule.                    B. Unplanned, spontaneous",
    "9) A. Seek many tasks, public activities, interaction with others. B. Seek private, solitary activities with quiet to concentrate.",
    "10) A. Standard, usual, conventional.     B. Different, novel, unique.",
    "11) A. Firm, tend to criticize, hold the line. B. Gentle, tend to appreciate, conciliate.",
    "12) A. Regulated, structured.             B. Easygoing, live and let live.",
    "13) A. External, communicative, express yourself. B. Internal, reticent, keep to yourself.",
    "14) A. Focus on here-and-now.             B. Look to the future, global perspective, big picture",
    "15) A. Tough minded, just.                B. Tender-hearted, merciful",
    "16) A. Preparation, plan ahead.           B. Go with the flow, adapt as you go.",
    "17) A. Active, initiate.                  B. Reflective, deliberate",
    "18) A. Facts, things, what is.            B. Ideas, dreams, 'what could be', philosophical",
    "19) A. Matter of fact, issue oriented.    B. Sensitive, people-oriented, compassionate",
    "20) A. Control, govern.                   B. Latitude, freedom"

  }



personalityType = ""
personalityType += extrovertOrIntrovert(userResponses[0], userResponses[1]);
personalityType += sensitiveOrIntuitive(userResponses[2], userResponses[3]);
personalityType += thinkerOrFeeler(userResponses[4], userResponses[5]);
personalityType += judgingOrPerspective(userResponses[6], userResponses[7]);

return personalityType



extrovertOrIntrovert

