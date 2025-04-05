def get_source():
    """"
    Get the source of the export, will repeat until valid input is found.
    """
    source = input("Enter Source: \n 1)Spotify \n 2)YouTube Music \n 3)File\n")
    match str.lower(source):
        case "spotify" | "1":
            return 1
        case "youtube music" | "2":
            return 2
        case "file" | "3":
            return 3
        case _:
            print("Invalid Input for source, please try again.")
            return get_source()
        
def get_output():
    """
    Get the output of the export, will repeat until valid input is found.
    """
    output = input("Enter Output: \n 1)Spotify \n 2)YouTube Music \n 3)File\n")
    match str.lower(output):
        case "spotify" | "1":
            return 1
        case "youtube music" | "2":
            return 2
        case "file" | "3":
            return 3
        case _:
            print("Invalid Input for source, please try again.")
            return get_output()

def main():
    source = get_source()
    output = get_output()
    if (source == output):
        print("Source and output are the same, please try again.")
        main()
    else:
        print("Starting export, please wait!")
        match [source, output]:
            case [1, 2]:
                pass
            case [1, 3]:
                pass
            case [2, 1]:
                pass
            case [2, 3]:
                pass
            case [3, 1]:
                pass
            case [3, 2]:
                pass

try:
    print("Press Ctrl+C at any time to stop program")
    main()
except KeyboardInterrupt:
    print("\nExciting the program.")

