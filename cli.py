"""
Script intended for testing the simple_media_dl module
"""

from simple_media_dl import MediaDownloader


def menu() -> int:
    """
    Console Graphical Interface with return of chosen option.
    """
    print(
        f"""
    {'='*40}
            MENU
    {'='*40}
        0) - Go out.
        1) - Download Audio or Video.
    {'='*40}
    """
    )
    opc = ""
    flag = False
    while not opc.isdigit() or (int(opc) < 0 or int(opc) > 1):

        if flag:
            print("Invalid Option...")
        else:
            flag = True

        opc = input("Enter option: ")

    return int(opc)


def app() -> None:
    """
    Main App Execution.
    """
    while True:
        opc = menu()

        if opc == 0:
            exit("Done!")

        elif opc == 1:
            cont = True
            url_list = []
            while cont:
                url_list.append(input("Enter URL: "))
                cont = input("Add another URL? (y/n): ").lower() == "y"

            dwnld = MediaDownloader()
            dwnld.set_urls(url_list)
            dwnld.download_media()


if __name__ == "__main__":
    app()
