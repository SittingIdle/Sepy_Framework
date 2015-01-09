import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
##print current_time

## Browser and URL ##
sURL = GenericLib.getValueFromINIFile('Config.ini','Environment', 'tbburl')
GenericLib.openBrowser(sURL)
time.sleep(10)
##print "slept for 10 sec"

## Not a member ##
GenericLib.clickObject("CSS=li[class='not-a-member'] > a")

## Select Club registration link ##
GenericLib.clickObject("CSS=img[alt='YES! Sign me up for Club membership']")

## General Information ##
GenericLib.inputText("id=loginForm.firstName", "Test")
GenericLib.inputText("id=loginForm.lastName", "Test")
screenName = "AT" + current_time
emailId =  screenName + "@test.com"
GenericLib.inputText("id=emailForm.email",emailId)
GenericLib.inputText("id=emailForm.confirmEmail",emailId)
password = "password1"
GenericLib.inputText("name=passwordScreennameForm.password",password)
GenericLib.inputText("name=passwordScreennameForm.confirmPassword",password)
GenericLib.inputText("ID=screenName", screenName)
GenericLib.selectDropDownByValue("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayMonth","3")
GenericLib.selectDropDownByVisibleText("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayDay","15")
GenericLib.selectDropDownByVisibleText("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayYear","1985")

## Shipping Address ##
GenericLib.selectDropDownByVisibleText("id=addressCountryId","Canada")
GenericLib.inputText("id=shippingAddressForm.street1","Test")
GenericLib.inputText("id=shippingAddressForm.street2","Address")
GenericLib.inputText("id=shippingAddressForm.city","Edmonton")
GenericLib.selectDropDownByVisibleText("id=addressRegionId","Alberta")
GenericLib.inputText("id=shippingAddressForm.postalCode","T5A0A1")

## Billing Information ##
GenericLib.inputText("name=billingInfo.cardHolderFirstName","Test")
GenericLib.inputText("name=billingInfo.cardHolderLastName","Billing")
GenericLib.selectDropDownByValue("id=billingInfo.ccType","visa")
GenericLib.inputText("name=billingInfo.ccNumber","1234123412341234")
GenericLib.selectDropDownByVisibleText("id=billingInfo.expMonth","May")
GenericLib.selectDropDownByVisibleText("id=billingInfo.expYear","2020")
GenericLib.inputText("name=billingInfo.cvv","159")

    ## Billing Address ##
GenericLib.selectCheckbox("id=billingSameAsShipping")
##GenericLib.inputText("id=billingAddressForm.street1","Test")
##GenericLib.inputText("id=billingAddressForm.street2","Address")
##GenericLib.inputText("id=billingAddressForm.city","Edmonton")
##GenericLib.selectDropDownByVisibleText("id=addressRegionIdBilling","Alberta")
##GenericLib.inputText("id=billingAddressForm.postalCode","T5A0A1")

## Coach Referral ##
GenericLib.clickObject("id=defaultCoach")

## CASL T&C ##
GenericLib.selectCheckbox("id=termsAndConditionsForm.canadaOptIn1")
sExpectedText = "I want to receive communication and support from my Team Beachbody Coach to learn about exciting specials and upcoming releases. There are no hidden fees or charges later on and I can choose to stop receiving communication at any time. For any questions, e-mail Privacy@Beachbody.com or write to Attn: Legal Dept., 3301 Exposition Blvd., 3rd Fl., Santa Monica, CA 90404."
print  GenericLib.verifyObjectText("CSS=div[id='tncText']", sExpectedText)

## T&C ##
GenericLib.selectCheckbox("id=termsAndConditionsForm.termsAndConditionsAgree1")
GenericLib.inputText("name=_TBBSIGNUP_WAR_signuprefactorportlet_captchaText",1111)
GenericLib.clickObject("id=club_submit")


## Verification ##
sText = "This is Club flow without selecting Coach but selecting the CASL T&C: - " + emailId
sVerificationMsg = GenericLib.verifyObjectText("CSS=h3[class='title']", "Welcome Club Member!")
print sVerificationMsg
if "True" in sVerificationMsg :
    print sText
    sFileName = screenName + ".log"
    GenericLib.writeInNotePad(sFileName,sText)
