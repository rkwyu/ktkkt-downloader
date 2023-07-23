import argparse
import os
import PySimpleGUI as sg
import traceback

from ktkkt_downloader import KtkktDownloader

def run_gui():
    control_column = [
        [
            sg.Text(text='Url:', size=(10, 1), key='KEY_TEXT_URL'),
            sg.InputText(
                size=(40, 1),
                default_text='',
                key='KEY_INPUTTEXT_URL'
            ),
        ],
        [
            sg.Text(text='Directory:', size=(10, 1), key='KEY_TEXT_DIRECTORY'),
            sg.In(
                size=(40, 1),
                default_text=os.getcwd(),
                enable_events=True,
                key='KEY_IN_DIRECTORY'
            ),
            sg.FolderBrowse(),
        ],
        [
            sg.Button(
                button_text='Download Series',
                key='KEY_BUTTON_DOWNLOAD_SERIES'
            ),
            sg.Button(
                button_text='Download Episode',
                key='KEY_BUTTON_DOWNLOAD_EPISODE'
            ),
        ],
    ]
    layout = [
        [sg.Column(control_column)]
    ]
    window = sg.Window('KTKKT-DOWNLOADER', layout)
    while True:
        try:
            event, values = window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break
            elif event == 'KEY_BUTTON_DOWNLOAD_SERIES':
                if len(values['KEY_INPUTTEXT_URL']) > 0 and len(values['KEY_IN_DIRECTORY']) > 0:
                    downloader = KtkktDownloader(values['KEY_IN_DIRECTORY'])
                    downloader.download_series(values['KEY_INPUTTEXT_URL'])
                    sg.popup('Download Completed')
            elif event == 'KEY_BUTTON_DOWNLOAD_EPISODE':
                if len(values['KEY_INPUTTEXT_URL']) > 0 and len(values['KEY_IN_DIRECTORY']) > 0:
                    downloader = KtkktDownloader(values['KEY_IN_DIRECTORY'])
                    downloader.download_episode(values['KEY_INPUTTEXT_URL'])
                    sg.popup('Download Completed')
        except Exception as e:
            sg.popup(traceback.format_exc(), title='Error')


parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='all', action='store_true', help='download all episodes')
parser.add_argument('-d', type=str, dest='directory', help='directory',)
parser.add_argument('-u', type=str, dest='url', help='url')
args = parser.parse_args()

sg.theme('DarkAmber')
if __name__ == "__main__":
    if args.url is not None and args.directory is not None:
        downloader = KtkktDownloader(args.directory)
        if args.all is True:
            downloader.download_series(args.url)
        else:
            downloader.download_episode(args.url)
    else:
        run_gui()
