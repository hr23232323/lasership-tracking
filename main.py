import requests as req
import json, time, os

def main():
    # Replace with your own tracking number
    trackingNum = "1LS7306076435114-1"

    # Loop runs while item is not delivered
    while True:
        # Use lasership API to get info
        res = req.post(f"http://www.lasership.com/track/{trackingNum}/json")
        resJson = json.loads(res.text)

        # Status of most recent event in API res
        curStatus = resJson["Events"][0]["EventLabel"]

        # Timestamp for tracking
        t = time.localtime()
        curTime = time.strftime("%H:%M:%S", t)

        # Print TS and status so user is aware of running program
        print(curTime + " : " + curStatus)

        # If out for delivery, sleep for 30s, otherwise break
        if(curStatus != "Out for Delivery"):
            break
        else:
            time.sleep(30)

    # sound alarm if status not out for delivery anymore!!
    while True:
        print('\007')
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')
        time.sleep(1)

if __name__ == "__main__":
    main()
