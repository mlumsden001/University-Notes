#!/bin/bash
#
# This script will do a bit of housekeeping before removing the computers framework and MDM profiles.
# This script has been modified by Paul Bahry for the 2018 students.

# Remove CasperCheck
launchctl unload /Library/LaunchDaemons/com.company.caspercheck.plist
rm -rf /Library/Scripts/caspercheck.sh 
rm -rf /Library/LaunchDaemons/com.company.caspercheck.plist
rm -rf /var/log/caspercheck.log

# Remove applications and school owned software & Settings
defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText ""
chflags -R nouappnd /Applications/Server\ Access
rm -rf /Applications/Server\ Access
rm -rf /Library/Caches/com.apple.desktop.admin.png
rm -rf /Applications/Autodesk*
rm -rf /Applications/Click*
rm -rf /Applications/FX*
rm -rf /Applications/Gapminder*
rm -rf /Applications/GeoGebra*
rm -rf /Applications/LockDown*
rm -rf /Applications/Macbeth*
rm -rf /Applications/VMware*
rm -rf /Applications/Sibelius*
rm -rf /Library/Application\ Support/regid*
rm -rf /Library/Application\ Support/plasq
rm -rf /Applications/NAP\ Locked\ down\ browser.app
rm -rf /Library/Desktop\ Pictures/Riverview\ Background.png

# Remove Nomad
launchctl unload -w /Library/LaunchAgents/com.trusourcelabs.NoMAD.plist
rm -rf /Applications/Nomad.app

# Remove McAfee
sh /Library/McAfee/agent/scripts/uninstall.sh
rm -rf /Applications/McAfee*

#Disable ARD and Remote Login
/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -deactivate -configure -access -off
systemsetup -f -setremotelogin off

# Remove admin account
/usr/bin/dscl . -delete /Users/admin
rm -rf /private/var/admin &
wait %1

# Un-enrol device from the JSS + removed profiles.
jamf removeMDMprofile
jamf removeFramework

sleep 15

killall "Self Service"

reboot