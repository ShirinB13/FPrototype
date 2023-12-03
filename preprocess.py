import re

def clean_data(data_file_name):
    with open(data_file_name, "r", encoding="utf8") as data_file:
        # read all lines from the file and skip the first two lines
        data_lines = data_file.readlines()[2:]

    # join the lines into a single string
    data = "".join(data_lines)

    # remove unnecessary patterns
    cleaned_data = re.sub(r"(\[\d+\/\d+\/\d+,\s\d+:\d+:\d+\]\s\w+\:\s)|(<This message was edited>)|(<Media omitted>)|(You deleted this message.)|(‎)", "", data)

    # split the cleaned data into lines
    cleaned_data_lines = list(cleaned_data.split("\n"))
    cleaned_data_lines = list(filter(None, cleaned_data_lines))

    return cleaned_data_lines


