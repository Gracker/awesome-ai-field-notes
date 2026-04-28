# Prompt users to update to your latest app version

> 原文链接: https://android-developers.googleblog.com/2024/01/prompt-users-to-update-to-your-latest-app-version-google-play.html

---
29 January 2024

# Prompt users to update to your latest app version

* * *

Share this post [![Share on LinkedIn](images/img_001.svg) LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://android-developers.googleblog.com/2024/01/prompt-users-to-update-to-your-latest-app-version-google-play.html&title=Prompt users to update to your latest app version)[![Share on X](images/img_002.svg) Twitter ](https://x.com/share?text=Android Developers Blog: Prompt users to update to your latest app version&url=https://android-developers.googleblog.com/2024/01/prompt-users-to-update-to-your-latest-app-version-google-play.html&via=google)[![Share on Facebook](images/img_003.svg) Facebook ](https://www.facebook.com/sharer.php?u=https://android-developers.googleblog.com/2024/01/prompt-users-to-update-to-your-latest-app-version-google-play.html)[![Share in mail](images/img_004.svg) Email ](mailto:?subject=Prompt users to update to your latest app version&body=https://android-developers.googleblog.com/2024/01/prompt-users-to-update-to-your-latest-app-version-google-play.html)![Copy link](images/img_005.svg) Copy link

Link copied to clipboard

 ![](images/img_006.png) _Posted by Lidia Gaymond – Product Manager, Google Play_ [![](images/img_007.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVf1xFfP7lv0klpYSL7CyQ7KvpPFIWmRSwS2JHzzeLy43LkVZp82t1EpFkbLcTQMcPNOpxtWv8ntPTglOpjnutQ4Sn8nUzgMbiRBZMBKlHGIte6DjxAg_oP2PWrbTQ1dd-YXSgvRcrlm1gpDWU7Dju5Yc8ecMCIdvFr11gnd5AMO4nDQ3EKFUouM3z-vs/s1600/HEADER-Prompt-users-on-the-outdated-versions-to-update.png)

For years, Google Play has helped users enjoy the latest versions of your app through auto-updates or in-app updates. While most users update their apps this way, some may still be stuck on outdated, unsupported or broken versions of your app.

Today, we are introducing [a new tool that will prompt these users to update](https://support.google.com/googleplay/android-developer/answer/13812041?hl=en), bringing them closer to the app experience you intended to deliver.

Play recovery tools allow you to prompt users running specific versions of your app to update every time they restart the app.

![Image of side by side mobile device screens showing how the prompt to update may look to users](images/img_008.png)

_**Note:** Images are examples and subject to change_

To use this new feature, log into [Google Play Console](http://play.google.com/console) and head to your Releases or to the App Bundle Explorer page, where you can select the app versions where you want to deliver the prompts. Alternatively, the feature is also available via the [Play Developer API](https://developers.google.com/android-publisher/api-ref/rest/v3/apprecovery/create), and will soon be extended to allow you to target multiple app versions at once. Please note that the version you want to deploy the prompt to needs to be built as an [app bundle](https://developer.android.com/guide/app-bundle).

You can then narrow your targeting criteria by country or Android version (if required), with no prior integration necessary.

Currently, over 50% of users are responding to the prompts, enabling more users to get the best experience of your apps.

After prompting users to update, you can use Play Console's recovery tools to edit your update configuration, view its progress, or cancel the recovery action altogether. Learn more about the feature [here](https://support.google.com/googleplay/android-developer/answer/13812041?hl=en) and start using it today!

* * *

[android developers](https://android-developers.googleblog.com/search/label/android%20developers?max-results=12) [Best Practices](https://android-developers.googleblog.com/search/label/Best%20Practices?max-results=12) [Featured](https://android-developers.googleblog.com/search/label/Featured?max-results=12) [Google Play](https://android-developers.googleblog.com/search/label/Google%20Play?max-results=12)

[Newer post](https://android-developers.googleblog.com/2024/02/cloud-photos-now-available-in-android-photo-picker.html "Newer Post") [Older post](https://android-developers.googleblog.com/2024/01/whats-new-in-jetpack-compose-january-24-release.html "Older Post")