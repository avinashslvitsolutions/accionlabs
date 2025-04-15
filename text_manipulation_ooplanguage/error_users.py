import re

class LogParser:
    """
    A class to parse web server logs and users who encountered ERROR status.

    """

    def __init__(self, filepath):
        """
        Initializes the LogParser with log file path.

        """
        self.filepath = filepath

    def extract_error_users(self):
        """
        Extracts unique users and their IPs from ERROR logs.

        """
        # Regular expression to match lines with "ERROR" and extract user and IP
        pattern = re.compile(r'ERROR.*User: (\w+).*IP: ([\d\.]+)')
        unique_users = set()

        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    match = pattern.search(line)
                    if match:
                        user, ip = match.groups()
                        unique_users.add((user, ip))
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return unique_users


def main():
    """
    Main function to run the log parser.
    """
    log_file = "webserver.log"  # You can change this or make it configurable
    parser = LogParser(log_file)
    errors = parser.extract_error_users()

    if errors:
        print("Unique users with ERROR status and their IPs:")
        for user, ip in errors:
            print(f"User: {user}, IP: {ip}")
    else:
        print("No ERROR entries found or log file is empty.")


if __name__ == "__main__":
    main()

