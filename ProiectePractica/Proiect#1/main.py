from app.App import App

def main():
    application = App("Word Guesser")
    application.gui_loop()
    return 0

if __name__ == '__main__':
    main()