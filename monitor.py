"""
Internet speed using:
    https://medium.com/analytics-vidhya/record-your-internet-speeds-using-python-6a9827f8eec
    https://github.com/sivel/speedtest-cli
"""

import speedtest as st

from csv import writer
from time import sleep
from datetime import datetime


def get_new_speeds():
    """Get new speed values"""
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    ping = speed_test.results.ping
    download = speed_test.download()
    upload = speed_test.upload()

    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)

    return [ping, download_mbs, upload_mbs]


def main():
    """Main function"""
    file_name = f'speed_test_{datetime.now().strftime("%d%m%y_%H_%M")}.csv'
    with open(file_name, 'w', newline='') as file:
        csv_writer = writer(file, dialect='excel-tab')

        header1 = [f'Internet Speed test {datetime.now().strftime("%d.%B.%Y")}']
        header2 = ['Time', 'Ping[ms]', 'Download[Mb/s]', 'Upload[Mb/s]']

        csv_writer.writerow(header1)
        csv_writer.writerow([])
        csv_writer.writerow(header2) 

    counter = 1
    for i in range(0,5000):
        new_speeds = get_new_speeds()
        result = [datetime.now().strftime("%H:%M")] + new_speeds

        with open(file_name, 'a', newline='') as file:
            csv_writer = writer(file, dialect='excel-tab')
            csv_writer.writerow(result)

        print(f'Test: {counter}\n' \
            f'Date: {result[0]}\n' \
            f'Ping: {result[1]}[ms]\n' \
            f'Download: {result[2]}[Mb/s]\n' \
            f'Upload: {result[3]}[Mb/s]\n' \
            '-------------------------\n' \
            '-------------------------'
        )
        counter += 1
        sleep(180)


if __name__ == "__main__":
    main()