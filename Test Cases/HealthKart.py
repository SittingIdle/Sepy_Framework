import sys
import os
frameworkPath = os.getcwd()
print frameworkPath

sLibraryPath = frameworkPath + "\\Libraries"
print sLibraryPath
sys.path.insert(0, sLibraryPath)
import GenericLib
import time
from datetime import datetime

current_time = datetime.now().strftime('%Y%m%d%H%M%S')
##print current_time

## Browser and URL ##
sConfigFilePath = frameworkPath + "\\Config.ini"
print "SConfig File Path "
print sConfigFilePath
GenericLib.openBrowser("http://www.healthkart.com")
time.sleep(5)
##print "slept for 10 sec"

## Not a member ##
##GenericLib.actionsOnMenu("LINK=protein supplements","LINK=Whey Proteins")
GenericLib.actionsOnMenu("css=div[id='dropDownbox1']> ul > li[class='gm-mc brdr-t  gm-brdr-l-orange']>a", "css=a[class='gm-tc-nm maintainHover']")


#### Select Free registration link ##
##GenericLib.clickObject("CSS=img[alt='Sign me up for FREE membership']")
##
#### General Information ##
##GenericLib.inputText("id=loginForm.firstName", "Test")
##GenericLib.inputText("id=loginForm.lastName", "Test")
##screenName = "AT" + current_time
##emailId =  screenName + "@test.com"
##GenericLib.inputText("id=emailForm.email",emailId)
##GenericLib.inputText("id=emailForm.confirmEmail",emailId)
##password = "password1"
##GenericLib.inputText("name=passwordScreennameForm.password",password)
##GenericLib.inputText("name=passwordScreennameForm.confirmPassword",password)
##GenericLib.inputText("ID=screenName", screenName)
##GenericLib.selectDropDownByValue("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayMonth","3")
##GenericLib.selectDropDownByVisibleText("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayDay","15")
##GenericLib.selectDropDownByVisibleText("id=_TBBSIGNUP_WAR_signuprefactorportlet_birthdayYear","1985")
##
#### Shipping Address ##
##GenericLib.selectDropDownByVisibleText("id=addressCountryId","Canada")
##GenericLib.inputText("id=shippingAddressForm.street1","Test")
##GenericLib.inputText("id=shippingAddressForm.street2","Address")
##GenericLib.inputText("id=shippingAddressForm.city","Edmonton")
##GenericLib.selectDropDownByVisibleText("id=addressRegionId","Alberta")
##GenericLib.inputText("id=shippingAddressForm.postalCode","T5A0A1")
##
#### Coach Referral ##
##sCoachId = GenericLib.getValueFromINIFile('Config.ini','Environment', 'ReferralCoachID')
##GenericLib.clickObject("id=coachSelectedInput")
##GenericLib.selectDropDownByValue("id=coachLookupType","search-coach-id")
##GenericLib.inputText("id=coachSearchField",sCoachId)
##GenericLib.clickObject("id=_TBBSIGNUP_WAR_signuprefactorportlet_lookupCoachBtn")
##time.sleep(5)
##print GenericLib.verifyObjectText("CSS=span[id='_TBBSIGNUP_WAR_signuprefactorportlet_coachSelectedMessage'] > span", "Yes, I want")
##
##
#### T&C ##
##GenericLib.selectCheckbox("id=termsAndConditionsForm.termsAndConditionsAgree1")
##
#### CASL T&C ##
##GenericLib.selectCheckbox("id=termsAndConditionsForm.canadaOptIn1")
##sExpectedText = "I want to receive communication and support from my Team Beachbody Coach to learn about exciting specials and upcoming releases. There are no hidden fees or charges later on and I can choose to stop receiving communication at any time. For any questions, e-mail Privacy@Beachbody.com or write to Attn: Legal Dept., 3301 Exposition Blvd., 3rd Fl., Santa Monica, CA 90404."
##print  GenericLib.verifyObjectText("CSS=div[id='tncText']", sExpectedText)
##
#### CAPTCHA and Submit ##
##GenericLib.inputText("name=_TBBSIGNUP_WAR_signuprefactorportlet_captchaText",1111)
##GenericLib.clickObject("id=free_submit")
##
##sText = "This is Free flow where selecting the CASL T&C: - " + emailId
##time.sleep(10)
##sVerificationMsg = GenericLib.verifyObjectText("CSS=h3[class='title']", "Welcome Free Member!")
##print sVerificationMsg
##if "True" in sVerificationMsg :
##    print sText
####    fileName = screenName + ".log"
####    GenericLib.writeInNotePad(screenName,sText)
