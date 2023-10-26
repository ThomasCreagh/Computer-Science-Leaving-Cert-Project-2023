import urllib.request as ur
import urllib.error as ue
import subprocess

import csv


# https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/
def connected_to_internet(_url: str = "http://google.com") -> None:
    """Check if it connected to the internet by pinging google.com

    Args:
        _url (str): the url of the address to ping.
            Defaults to "http://google.com".

    Returns:
        bool: True if connected to the internet, otherwise False
    """
    try:
        ur.urlopen(_url)
        return True
    except ue.URLError:
        return False


def library_install_online(file_path: str = "installed.txt") -> None:
    """Install requirements if necessary
    """

    with open(file_path, "r") as read_file:
        csv_data = csv.reader(read_file)
        data = list(csv_data)
        if data[0][0] == "False":
            bat_cmd = "pip install -r requirements.txt"
            result = subprocess.check_output(bat_cmd, shell=True)
            result = str(result).split("Requirement ")
            for i in result[1:]:
                text = i.split("c:")
                print("Requirement", text[0][:-4])
            print("May have installed dependencies that are not installed.")
            print()
            with open(file_path, "w") as write_file:
                data_writer = csv.writer(write_file)
                data_writer.writerow(["True"])


if __name__ == "__main__":
    if connected_to_internet():
        library_install_online()
    import start
    run = start.Start()
