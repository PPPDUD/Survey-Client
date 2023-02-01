import scratchattach as scratch3
username = input("Username: ")
try:
    session = scratch3.login(username, input("Password: "))
    user = scratch3.get_user(username)
    print("Login complete.")

except:
    print("The username or password is incorrect.")
    while True:
        pass

conn = session.connect_cloud("796647920")
followers = int(scratch3.get_var("796647920", "followers"))
my_followers = user.follower_count()

if my_followers > followers:
    input("It appears that your follower count is higher than ever recorded by this program! Press ENTER to set the highscore.")
    conn.set_var("followers", str(my_followers))
    print("The highscore has been updated. Thank you for  participating!")

else:
    print("Sadly, your follower count isn't high enough to set a record. Try again when you have more followers!")


conn.disconnect()
print("\nIt is now safe to close this window.")
while True:
    pass










