cbb-flair-updater
=================

Small script for generating updated flair spritesheet and css for /r/CollegeBasketball

Dependencies
------
* Pillow

Instructions
------
run get_logos.py
Upload the png to subreddit stylesheep page. Copy CSS contents to subreddit stylesheet, overwriting current specific flair styles. Make sure the base selector(s) for flairs points to the new image. If new teams have been added, make sure to add them to the base flair selectors. 
