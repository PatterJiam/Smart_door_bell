from pushbullet import PushBullet
 
# Get the access token from Pushbullet.com
access_token = "o.V1cD5reRGIguzuSuJ75jVjNyDqJAdbtL"
 
# Push notification to mobile phone
def push_noti():
	pb = PushBullet(access_token)
	push = pb.push_note("Notification","Somebody's at the door \n 192.168.1.158:5000 ")

