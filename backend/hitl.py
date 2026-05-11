def check_escalation(answer):

    keywords = [
        "i don't know",
        "not available",
        "cannot find",
        "no information"
    ]

    for word in keywords:

        if word.lower() in answer.lower():

            return True

    return False