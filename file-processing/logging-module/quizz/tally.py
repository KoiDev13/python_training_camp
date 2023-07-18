import logging

def tally_votes(data):
    """ 
    the example voting data and operations are in the __main__ section
    write code that will ask for user input for item number being voted on
    create a log file named <voting item>.log 
    tally votes and log each vote
    using: tally = f"Item: {voting_item} Yes: {yes} No: {no}"
    return tally
    """

    voting_item = input("What is the item number for this vote? ").strip()
    file_name = f"{voting_item}.log"

    logging.basicConfig(
        filename=file_name,
        format='%(asctime)s-[%(levelname)s]:%(message)s', level=logging.INFO)

    yes = 0
    no = 0
    for vote in data:
        if vote == 'y':
            yes += 1
        else:
            no += 1
        # log vote
        logging.info(vote)

    tally = f"Item: {voting_item} Yes: {yes} No: {no}"

    logging.info(tally)

    return tally

if __name__ == "__main__":
    voting_data = ["y", "n", "y", "y", "y", "n"]
    tally = tally_votes(voting_data)
    print(tally)
    