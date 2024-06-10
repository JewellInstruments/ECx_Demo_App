import serial
import time
import datetime


def main():

    # ask the user for the com port information
    com_port = input("Enter COM port [COM<x>]: ")  # "COM5"
    baud_rate = input("Enter baud rate [19200]: ")  # 19200

    # create the serial device per section 4 of the manual.
    device = serial.Serial(com_port, baud_rate, 8, "N", 1, timeout=1)

    # get the list of commands sent and received by the sensor.
    device.write("@X?*67\r\n".encode())
    time.sleep(0.01)
    data = device.readline().decode("utf-8")
    print(data)

    print("Testing streaming capabilities...")
    print("Press ctrl+c to stop streaming.")
    while True:
        try:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            device.write("$PTNT,HTM*63\r\n".encode())
            time.sleep(0.01)
            # get the data at the serial port
            data = device.readline().decode("utf-8").rstrip().split(",")
            # unpack the data per section 4.1.4.4
            heading = float(data[1])
            pitch = float(data[3])
            roll = float(data[5])
            dip = float(data[7])
            b_field = float(data[8][:-3])

            # show the data to the user
            print_string = f"{current_datetime}: Heading = {heading: 0.1f}, pitch = {pitch: 0.1f}, roll = {roll: 0.1f}, dip = {dip: 0.1f}, relative field = {b_field: .0f}"
            print(print_string)
        except KeyboardInterrupt:
            # allow for easy exiting
            break
        except Exception as e:
            # show any errors that pop up (like no data at serial port...)
            print(e)
    device.close()

    return


if __name__ == "__main__":
    main()
