import requests as req
import json, time, os

def main():
    # Replace with your own tracking number
    trackingNum = "1LS7306077308792-1"

    # Loop runs while item is not delivered
    while True:
        try:
            # Use lasership API to get info
            res = req.post(f"http://www.lasership.com/track/{trackingNum}/json")
            resJson = json.loads(res.text)

            # Status of most recent event in API res
            curStatus = resJson["Events"][0]["EventLabel"]
        except:
            curStatus = "Error with API, will sleep and proceed"
        
        # Timestamp for tracking
        t = time.localtime()
        curTime = time.strftime("%H:%M:%S", t)

        # Print TS and status so user is aware of running program
        print(curTime + " : " + curStatus)

        # If out for delivery, sleep for 30s, otherwise break
        if(curStatus == "Delivered"):
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
