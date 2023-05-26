import gecko_class


#Provde your coingecko email and password
# You can provide more than one coingecko account in the user_credentiial
# Always make sure the email and the paswword exist
user_credential =  {'YOUR_COINGECKO EMAIL':'YOUR_COINGECKO_PASSWORD'}


for email, password in user_credential.items():
    print("signing in user credentials")

   #signing in with password and email
    signin = gecko_class.sign_in()
    signin.login(email, password)
    

    #clickimg the candy to collect the candy
    collect_candy = gecko_class.candy()
    collect_candy.candy_click()

    #sigining ou the user 
    print("Signing out")
    signout = gecko_class.signout()
    signout.logout(email)






